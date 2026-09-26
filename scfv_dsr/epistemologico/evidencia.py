"""
SCFV v8.2 — Modelo de Evidencia (Fase B)
Autor: Domingo E. Díaz N. (C.P.C. Nº 183594)
Fecha: 2026-09-04

Representa la fuente original ingresada al SCFV, antes de cualquier interpretación.
Contiene identidad, procedencia, contenido original y trazabilidad.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any
import uuid
import time
import hashlib
import json

from scfv_dsr.infraestructura.serializador_canonico import serializar


def _hacer_inmutable(obj: Any) -> Any:
    """
    Convierte recursivamente estructuras mutables (dict, list)
    en estructuras inmutables (frozenset, tuple).
    """
    if isinstance(obj, dict):
        return frozenset(
            (_hacer_inmutable(k), _hacer_inmutable(v))
            for k, v in obj.items()
        )

    if isinstance(obj, list):
        return tuple(_hacer_inmutable(v) for v in obj)

    return obj


@dataclass(frozen=True)
class Evidencia:
    """
    Evidencia: fuente original adquirida por el SCFV.
    Inmutable, no contiene interpretaciones contables.
    """

    evidencia_id: str
    hash_evidencia: str

    tipo: str
    origen: str
    referencia: Optional[str]

    contenido_original: str

    timestamp_adquisicion: int
    correlation_id: str

    metadata: Any = field(default_factory=dict)

    def __post_init__(self):
        # 1. Contenido obligatorio
        if not self.contenido_original or self.contenido_original.strip() == "":
            raise ValueError(
                "EVIDENCIA_VIOLACION: "
                "contenido_original no puede estar vacío"
            )

        # 2. Metadata sin campos semántico-contables
        campos_prohibidos = [
            "monto",
            "rif",
            "fecha",
            "moneda",
            "cuenta",
            "iva",
            "impuesto",
            "total",
        ]

        if isinstance(self.metadata, dict):
            for key in campos_prohibidos:
                if key in self.metadata:
                    raise ValueError(
                        "EVIDENCIA_VIOLACION: "
                        f"metadata contiene campo interpretado '{key}'"
                    )

            object.__setattr__(
                self,
                "metadata",
                _hacer_inmutable(self.metadata)
            )

        elif isinstance(self.metadata, frozenset):
            for item in self.metadata:
                if isinstance(item, tuple) and len(item) == 2:
                    key = item[0]
                    if key in campos_prohibidos:
                        raise ValueError(
                            "EVIDENCIA_VIOLACION: "
                            f"metadata contiene campo interpretado '{key}'"
                        )

    @staticmethod
    def calcular_hash(
        contenido: str,
        tipo: str,
        origen: str,
        metadata: Any = None
    ) -> str:
        """
        Calcula hash SHA-256 determinista de la evidencia.

        No incluye timestamp_adquisicion ni correlation_id.
        """

        if isinstance(metadata, frozenset):
            metadata_dict = dict(metadata)
        else:
            metadata_dict = metadata or {}

        payload = {
            "contenido": contenido,
            "tipo": tipo,
            "origen": origen,
            "metadata": {
                k: v
                for k, v in metadata_dict.items()
                if k not in ["timestamp", "correlation_id"]
            },
        }

        serializado = serializar(payload)

        return hashlib.sha256(
            json.dumps(
                serializado,
                sort_keys=True
            ).encode()
        ).hexdigest()

    @classmethod
    def crear(
        cls,
        tipo: str,
        origen: str,
        contenido_original: str,
        correlation_id: Optional[str] = None,
        referencia: Optional[str] = None,
        metadata: Optional[Dict] = None,
    ) -> "Evidencia":

        evidencia_id = str(uuid.uuid4())

        correlation_id = (
            correlation_id
            or str(uuid.uuid4())
        )

        timestamp = int(time.time())

        hash_evidencia = cls.calcular_hash(
            contenido_original,
            tipo,
            origen,
            metadata,
        )

        return cls(
            evidencia_id=evidencia_id,
            hash_evidencia=hash_evidencia,
            tipo=tipo,
            origen=origen,
            referencia=referencia or origen,
            contenido_original=contenido_original,
            timestamp_adquisicion=timestamp,
            correlation_id=correlation_id,
            metadata=metadata or {},
        )
