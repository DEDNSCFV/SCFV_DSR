"""
SCFV v8.2 — H₂ Decisión Profesional
"""

import hashlib
import os
import time
import uuid
from typing import Dict, List, Optional

from scfv_dsr.contable.estados import TipoDecisionH2, TipoEvento, VersionContexto
from scfv_dsr.contable.event_store import EventStore
from scfv_dsr.epistemologico.models import PropuestaH1, DecisionProfesional


def _validar_modo_prueba(modo_auto: bool) -> None:
    if modo_auto and os.getenv("SCFV_MODO_PRUEBA") != "1":
        raise RuntimeError(
            "H2_VIOLACION: modo_auto=True requiere SCFV_MODO_PRUEBA=1"
        )


def _firmar_decision(
    decision_id: str,
    justificacion: str,
    autor: str,
    timestamp: int,
) -> str:
    contenido = (
        f"{decision_id}|"
        f"{justificacion}|"
        f"{autor}|"
        f"{timestamp}"
    )
    return hashlib.sha256(contenido.encode("utf-8")).hexdigest()


class H2Decision:

    @staticmethod
    def decidir(
        propuesta_original: PropuestaH1,
        alertas: List[str],
        contexto: VersionContexto,
        event_store: EventStore,
        modo_auto: bool = False,
        tipo_decision: TipoDecisionH2 = TipoDecisionH2.ACEPTAR,
        justificacion: Optional[str] = None,
        autor: Optional[str] = None,
    ) -> Dict:

        if propuesta_original is None:
            raise ValueError("H₂ requiere PropuestaH1")

        _validar_modo_prueba(modo_auto)

        autor_final = (
            autor
            or os.getenv(
                "SCFV_CPC_PROFESIONAL",
                "PROFESIONAL_NO_IDENTIFICADO"
            )
        )

        if modo_auto:
            justificacion_final = "Decisión automática en prueba"
        else:
            if not justificacion or not justificacion.strip():
                raise ValueError(
                    "H₂ requiere justificación profesional"
                )
            justificacion_final = justificacion.strip()

        decision_id = str(uuid.uuid4())
        timestamp = int(time.time())

        tipo_final = (
            tipo_decision.name
            if isinstance(tipo_decision, TipoDecisionH2)
            else str(tipo_decision)
        )

        idempotency_key = hashlib.sha256(
            f"DECISION_H2|{propuesta_original.propuesta_id}|"
            f"{propuesta_original.correlation_id}".encode("utf-8")
        ).hexdigest()

        firma_h2 = _firmar_decision(
            decision_id=decision_id,
            justificacion=justificacion_final,
            autor=autor_final,
            timestamp=timestamp,
        )

        decision = DecisionProfesional(
            decision_id=decision_id,
            propuesta_h1_id=propuesta_original.propuesta_id,
            propuesta_h2_id=None,
            tipo_decision=tipo_final,
            justificacion=justificacion_final,
            autor=autor_final,
            timestamp=timestamp,
            correlation_id=propuesta_original.correlation_id,
            idempotency_key=idempotency_key,
            firma_h2=firma_h2,
        )

        event_store.guardar(
            TipoEvento.DECISION_H2,
            decision,
            decision.correlation_id,
            decision.idempotency_key,
            contexto,
        )

        return {
            "decision": decision,
            "tipo": tipo_final,
            "firma_h2": firma_h2,
        }
