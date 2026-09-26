"""
Soporte mínimo U-SEQ-01 · lectura
Lee eventos ASIENTO_REGISTRADO de event_store y devuelve payload parseado.

Acto 11 · soporte mínimo · pre-registro vE vigente.
Sin modificar la DB. Sólo lectura.
"""
import json
import sqlite3
from pathlib import Path


def leer_eventos_asiento(db_path):
    """
    Devuelve lista de dicts:
      {id, tipo_evento, payload (dict), correlation_id,
       hash_previo, hash_actual, timestamp, version_contexto (dict|None)}
    Sólo incluye tipo_evento='ASIENTO_REGISTRADO'.
    """
    p = Path(db_path)
    if not p.is_file():
        raise FileNotFoundError(f"DB no encontrada: {db_path}")

    conn = sqlite3.connect(str(p))
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            """
            SELECT id, tipo_evento, payload, correlation_id,
                   hash_previo, hash_actual, timestamp, version_contexto
            FROM event_store
            WHERE tipo_evento = 'ASIENTO_REGISTRADO'
            ORDER BY id
            """
        ).fetchall()
    finally:
        conn.close()

    eventos = []
    for r in rows:
        payload = json.loads(r["payload"]) if r["payload"] else {}
        vc = json.loads(r["version_contexto"]) if r["version_contexto"] else None
        eventos.append({
            "id": r["id"],
            "tipo_evento": r["tipo_evento"],
            "payload": payload,
            "correlation_id": r["correlation_id"],
            "hash_previo": r["hash_previo"],
            "hash_actual": r["hash_actual"],
            "timestamp": r["timestamp"],
            "version_contexto": vc,
        })
    return eventos


if __name__ == "__main__":
    import sys
    eventos = leer_eventos_asiento(sys.argv[1])
    print(f"eventos leídos: {len(eventos)}")
    for e in eventos:
        n = len(e["payload"].get("partidas", []))
        print(f"  id={e['id']} partidas={n}")
