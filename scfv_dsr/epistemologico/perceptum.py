"""
SCFV v6.1 — Perceptum (Percepción de Evidencia)
Autor: Domingo E. Díaz N. (C.P.C. Nº 183594)
Fecha: 2026-09-05

D.3 — Adaptación del Perceptum al contrato Evidencia.

Responsabilidad:
    Evidencia -> ObservacionH1

Perceptum NO:
    - adquiere evidencia
    - modifica evidencia
    - genera HechoEconomico
    - genera PropuestaH1
    - decide H2

S0 — Extensión DA-1:
    extraer_lote(evidencia) -> List[ObservacionH1]
    Segmenta CSV (registro base 1) o JSON array (índice base 1).
    extraer() permanece intacto (contrato D3/D4).
"""

import csv
import io
import json
import time
import uuid
from typing import Any, Dict, List, Optional, Tuple

from scfv_dsr.contable.estados import EstadoEpistemico
from scfv_dsr.epistemologico.evidencia import Evidencia
from scfv_dsr.epistemologico.models import (
    ObservacionH1,
    EntidadExtraida,
)


class Perceptum:

    @staticmethod
    def _extraer_entidades(evidencia: Evidencia) -> List[EntidadExtraida]:
        """
        Extrae entidades únicamente desde el contenido original.

        En D.3 se soporta contenido JSON estructurado.
        Otros formatos quedan disponibles para adaptadores perceptivos
        posteriores (OCR/parser/etc.).
        """
        entidades: List[EntidadExtraida] = []

        if evidencia.tipo.upper() == "JSON":
            try:
                datos = json.loads(evidencia.contenido_original)
            except (json.JSONDecodeError, TypeError):
                return entidades

            if isinstance(datos, dict):
                for campo, valor in datos.items():
                    confianza = 0.95 if valor not in (None, "") else 0.0
                    entidades.append(
                        EntidadExtraida(
                            campo=str(campo),
                            valor=valor,
                            confianza=confianza,
                        )
                    )

        return entidades

    @staticmethod
    def extraer(evidencia: Evidencia) -> ObservacionH1:
        """
        Convierte una Evidencia inmutable en una ObservacionH1.

        Conserva:
            - evidencia_id
            - hash_evidencia
            - correlation_id

        Genera:
            - observacion_id
            - timestamp de percepción

        No modifica la Evidencia.
        """
        if not isinstance(evidencia, Evidencia):
            raise TypeError(
                "PERCEPTUM: se requiere una instancia de Evidencia"
            )

        observacion_id = str(uuid.uuid4())
        timestamp = int(time.time())

        entidades = Perceptum._extraer_entidades(evidencia)

        confianza_global = min(
            (entidad.confianza for entidad in entidades),
            default=0.0,
        )

        if confianza_global < 0.60:
            print(
                f"⚠️ ALTA_INCERTIDUMBRE: "
                f"confianza_global={confianza_global}"
            )

        return ObservacionH1(
            observacion_id=observacion_id,
            evidencia_id=evidencia.evidencia_id,
            entidades=entidades,
            confianza_global=confianza_global,
            timestamp=timestamp,
            correlation_id=evidencia.correlation_id,
            estado_epistemico=EstadoEpistemico.OBSERVADO,
            hash_evidencia=evidencia.hash_evidencia,
        )

    # ------------------------------------------------------------------
    # S0 — Segmentación de lotes (DA-1)
    # ------------------------------------------------------------------

    @staticmethod
    def _validar_referencia_fuente(ref: Dict[str, Any]) -> None:
        """
        Validación estructural de referencia_fuente.

        Tipos conocidos S0: CSV_ROW, JSON_INDEX, TXT_LINE.
        Tipos futuros pasan sin validación específica.
        """
        if not isinstance(ref, dict):
            raise ValueError("referencia_fuente debe ser dict")
        tipo = ref.get("tipo")
        if not isinstance(tipo, str):
            raise ValueError("referencia_fuente.tipo debe ser str")

        if tipo == "CSV_ROW":
            if not isinstance(ref.get("registro"), int):
                raise ValueError("CSV_ROW requiere registro int")
        elif tipo == "JSON_INDEX":
            if not isinstance(ref.get("indice"), int):
                raise ValueError("JSON_INDEX requiere indice int")
        elif tipo == "TXT_LINE":
            if not isinstance(ref.get("linea"), int):
                raise ValueError("TXT_LINE requiere linea int")

    @staticmethod
    def _segmentar_csv(evidencia: Evidencia) -> List[Tuple[Dict[str, Any], Dict[str, Any]]]:
        """
        Segmenta contenido CSV en pares (fila_dict, referencia_fuente).

        Base 1: primera fila de datos = registro 1 (header excluido).
        """
        unidades: List[Tuple[Dict[str, Any], Dict[str, Any]]] = []
        try:
            reader = csv.DictReader(io.StringIO(evidencia.contenido_original))
            for i, fila in enumerate(reader, start=1):
                referencia = {"tipo": "CSV_ROW", "registro": i}
                unidades.append((fila, referencia))
        except Exception:
            return []
        return unidades

    @staticmethod
    def _segmentar_json_array(evidencia: Evidencia) -> List[Tuple[Any, Dict[str, Any]]]:
        """
        Segmenta contenido JSON array en pares (item, referencia_fuente).

        Base 1: primer elemento del array = indice 1.
        Si el JSON no es array, devuelve lista vacía.
        """
        try:
            datos = json.loads(evidencia.contenido_original)
        except (json.JSONDecodeError, TypeError):
            return []

        if not isinstance(datos, list):
            return []

        unidades: List[Tuple[Any, Dict[str, Any]]] = []
        for i, item in enumerate(datos, start=1):
            referencia = {"tipo": "JSON_INDEX", "indice": i}
            unidades.append((item, referencia))
        return unidades

    @staticmethod
    def _entidades_desde_dict(datos: Any) -> List[EntidadExtraida]:
        """
        Construye entidades desde un dict (fila CSV o item JSON array).
        No admite listas ni escalares.
        """
        entidades: List[EntidadExtraida] = []
        if not isinstance(datos, dict):
            return entidades
        for campo, valor in datos.items():
            confianza = 0.95 if valor not in (None, "") else 0.0
            entidades.append(
                EntidadExtraida(
                    campo=str(campo),
                    valor=valor,
                    confianza=confianza,
                )
            )
        return entidades

    @staticmethod
    def _construir_observacion(
        evidencia: Evidencia,
        entidades: List[EntidadExtraida],
        referencia_fuente: Optional[Dict[str, Any]],
    ) -> ObservacionH1:
        """Construye ObservacionH1 compartiendo identidad con la Evidencia origen."""
        observacion_id = str(uuid.uuid4())
        timestamp = int(time.time())

        confianza_global = min(
            (entidad.confianza for entidad in entidades),
            default=0.0,
        )

        if confianza_global < 0.60:
            print(
                f"⚠️ ALTA_INCERTIDUMBRE: "
                f"confianza_global={confianza_global}"
            )

        return ObservacionH1(
            observacion_id=observacion_id,
            evidencia_id=evidencia.evidencia_id,
            entidades=entidades,
            confianza_global=confianza_global,
            timestamp=timestamp,
            correlation_id=evidencia.correlation_id,
            estado_epistemico=EstadoEpistemico.OBSERVADO,
            hash_evidencia=evidencia.hash_evidencia,
            referencia_fuente=referencia_fuente,
        )

    @staticmethod
    def extraer_lote(evidencia: Evidencia) -> List[ObservacionH1]:
        """
        Segmenta una Evidencia masiva en N ObservacionH1.

        Soporta:
            - CSV con header: N filas -> N observaciones, referencia CSV_ROW.
            - JSON array: N items -> N observaciones, referencia JSON_INDEX.
            - JSON objeto: 1 observación (delega en extraer()).

        Otros tipos devuelven lista vacía.

        No modifica la Evidencia.
        """
        if not isinstance(evidencia, Evidencia):
            raise TypeError(
                "PERCEPTUM: se requiere una instancia de Evidencia"
            )

        tipo = evidencia.tipo.upper()

        if tipo == "CSV":
            unidades = Perceptum._segmentar_csv(evidencia)
        elif tipo == "JSON":
            unidades = Perceptum._segmentar_json_array(evidencia)
            if not unidades:
                try:
                    datos = json.loads(evidencia.contenido_original)
                    if isinstance(datos, dict):
                        return [Perceptum.extraer(evidencia)]
                except (json.JSONDecodeError, TypeError):
                    pass
                return []
        else:
            return []

        observaciones: List[ObservacionH1] = []
        for contenido, referencia in unidades:
            Perceptum._validar_referencia_fuente(referencia)
            entidades = Perceptum._entidades_desde_dict(contenido)
            obs = Perceptum._construir_observacion(
                evidencia, entidades, referencia
            )
            observaciones.append(obs)

        return observaciones
