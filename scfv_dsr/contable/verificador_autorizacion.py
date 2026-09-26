"""
SCFV v8.2 — Verificador de Autorización H₂

F3B.6.6

Responsabilidad:
    Verificar que una DecisionProfesional:
        - exista;
        - tenga firma coincidente;
        - pertenezca a la propuesta H₁ indicada;
        - pertenezca a la misma correlation_id.

El Verificador NO:
    - crea decisiones;
    - decide;
    - cambia estados;
    - genera consecuencias;
    - genera asientos.

Compatibilidad:
    Se mantiene estado_actual como parámetro opcional de compatibilidad
    con el contrato anterior del Motor Contable.

    Cuando se suministra estado_actual, se valida que sea ADMITIDO.

    La Máquina de Estados es responsable de demostrar la transición
    EVALUADO → ADMITIDO mediante autorizar_admitido().
"""


class VerificadorAutorizacion:

    def __init__(self, decision_provider):
        """
        decision_provider:
            objeto que implementa:

                obtener_decision(decision_id)

            y devuelve un objeto con:
                firma_h2
                propuesta_h1_id
                correlation_id
        """
        self.decision_provider = decision_provider

    def esta_autorizado(
        self,
        propuesta_id: str,
        decision_id: str,
        firma_h2: str,
        correlation_id: str,
        estado_actual: str = None
    ) -> bool:
        """
        Verifica la autorización de una DecisionProfesional.

        Compatibilidad v8.1/v8.2:
            Si estado_actual se proporciona, debe ser ADMITIDO.

        Nuevo puente F3B.6.6:
            La Máquina puede invocar este método sin depender
            de estado_actual para validar la identidad y autoridad
            de la decisión H₂.
        """

        # --------------------------------------------------------
        # 1. La decisión debe existir
        # --------------------------------------------------------

        decision = self.decision_provider.obtener_decision(
            decision_id
        )

        if not decision:
            return False

        # --------------------------------------------------------
        # 2. Firma H₂
        # --------------------------------------------------------

        if decision.firma_h2 != firma_h2:
            return False

        # --------------------------------------------------------
        # 3. Vinculación con propuesta H₁
        # --------------------------------------------------------

        if decision.propuesta_h1_id != propuesta_id:
            return False

        # --------------------------------------------------------
        # 4. Vinculación causal
        # --------------------------------------------------------

        if decision.correlation_id != correlation_id:
            return False

        # --------------------------------------------------------
        # 5. Compatibilidad con contrato anterior
        #
        # El Motor todavía puede exigir:
        #     estado_actual == "ADMITIDO"
        #
        # La Máquina NO necesita suministrarlo.
        # --------------------------------------------------------

        if estado_actual is not None:
            if estado_actual != "ADMITIDO":
                return False

        return True
