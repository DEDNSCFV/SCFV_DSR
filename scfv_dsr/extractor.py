"""
Extractor: evento.payload.evidencia → Evidencia (Perceptum) → dict del fractal.

Tres funciones:
    · evidencia_desde_evento(evento)  → Evidencia (para Perceptum)
    · observacion_desde_evento(evento) → ObservacionH1 (usa Perceptum.extraer)
    · dict_desde_observacion(obs)      → dict compatible con fractales

Autoridad:
    - NO interpreta. Solo mapea.
    - NO decide. Solo transforma.
"""

import json
import sys
import uuid
from pathlib import Path


from scfv_dsr.epistemologico.evidencia import Evidencia
from scfv_dsr.epistemologico.perceptum import Perceptum


def evidencia_desde_evento(evento: dict) -> Evidencia:
    """Construye Evidencia desde evento.payload.evidencia."""
    payload = evento.get('payload') or json.loads(evento.get('payload', '{}'))
    ev = payload.get('evidencia', {}) if isinstance(payload, dict) else {}
    return Evidencia(
        evidencia_id=f"EVID-{uuid.uuid4()}",
        hash_evidencia=__import__("hashlib").sha256(json.dumps(ev, sort_keys=True).encode()).hexdigest(),
        tipo='json',
        origen='event_store',
        referencia=ev.get('factura'),
        contenido_original=json.dumps(ev, ensure_ascii=False),
        timestamp_adquisicion=int(evento.get('timestamp', 0) or 0),
        correlation_id=evento.get('correlation_id', f"CORR-{uuid.uuid4()}"),
        metadata={},
    )


def observacion_desde_evento(evento: dict):
    """Evidencia → Perceptum → ObservacionH1."""
    ev = evidencia_desde_evento(evento)
    return Perceptum.extraer(ev)


def dict_desde_observacion(observacion) -> dict:
    """
    Convierte ObservacionH1.entidades → dict compatible con fractales.
    Añade flags activadoras por tipo.
    """
    d = {e.campo: e.valor for e in observacion.entidades}

    # Flags + campos derivados
    tipo = str(d.get('tipo', '')).lower()
    d['activo_es_venta'] = (tipo == 'venta')
    d['activo_es_compra'] = (tipo in ('compra', 'compra_inventario'))
    d['activo_es_inventario'] = (tipo == 'compra_inventario')
    d['activo_es_ppe'] = (tipo == 'adquisicion_ppe')
    d['activo_es_intangible'] = (tipo == 'adquisicion_intangible')
    d['transaccion_moneda_extranjera'] = (d.get('moneda', 'VES') != 'VES')
    d['economia_hiperinflacionaria'] = d.get('economia_hiperinflacionaria', False)

    # Derivados numéricos
    try:
        cant = float(d.get('cantidad', 0) or 0)
        cu = float(d.get('costo_unitario', 0) or 0)
        if cant > 0 and cu > 0:
            d['costo'] = cant * cu
    except Exception:
        pass

    return d
