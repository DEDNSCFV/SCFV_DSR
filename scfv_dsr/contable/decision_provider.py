"""
SCFV v8.1+ — DecisionProvider
F3B.4-INFRA-E

Responsabilidad:
    Adaptar eventos DECISION_H2 persistidos por EventStore
    hacia objetos DecisionProfesional.

Principios:
    - EventStore permanece genérico.
    - El Provider conoce el dominio H₂.
    - El Verificador no conoce EventStore.
    - Los eventos históricos no se modifican.
    - La persistencia canónica pertenece a infraestructura.
"""

from typing import Optional

from scfv_dsr.contable.estados import TipoEvento, TipoDecisionH2
from scfv_dsr.contable.event_store import EventStore
from scfv_dsr.epistemologico.models import DecisionProfesional


class DecisionProvider:
    """
    Adaptador entre EventStore y DecisionProfesional.

    API contractual:
        obtener_decision(decision_id) -> DecisionProfesional | None
    """

    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def obtener_decision(
        self,
        decision_id: str
    ) -> Optional[DecisionProfesional]:
        """
        Recupera una decisión H₂ por su decision_id.

        El EventStore permanece genérico:
        se consulta el tipo de evento y el Provider filtra
        el payload por decision_id.
        """

        if not decision_id:
            return None

        eventos = self.event_store.obtener_por_tipo(
            TipoEvento.DECISION_H2
        )

        for evento in eventos:
            payload = evento.get("payload")

            if not isinstance(payload, dict):
                continue

            if payload.get("decision_id") != decision_id:
                continue

            tipo_decision = payload.get("tipo_decision")

            if isinstance(tipo_decision, str):
                try:
                    tipo_decision = TipoDecisionH2[tipo_decision]
                except KeyError:
                    return None

            return DecisionProfesional(
                decision_id=payload["decision_id"],
                propuesta_h1_id=payload["propuesta_h1_id"],
                propuesta_h2_id=payload.get("propuesta_h2_id"),
                tipo_decision=tipo_decision,
                justificacion=payload["justificacion"],
                autor=payload["autor"],
                timestamp=payload["timestamp"],
                correlation_id=payload["correlation_id"],
                idempotency_key=payload["idempotency_key"],
                firma_h2=payload.get("firma_h2"),
            )

        return None
