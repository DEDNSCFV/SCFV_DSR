"""
SCFV v8.2 — F3B.6-F
Puente Máquina de Estados → Núcleo de Consecuencias.

Responsabilidad:
    Convertir una consecuencia candidata ya admitida por la
    Máquina de Estados en una ConsecuenciaAutorizada mediante NC.

Cadena:

    DecisionProfesional
        ↓
    Máquina = ADMITIDO
        ↓
    PuenteConsecuencias
        ↓
    NucleoConsecuencias
        ↓
    ConsecuenciaAutorizada

El puente NO:
    - decide;
    - crea decisiones H₂;
    - cambia estados;
    - persiste;
    - ejecuta Sagas;
    - ejecuta MotorContable;
    - genera consecuencias económicas.

La autoridad permanece en H₂ + Verificador.
El estado permanece en la Máquina.
La construcción permanece en NC.
"""

from typing import Dict, List

from scfv_dsr.contable.estados import EstadoAsiento
from scfv_dsr.contable.maquina_estados_asiento import MaquinaEstadosAsiento
from scfv_dsr.contable.nucleo_consecuencias import NucleoConsecuencias
from scfv_dsr.contable.modelos import (
    ConsecuenciaAutorizada,
    ContextoContable,
)
from scfv_dsr.epistemologico.models import DecisionProfesional
from scfv_dsr.contable.verificador_autorizacion import VerificadorAutorizacion


class PuenteConsecuencias:
    """
    Frontera explícita entre Máquina de Estados y NC.
    """

    def __init__(
        self,
        maquina: MaquinaEstadosAsiento,
        nucleo_consecuencias: NucleoConsecuencias,
    ):
        self.maquina = maquina
        self.nc = nucleo_consecuencias

    def construir_consecuencia_autorizada(
        self,
        decision: DecisionProfesional,
        consecuencia_candidata: List[Dict],
        evidencia_hash: str,
        correlation_id: str,
        contexto_contable: ContextoContable,
        fecha: str,
        periodo_id: str,
        verificador: VerificadorAutorizacion,
    ) -> ConsecuenciaAutorizada:
        """
        Permite que NC construya una consecuencia únicamente cuando
        la Máquina demuestra que el asiento está ADMITIDO.

        El puente no modifica la máquina.
        """

        # ==============================================================
        # 1. La Máquina debe estar en ADMITIDO
        # ==============================================================

        if self.maquina.estado_actual != EstadoAsiento.ADMITIDO:
            raise ValueError(
                "F3B6F_VIOLACION: la máquina no está en ADMITIDO"
            )

        # ==============================================================
        # 2. Debe existir propuesta H₁ asociada a la máquina
        # ==============================================================

        if not self.maquina.propuesta_original_id:
            raise ValueError(
                "F3B6F_VIOLACION: falta propuesta_original_id en la máquina"
            )

        if not decision.propuesta_h1_id:
            raise ValueError(
                "F3B6F_VIOLACION: falta propuesta_h1_id en DecisionProfesional"
            )

        if self.maquina.propuesta_original_id != decision.propuesta_h1_id:
            raise ValueError(
                "F3B6F_VIOLACION: propuesta H₁ inconsistente con la máquina"
            )

        # ==============================================================
        # 3. Correlación H₂ ↔ llamada
        # ==============================================================

        if not correlation_id:
            raise ValueError(
                "F3B6F_VIOLACION: falta correlation_id"
            )

        if decision.correlation_id != correlation_id:
            raise ValueError(
                "F3B6F_VIOLACION: correlation_id inconsistente con H₂"
            )

        # ==============================================================
        # 4. La última transición debe ser EVALUADO → ADMITIDO
        #    y conservar la misma correlación.
        # ==============================================================

        historial = self.maquina.obtener_historial()

        if not historial:
            raise ValueError(
                "F3B6F_VIOLACION: máquina ADMITIDO sin historial"
            )

        ultima = historial[-1]

        if ultima["desde"] != EstadoAsiento.EVALUADO.name:
            raise ValueError(
                "F3B6F_VIOLACION: ADMITIDO no proviene de EVALUADO"
            )

        if ultima["hasta"] != EstadoAsiento.ADMITIDO.name:
            raise ValueError(
                "F3B6F_VIOLACION: última transición no termina en ADMITIDO"
            )

        if ultima["correlation_id"] != correlation_id:
            raise ValueError(
                "F3B6F_VIOLACION: correlación de máquina inconsistente"
            )

        # ==============================================================
        # 5. Delegación exclusiva a NC
        # ==============================================================

        return self.nc.construir_consecuencia_autorizada(
            decision=decision,
            consecuencia_candidata=consecuencia_candidata,
            evidencia_hash=evidencia_hash,
            correlation_id=correlation_id,
            contexto_contable=contexto_contable,
            fecha=fecha,
            periodo_id=periodo_id,
            estado_actual=EstadoAsiento.ADMITIDO.name,
        )
