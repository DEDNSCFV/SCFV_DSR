"""
SCFV v8.2 — Event Store
F3B.4-INFRA-D.3

Propósito:
    Persistencia de eventos con representación canónica.

Principios:
    - EventStore permanece genérico.
    - No interpreta dominio contable.
    - No conoce H1, H2, Motor ni Verificador.
    - La representación persistida utiliza el Serializador Canónico.
    - Los Enum se almacenan mediante Enum.name.
    - Los datetimes se almacenan en ISO 8601.
    - Los objetos no soportados provocan PersistenciaViolacion.
    - La cadena hash utiliza exactamente las representaciones
      canónicas persistidas de payload y version_contexto.
"""

import sqlite3
import json
from contextlib import contextmanager
import hashlib
import time

from typing import Dict, Optional, List

from scfv_dsr.infraestructura.serializador_canonico import (
    serializar,
)


class EventStore:
    """
    Almacén genérico de eventos.

    EventStore no interpreta el significado del evento.
    Solo persiste y recupera representaciones canónicas.
    """

    GENESIS_HASH = "0" * 64

    def __init__(self, db_path: str = "scfv.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._en_transaccion = False
        self._init_tables()

    def _init_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS event_store (
                id INTEGER PRIMARY KEY,
                tipo_evento TEXT NOT NULL,
                payload TEXT NOT NULL,
                correlation_id TEXT NOT NULL,
                idempotency_key TEXT UNIQUE NOT NULL,
                hash_previo TEXT NOT NULL,
                hash_actual TEXT NOT NULL,
                timestamp INTEGER NOT NULL,
                version_contexto TEXT
            )
        """)

        self.conn.commit()

    def guardar(
        self,
        tipo_evento: str,
        payload: Dict,
        correlation_id: str,
        idempotency_key: str,
        version_contexto: Optional[Dict] = None,
        commit: bool = True,
    ) -> None:
        """
        Persiste un evento utilizando exclusivamente representación canónica.

        D.3:
            tipo_evento
                Enum -> .name
                str  -> str

            payload
                serializado mediante serializar()

            version_contexto
                serializado mediante serializar()

        No se utiliza default=str.
        """

        if not commit and not self._en_transaccion:
            raise RuntimeError(
                "guardar(commit=False) requiere estar dentro de "
                "store.transaccion(). Sin CM, la transacción "
                "implícita de sqlite3 no se cierra y quedan locks."
            )

        cursor = self.conn.cursor()

        # ---------------------------------------------------------------
        # 1. Obtener hash anterior
        # ---------------------------------------------------------------

        cursor.execute(
            """
            SELECT hash_actual
            FROM event_store
            ORDER BY id DESC
            LIMIT 1
            """
        )

        row = cursor.fetchone()

        hash_previo = (
            row[0]
            if row
            else self.GENESIS_HASH
        )

        # ---------------------------------------------------------------
        # 2. Normalización canónica del tipo de evento
        # ---------------------------------------------------------------

        tipo_evento_canonico = serializar(tipo_evento)

        if not isinstance(tipo_evento_canonico, (str, int, float, bool)):
            raise TypeError(
                "tipo_evento debe producir una representación escalar "
                "compatible con SQLite"
            )

        # ---------------------------------------------------------------
        # 3. Serialización canónica del payload
        # ---------------------------------------------------------------

        payload_canonico = serializar(payload)

        payload_json = json.dumps(
            payload_canonico,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":")
        )

        # ---------------------------------------------------------------
        # 4. Serialización canónica del contexto
        # ---------------------------------------------------------------

        version_canonica = serializar(
            version_contexto
        ) if version_contexto is not None else {}

        version_json = json.dumps(
            version_canonica,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":")
        )

        # ---------------------------------------------------------------
        # 5. Construcción determinista de la cadena hash
        # ---------------------------------------------------------------

        datos = (
            payload_json
            + version_json
            + correlation_id
            + idempotency_key
            + hash_previo
        )

        hash_actual = hashlib.sha256(
            datos.encode("utf-8")
        ).hexdigest()

        timestamp = int(time.time())

        # ---------------------------------------------------------------
        # 6. Persistencia
        # ---------------------------------------------------------------

        cursor.execute(
            """
            INSERT INTO event_store (
                tipo_evento,
                payload,
                correlation_id,
                idempotency_key,
                hash_previo,
                hash_actual,
                timestamp,
                version_contexto
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                tipo_evento_canonico,
                payload_json,
                correlation_id,
                idempotency_key,
                hash_previo,
                hash_actual,
                timestamp,
                version_json
            )
        )

        if commit:
            self.conn.commit()

    def obtener_hash_final(self) -> str:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT hash_actual
            FROM event_store
            ORDER BY id DESC
            LIMIT 1
            """
        )

        row = cursor.fetchone()

        return (
            row[0]
            if row
            else self.GENESIS_HASH
        )

    def verificar_cadena(self) -> tuple:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                hash_previo,
                hash_actual,
                payload,
                version_contexto,
                correlation_id,
                idempotency_key
            FROM event_store
            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        hash_esperado = self.GENESIS_HASH

        for row in rows:

            if row["hash_previo"] != hash_esperado:
                return (
                    False,
                    f"Cadena rota en evento {row['id']}"
                )

            version_json = (
                row["version_contexto"]
                or "{}"
            )

            payload_json = row["payload"]

            datos = (
                payload_json
                + version_json
                + row["correlation_id"]
                + row["idempotency_key"]
                + row["hash_previo"]
            )

            recomputado = hashlib.sha256(
                datos.encode("utf-8")
            ).hexdigest()

            if recomputado != row["hash_actual"]:
                return (
                    False,
                    f"Hash inválido en evento {row['id']}"
                )

            hash_esperado = row["hash_actual"]

        return True, "CADENA_INTEGRA"

    def obtener_por_id(
        self,
        evento_id: int
    ) -> Optional[Dict]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                tipo_evento,
                payload,
                correlation_id,
                idempotency_key,
                hash_previo,
                hash_actual,
                timestamp,
                version_contexto
            FROM event_store
            WHERE id = ?
            """,
            (evento_id,)
        )

        row = cursor.fetchone()

        if not row:
            return None

        return {
            "id": row[0],
            "tipo_evento": row[1],
            "payload": json.loads(row[2]),
            "correlation_id": row[3],
            "idempotency_key": row[4],
            "hash_previo": row[5],
            "hash_actual": row[6],
            "timestamp": row[7],
            "version_contexto": json.loads(row[8]) if row[8] else None,
        }

    def obtener_por_tipo(
        self,
        tipo_evento: str,
        limite: Optional[int] = None
    ) -> List[Dict]:
        """
        Obtiene eventos de un tipo específico.

        EventStore permanece genérico:
        no interpreta el dominio del evento.
        """

        cursor = self.conn.cursor()

        tipo_evento_canonico = serializar(tipo_evento)

        if limite is not None:

            cursor.execute(
                """
                SELECT
                    id,
                    tipo_evento,
                    payload,
                    correlation_id,
                    idempotency_key,
                    hash_previo,
                    hash_actual,
                    timestamp,
                    version_contexto
                FROM event_store
                WHERE tipo_evento = ?
                ORDER BY timestamp DESC, id DESC
                LIMIT ?
                """,
                (
                    tipo_evento_canonico,
                    limite
                )
            )

        else:

            cursor.execute(
                """
                SELECT
                    id,
                    tipo_evento,
                    payload,
                    correlation_id,
                    idempotency_key,
                    hash_previo,
                    hash_actual,
                    timestamp,
                    version_contexto
                FROM event_store
                WHERE tipo_evento = ?
                ORDER BY timestamp DESC, id DESC
                """,
                (tipo_evento_canonico,)
            )

        rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "tipo_evento": row[1],
                "payload": json.loads(row[2]),
                "correlation_id": row[3],
                "idempotency_key": row[4],
                "hash_previo": row[5],
                "hash_actual": row[6],
                "timestamp": row[7],
                "version_contexto": (
                    json.loads(row[8])
                    if row[8]
                    else None
                ),
            }
            for row in rows
        ]

    def cerrar(self):
        self.conn.close()

    @contextmanager
    def transaccion(self):
        """Context manager transaccional.
        
        Con isolation_level='' (default de sqlite3), Python abre
        transacción implícita en la primera DML y la cierra en el
        próximo commit()/rollback(). Este CM coordina el cierre.
        Reentrada: si ya estamos dentro, hace yield sin commit propio.
        """
        if self._en_transaccion:
            yield self
            return
        self._en_transaccion = True
        try:
            yield self
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise
        finally:
            self._en_transaccion = False

    def obtener_por_correlation(
        self,
        correlation_id: str
    ) -> Optional[Dict]:
        """
        Obtiene el primer evento con un correlation_id dado (I10).
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                tipo_evento,
                payload,
                correlation_id,
                idempotency_key,
                hash_previo,
                hash_actual,
                timestamp,
                version_contexto
            FROM event_store
            WHERE correlation_id = ?
            """,
            (correlation_id,)
        )

        row = cursor.fetchone()

        if not row:
            return None

        return {
            "id": row[0],
            "tipo_evento": row[1],
            "payload": json.loads(row[2]),
            "correlation_id": row[3],
            "idempotency_key": row[4],
            "hash_previo": row[5],
            "hash_actual": row[6],
            "timestamp": row[7],
            "version_contexto": json.loads(row[8]) if row[8] else None,
        }


