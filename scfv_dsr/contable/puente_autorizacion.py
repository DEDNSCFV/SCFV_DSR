"""
SCFV v8.2 — F3B.6-E
Puente de Autorización H₂ → Máquina de Estados.

Responsabilidad:
    Convertir una DecisionProfesional H₂ ya emitida y verificable
    en una transición EVALUADO → ADMITIDO.

NO:
    - decide
    - crea decisiones H₂
    - persiste decisiones
    - genera consecuencias
    - genera asientos
    - ejecuta Sagas
    - ejecuta MotorContable

El estado pertenece a MaquinaEstadosAsiento.
La autoridad H₂ pertenece a DecisionProfesional + Verificador.
"""

from typing import Dict

from scfv_dsr.contable.estados import EstadoAsiento, TipoDecisionH2
from scfv_dsr.contable.maquina_estados_asiento import (
    MaquinaEstadosAsiento,
    Transicion,
)
from scfv_dsr.epistemologico.models import DecisionProfesional
from scfv_dsr.contable.verificador_autorizacion import (
    VerificadorAutorizacion,
)


class PuenteAutorizacion:
    """
    Puente explícito entre H₂ y la máquina de estados.

    El puente NO posee autoridad decisoria.
    Solamente verifica una decisión ya existente y solicita
    a la máquina la transición EVALUADO → ADMITIDO.
    """

    def __init__(self, maquina: MaquinaEstadosAsiento):
        self.maquina = maquina

    @staticmethod
    def _es_aceptar(tipo_decision) -> bool:
        """
        Compatibilidad con TipoDecisionH2 y representación string.
        """
        if isinstance(tipo_decision, TipoDecisionH2):
            return tipo_decision == TipoDecisionH2.ACEPTAR

        return str(tipo_decision).upper() == "ACEPTAR"

    def autorizar_admitido(
        self,
        decision: DecisionProfesional,
        correlation_id: str,
        version_contexto: Dict,
        verificador: VerificadorAutorizacion,
    ) -> Transicion:
        """
        Autoriza la transición EVALUADO → ADMITIDO.

        Preconditions:
            - existe decisión H₂
            - decisión = ACEPTAR
            - existe propuesta H₁
            - existe firma H₂
            - correlation_id coincide
            - máquina está en EVALUADO
            - Verificador confirma autoridad

        Postcondition:
            - máquina queda en ADMITIDO
            - propuesta_original_id conserva propuesta_h1_id

        Raises:
            ValueError: ante cualquier violación contractual.
        """

        if decision is None:
            raise ValueError(
                "F3B6E: falta DecisionProfesional"
            )

        if self.maquina.estado_actual != EstadoAsiento.EVALUADO:
            raise ValueError(
                "F3B6E: la máquina debe estar en EVALUADO"
            )

        if not self._es_aceptar(decision.tipo_decision):
            raise ValueError(
                "F3B6E: la decisión H₂ no es ACEPTAR"
            )

        if not decision.decision_id:
            raise ValueError(
                "F3B6E: falta decision_id"
            )

        if not decision.propuesta_h1_id:
            raise ValueError(
                "F3B6E: falta propuesta_h1_id"
            )

        if not decision.firma_h2:
            raise ValueError(
                "F3B6E: falta firma_h2"
            )

        if not correlation_id:
            raise ValueError(
                "F3B6E: falta correlation_id"
            )

        if decision.correlation_id != correlation_id:
            raise ValueError(
                "F3B6E: correlation_id inconsistente"
            )

        if not decision.justificacion:
            raise ValueError(
                "F3B6E: falta justificación H₂"
            )

        autorizado = verificador.esta_autorizado(
            propuesta_id=decision.propuesta_h1_id,
            decision_id=decision.decision_id,
            firma_h2=decision.firma_h2,
            correlation_id=correlation_id,
        )

        if not autorizado:
            raise ValueError(
                "F3B6E: Verificador rechazó la autorización H₂"
            )

        # La identidad de propuesta pertenece a H₁.
        # correlation_id NO se utiliza como sustituto.
        self.maquina.propuesta_original_id = decision.propuesta_h1_id

        transicion = self.maquina.transicionar(
            nuevo_estado=EstadoAsiento.ADMITIDO,
            autor=decision.autor,
            correlation_id=correlation_id,
            version_contexto=version_contexto,
            justificacion=decision.justificacion,
            metadata={
                "decision_id": decision.decision_id,
                "firma_h2": decision.firma_h2,
                "propuesta_h1_id": decision.propuesta_h1_id,
                "autor_h2": decision.autor,
            },
        )

        return transicion
