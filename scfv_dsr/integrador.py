"""
Integrador SCFV_DSR → pipeline S0.

Toma un fractal del DSR, lo evalúa, produce consecuencia candidata
y ejecuta el ciclo v8.2 completo hasta persistir ASIENTO_REGISTRADO.

Autoridad:
    - NO decide (H2 decide).
    - NO escribe directamente (Motor escribe vía EventStore).
    - Traduce formato DSR → formato orquestador.
"""

import sys
import os
import hashlib
import uuid
from pathlib import Path
from typing import Dict, List, Any, Optional

SCFV_DSR = str(Path(__file__).parent)

if SCFV_DSR not in sys.path:
    sys.path.insert(0, SCFV_DSR)

from scfv_dsr.dsl.parser import SCFVParser
import evaluador
from scfv_dsr.kernel import baldor
from scfv_dsr.kernel import xnor
from scfv_dsr.contable.event_store import EventStore
from scfv_dsr.profesional.orquestador import ejecutar_ciclo_v82
from scfv_dsr.contable.modelos import ContextoContable


def _importar_version_contexto():
    """VersionContexto puede vivir en varios sitios."""
    candidatos = [
        'scfv_dsr.epistemologico.models',
        'scfv_dsr.contable.estados',
        'scfv_dsr.profesional.h2',
    ]
    for mod in candidatos:
        try:
            m = __import__(mod, fromlist=['VersionContexto'])
            if hasattr(m, 'VersionContexto'):
                return m.VersionContexto
        except Exception:
            continue
    raise ImportError("VersionContexto no encontrado en el corpus")


def _construir_observacion(observacion_id, evidencia_id, correlation_id, evidencia: dict):
    from scfv_dsr.epistemologico.models import ObservacionH1, EntidadExtraida
    entidades = [EntidadExtraida(str(k), v, 1.0) for k, v in evidencia.items()]
    return ObservacionH1(
        observacion_id=observacion_id,
        evidencia_id=evidencia_id,
        entidades=entidades,
        confianza_global=0.95,
        timestamp=1756800000,
        correlation_id=correlation_id,
    )


def _construir_version_contexto(marco: str):
    V = _importar_version_contexto()
    return V(
        version_id="CTX-SCFV_DSR-1.0",
        fecha_inicio="2026-01-01",
        fecha_fin="2026-12-31",
        PCU_version="PCU-SCFV_DSR-1.0",
        reglas_version="REGLAS-SCFV_DSR-1.0",
        politica_inventario_version="INV-1.0",
        marco_contable_version=marco,
        politica_monetaria_version="PM-1.0",
    )


def _pcu_para_motor(kernel: dict, marcos: List[str]) -> Dict:
    pcu = {}
    for cuenta, info in kernel['cuentas'].items():
        pcu[cuenta] = {
            "nombre": info.get('nombre', ''),
            "naturaleza": info.get('naturaleza', 'DEUDORA'),
            "marcos": list(marcos),
        }
    return pcu


def _consecuencia_a_candidata(consecuencias: List[Dict]) -> List[Dict]:
    return [
        {
            "cuenta": c["cuenta"],
            "monto": float(c["monto"]),
            "naturaleza": c["naturaleza"],
            "movimiento": c["movimiento"],
        }
        for c in consecuencias
    ]


def ejecutar_fractal_en_pipeline(
    fractal_path: str,
    marco: str,
    evidencia: Dict,
    justificacion: str,
    db_path: Optional[str] = None,
    fecha: str = "2026-09-25",
    periodo_id: str = "2026-09",
    evidencia_hash: Optional[str] = None,
    observacion_id: Optional[str] = None,
    evidencia_id: Optional[str] = None,
    correlation_id: Optional[str] = None,
    catalogo_normas: Optional[Dict] = None,
) -> Dict[str, Any]:
    """
    Ciclo completo: DSR → H1 → H2 → DP → VA → PA → NC → PC → MC → ASENTADO → EventStore.
    """
    # 1 · Parsear fractal + cargar kernel
    parser = SCFVParser()
    fractal = parser.parse_file(fractal_path)
    kernel = evaluador.cargar_kernel()

    # 2 · Evaluar fractal
    consecuencias = evaluador.evaluar_fractal(
        fractal,
        {"marco_contable": marco, "evidencia": evidencia},
        kernel, baldor, xnor,
    )
    if not consecuencias:
        raise ValueError("DSR: sin consecuencias para esta evidencia/marco")

    # 3 · Transformar formato
    candidata = _consecuencia_a_candidata(consecuencias)

    # 4 · Preparar contexto S0
    if db_path is None:
        db_path = os.path.join(os.path.expanduser('~'), 'SCFV_DSR', 'var', 'scfv.db')
    store = EventStore(db_path)

    obs_id = observacion_id or f"OBS-{uuid.uuid4()}"
    ev_id = evidencia_id or f"EVID-{uuid.uuid4()}"
    corr_id = correlation_id or f"CORR-{uuid.uuid4()}"

    obs = _construir_observacion(obs_id, ev_id, corr_id,
                                  {**evidencia, "fecha": fecha})
    ctx_ver = _construir_version_contexto(marco)
    pcu = _pcu_para_motor(kernel, [marco])
    contexto_contable = ContextoContable(
        marco_contable=marco,
        PCU_version="PCU-SCFV_DSR-1.0",
        reglas_version="REGLAS-SCFV_DSR-1.0",
        politica_monetaria_version="PM-1.0",
    )

    if evidencia_hash is None:
        evidencia_hash = hashlib.sha256(str(evidencia).encode()).hexdigest()

    # 5 · Ejecutar pipeline S0
    resultado = ejecutar_ciclo_v82(
        observacion=obs,
        contexto_version=ctx_ver,
        store=store,
        pcu=pcu,
        catalogo_normas=catalogo_normas or {},
        consecuencia_candidata=candidata,
        contexto_contable=contexto_contable,
        fecha=fecha,
        periodo_id=periodo_id,
        evidencia_hash=evidencia_hash,
        justificacion=justificacion,
        inflacion_anual=0.0,
    )

    # 6 · Verificar persistencia
    verif = store.verificar_cadena()
    store.cerrar()

    return {
        "consecuencias_dsr": consecuencias,
        "candidata": candidata,
        "resultado_s0": resultado,
        "cadena_integra": verif,
    }
