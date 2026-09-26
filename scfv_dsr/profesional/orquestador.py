"""
SCFV v8.2 — Orquestador del ciclo contable (modo supervisado).

Encadena: H1 → H2 → DP → VA → PA → NC → PC → MC → ASENTADO → EventStore.

H2 opera en modo supervisado: requiere justificación profesional explícita.
"""

import hashlib
from typing import Any, Dict, List

from scfv_dsr.epistemologico.generador_propuesta import generar_propuesta_h1
from scfv_dsr.profesional.h2 import H2Decision
from scfv_dsr.contable.decision_provider import DecisionProvider
from scfv_dsr.contable.verificador_autorizacion import VerificadorAutorizacion
from scfv_dsr.contable.puente_autorizacion import PuenteAutorizacion
from scfv_dsr.contable.puente_consecuencias import PuenteConsecuencias
from scfv_dsr.contable.nucleo_consecuencias import NucleoConsecuencias
from scfv_dsr.contable.motor import MotorContable
from scfv_dsr.contable.maquina_estados_asiento import MaquinaEstadosAsiento
from scfv_dsr.contable.estados import EstadoAsiento


def ejecutar_ciclo_v82(
    observacion,
    contexto_version,
    store,
    pcu: Dict[str, Any],
    catalogo_normas: Dict[str, Any],
    consecuencia_candidata: List[Dict[str, Any]],
    contexto_contable,
    fecha: str,
    periodo_id: str,
    evidencia_hash: str,
    justificacion: str = None,
    decision_externa=None,
    inflacion_anual: float = 0.0,
) -> Dict[str, Any]:
    """Ejecuta el ciclo contable v8.2 en modo supervisado."""

    # 1-2. H1 + H2, o reutilizar decision_externa
    propuesta = None
    if decision_externa is not None:
        decision = decision_externa
        propuesta_id = decision.propuesta_h1_id
    else:
        propuesta = generar_propuesta_h1(observacion, inflacion_anual)
        h2 = H2Decision()
        resultado_h2 = h2.decidir(
            propuesta, [], contexto_version, store,
            modo_auto=False,
            justificacion=justificacion,
        )
        propuesta_id = propuesta.propuesta_id

    # 3. DP
    provider = DecisionProvider(store)
    if decision_externa is None:
        decision = provider.obtener_decision(
            resultado_h2["decision"].decision_id
        )

    # 4. Máquina de estados + Verificador
    maquina = MaquinaEstadosAsiento(EstadoAsiento.EVALUADO)
    maquina.propuesta_original_id = propuesta_id
    verificador = VerificadorAutorizacion(provider)

    # 5. PA — Transición EVALUADO → ADMITIDO
    puente_auth = PuenteAutorizacion(maquina)
    puente_auth.autorizar_admitido(
        decision=decision,
        correlation_id=decision.correlation_id,
        version_contexto={"version_id": contexto_version.version_id},
        verificador=verificador,
    )

    # 6. NC + PC — Construcción de consecuencia autorizada
    nc = NucleoConsecuencias(verificador)
    puente_cons = PuenteConsecuencias(maquina, nc)
    consecuencia = puente_cons.construir_consecuencia_autorizada(
        decision=decision,
        consecuencia_candidata=consecuencia_candidata,
        evidencia_hash=evidencia_hash,
        correlation_id=decision.correlation_id,
        contexto_contable=contexto_contable,
        fecha=fecha,
        periodo_id=periodo_id,
        verificador=verificador,
    )

    # 7. MC — Generación de asiento
    motor = MotorContable(None, pcu, moneda_funcional="VES")
    asiento = motor.generar_asiento(
        consecuencia,
        verificador,
        "ADMITIDO",
        catalogo_normas,
    )

    # 8. Cerrar ciclo de estados: ADMITIDO → ASENTADO
    maquina.transicionar(
        nuevo_estado=EstadoAsiento.ASENTADO,
        autor=decision.autor,
        correlation_id=decision.correlation_id,
        version_contexto={"version_id": contexto_version.version_id},
        justificacion=decision.justificacion,
        metadata={"asiento_id": asiento["id"]},
    )

    # 9. Persistir el evento terminal
    idempotency_key = hashlib.sha256(
        (asiento["id"] + decision.correlation_id).encode()
    ).hexdigest()
    store.guardar(
        "ASIENTO_REGISTRADO",
        asiento,
        decision.correlation_id,
        idempotency_key,
        version_contexto={"version_id": contexto_version.version_id},
    )

    return {
        "propuesta": propuesta,
        "decision": decision,
        "consecuencia": consecuencia,
        "asiento": asiento,
        "maquina": maquina,
    }
