"""
SCFV v8.1+ — Modelos del Núcleo Contable (F3B.3-D)
Autor: Domingo E. Díaz N. (C.P.C. Nº 183594)
Fecha: 2026-09-02

Contiene las estructuras de datos para el Motor Contable v8.2:
ConsecuenciaAutorizada, ContextoContable, PartidaAutorizada.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class ContextoContable:
    marco_contable: str           # ej. "NIIF_Completas", "NIIF_PYMES"
    PCU_version: str              # Versión del PCU utilizada
    reglas_version: str           # Versión de reglas contables
    politica_monetaria_version: str

@dataclass
class ConsecuenciaAutorizada:
    # Identificación de la decisión H₂
    decision_id: str
    propuesta_id: str
    firma_h2: str
    correlation_id: str

    # Datos temporales y contextuales
    fecha: str                     # ISO 8601 (YYYY-MM-DD)
    periodo_id: str
    descripcion: str
    evidencia_hash: str
    timestamp: int

    # Contexto contable
    contexto_contable: ContextoContable

    # Partidas (lista de dicts con la estructura de PartidaAutorizada)
    partidas: List[Dict]

@dataclass
class PartidaAutorizada:
    cuenta_codigo: str
    cuenta_version: str            # Obligatorio
    monto: float
    ubicacion: str                 # "DEBE" o "HABER"
    movimiento: str                # "AUMENTA" o "DISMINUYE"
    moneda: Optional[str] = "VES"
    es_fiscal: bool = False
    norma_id: Optional[str] = None
