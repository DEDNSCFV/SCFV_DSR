"""
SCFV v8.1+ - Estados y Enumeraciones - EN RECTIFICACIÓN A v8.2
Autor: Domingo E. Díaz N. (C.P.C. Nº 183594)
Fecha: 2026-09-02
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class VersionContexto:
    version_id: str
    fecha_inicio: str
    fecha_fin: str
    PCU_version: str
    reglas_version: str
    politica_inventario_version: str
    marco_contable_version: str
    politica_monetaria_version: str


class EstadoEpistemico(Enum):
    OBSERVADO = auto()
    INFERIDO = auto()
    PROPUESTO = auto()
    CONFIRMADO = auto()
    RECHAZADO = auto()

class EstadoPropuesta(Enum):
    PROPUESTO = auto()
    ACEPTADO = auto()
    RECHAZADO = auto()
    MODIFICADO = auto()

class EstadoConsecuencia(Enum):
    GENERADA = auto()
    VALIDADA = auto()
    APLICADA = auto()
    RECHAZADA = auto()

class EstadoAsiento(Enum):
    PROPUESTO = auto()
    EVALUADO = auto()
    ADMITIDO = auto()
    MODIFICADO = auto()
    RECHAZADO = auto()
    ASENTADO = auto()
    ANULADO = auto()

class TipoDecisionH2(Enum):
    ACEPTAR = auto()
    MODIFICAR = auto()
    RECHAZAR = auto()

class TipoEvento(Enum):
    EVIDENCIA_ADQUIRIDA = auto()
    OBSERVACION_GENERADA = auto()
    PROPUESTA_GENERADA = auto()
    PROPUESTA_MODIFICADA = auto()
    PROPUESTA_ACEPTADA = auto()
    PROPUESTA_RECHAZADA = auto()
    HECHO_CONFIRMADO = auto()
    HECHO_RECHAZADO = auto()
    DECISION_H2 = auto()
    EVENTO_ECONOMICO = auto()
    CONSECUENCIA_GENERADA = auto()
    CONSECUENCIA_VALIDADA = auto()
    ASIENTO_PROPUESTO = auto()
    ASIENTO_REGISTRADO = auto()
    ASIENTO_ANULADO = auto()
    FRACTAL_FALLIDO = auto()
    CONSECUENCIAS_GENERADAS = auto()
    LOTE_PROCESADO = auto()

