"""
SCFV v8.1+ — Máquina de Estados del Asiento (Fase 2B)
Autor: Domingo E. Díaz N. (C.P.C. Nº 183594)
Fecha: 2026-09-02

ESTADO: Implementación aislada. Pendiente de integración con H₂ y Motor (Fase 3).
OBJETIVO: Gobernar el ciclo de vida del asiento, garantizando transiciones válidas.
PROHIBIDO: No contiene lógica contable, fiscal ni normativa.
"""

from scfv_dsr.contable.estados import EstadoAsiento
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
import uuid
import time
import hashlib


@dataclass
class Transicion:
    """Registro inmutable de una transición de estado."""
    id: str
    desde: EstadoAsiento
    hasta: EstadoAsiento
    autor: str
    timestamp: int
    justificacion: str
    correlation_id: str
    version_contexto: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)

    def hash(self) -> str:
        """Hash de integridad de la transición."""
        contenido = f"{self.id}|{self.desde.value}|{self.hasta.value}|{self.autor}|{self.timestamp}|{self.correlation_id}"
        return hashlib.sha256(contenido.encode("utf-8")).hexdigest()


class MaquinaEstadosAsiento:
    """
    Máquina de estados del asiento.
    Gobierna el ciclo de vida: PROPUESTO → EVALUADO → ADMITIDO/MODIFICADO/RECHAZADO → ASENTADO → ANULADO.
    """

    # Matriz de transiciones permitidas (desde → {hacia: precondición})
    _TRANSICIONES = {
        EstadoAsiento.PROPUESTO: {
            EstadoAsiento.EVALUADO: lambda self, **k: True,
        },
        EstadoAsiento.EVALUADO: {
            EstadoAsiento.ADMITIDO: lambda self, **k: k.get("justificacion") is not None,
            EstadoAsiento.MODIFICADO: lambda self, **k: k.get("justificacion") is not None and k.get("propuesta_modificada") is not None,
            EstadoAsiento.RECHAZADO: lambda self, **k: k.get("justificacion") is not None,
        },
        EstadoAsiento.MODIFICADO: {
            EstadoAsiento.EVALUADO: lambda self, **k: True,  # La reevaluación requiere H₂, pero la transición es técnica
        },
        EstadoAsiento.ADMITIDO: {
            EstadoAsiento.ASENTADO: lambda self, **k: True,
        },
        EstadoAsiento.ASENTADO: {
            EstadoAsiento.ANULADO: lambda self, **k: k.get("justificacion") is not None,
        },
        # Estados terminales: no tienen transiciones salientes
        EstadoAsiento.RECHAZADO: {},
        EstadoAsiento.ANULADO: {},
    }

    def __init__(self, estado_inicial: EstadoAsiento = EstadoAsiento.PROPUESTO):
        self.estado_actual = estado_inicial
        self.historial: List[Transicion] = []
        self.propuesta_original_id: Optional[str] = None
        self.propuesta_modificada_id: Optional[str] = None

    def transicionar(
        self,
        nuevo_estado: EstadoAsiento,
        autor: str,
        correlation_id: str,
        version_contexto: Dict[str, Any],
        justificacion: Optional[str] = None,
        propuesta_modificada: Optional[Dict] = None,
        metadata: Optional[Dict] = None
    ) -> Transicion:
        """
        Ejecuta una transición de estado si es permitida y cumple precondiciones.
        Lanza ValueError si la transición es inválida.
        """
        if metadata is None:
            metadata = {}

        # 1. Verificar si la transición está permitida
        if self.estado_actual not in self._TRANSICIONES:
            raise ValueError(f"Estado terminal {self.estado_actual} no permite transiciones salientes")
        if nuevo_estado not in self._TRANSICIONES[self.estado_actual]:
            raise ValueError(
                f"Transición inválida: {self.estado_actual} → {nuevo_estado}. "
                f"Transiciones permitidas desde {self.estado_actual}: {list(self._TRANSICIONES[self.estado_actual].keys())}"
            )

        # 2. Verificar precondición
        precondicion = self._TRANSICIONES[self.estado_actual][nuevo_estado]
        if not precondicion(self, justificacion=justificacion, propuesta_modificada=propuesta_modificada):
            raise ValueError(
                f"Precondición fallida para {self.estado_actual} → {nuevo_estado}. "
                f"Requisitos: {self._describir_precondicion(self.estado_actual, nuevo_estado)}"
            )

        # 3. Registrar la transición
        transicion = Transicion(
            id=str(uuid.uuid4()),
            desde=self.estado_actual,
            hasta=nuevo_estado,
            autor=autor,
            timestamp=int(time.time()),
            justificacion=justificacion or "",
            correlation_id=correlation_id,
            version_contexto=version_contexto,
            metadata={
                "propuesta_original_id": self.propuesta_original_id,
                "propuesta_modificada_id": self.propuesta_modificada_id,
                **metadata
            }
        )
        # Si es MODIFICADO, guardar referencia a la propuesta modificada
        if nuevo_estado == EstadoAsiento.MODIFICADO:
            self.propuesta_modificada_id = propuesta_modificada.get("id") if propuesta_modificada else None

        # 4. Actualizar estado
        self.historial.append(transicion)
        self.estado_actual = nuevo_estado

        # 5. Si es ADMITIDO, asegurar que tiene propuesta_original_id
        if nuevo_estado == EstadoAsiento.ADMITIDO and self.propuesta_original_id is None:
            self.propuesta_original_id = correlation_id

        return transicion

    def es_terminal(self) -> bool:
        """Indica si el estado actual es terminal."""
        return self.estado_actual in {EstadoAsiento.RECHAZADO, EstadoAsiento.ASENTADO, EstadoAsiento.ANULADO}

    def obtener_historial(self) -> List[Dict]:
        """Retorna el historial de transiciones en formato serializable."""
        return [
            {
                "id": t.id,
                "desde": t.desde.name,
                "hasta": t.hasta.name,
                "autor": t.autor,
                "timestamp": t.timestamp,
                "justificacion": t.justificacion,
                "correlation_id": t.correlation_id,
                "version_contexto": t.version_contexto,
                "metadata": t.metadata,
                "hash": t.hash()
            }
            for t in self.historial
        ]

    @staticmethod
    def _describir_precondicion(desde: EstadoAsiento, hasta: EstadoAsiento) -> str:
        """Devuelve una descripción legible de la precondición para error."""
        descripciones = {
            (EstadoAsiento.EVALUADO, EstadoAsiento.ADMITIDO): "Se requiere justificación",
            (EstadoAsiento.EVALUADO, EstadoAsiento.MODIFICADO): "Se requiere justificación y propuesta_modificada",
            (EstadoAsiento.EVALUADO, EstadoAsiento.RECHAZADO): "Se requiere justificación",
            (EstadoAsiento.ASENTADO, EstadoAsiento.ANULADO): "Se requiere justificación",
        }
        return descripciones.get((desde, hasta), "Sin requisitos adicionales")

    # ------------------------------------------------------------------
    # Métodos de consulta para el integrador/motor (Fase 3)
    # ------------------------------------------------------------------
    def puede_asentar(self) -> bool:
        """Verifica si el asiento está en estado ADMITIDO, listo para el motor."""
        return self.estado_actual == EstadoAsiento.ADMITIDO

    def puede_anular(self) -> bool:
        """Verifica si el asiento puede ser anulado (está ASENTADO)."""
        return self.estado_actual == EstadoAsiento.ASENTADO
