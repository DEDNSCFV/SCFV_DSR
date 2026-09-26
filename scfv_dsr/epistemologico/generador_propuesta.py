"""
SCFV v8.1+ — Generador de Propuesta H1 (F3A.1)
Autor: Domingo E. Díaz N. (C.P.C. Nº 183594)
Fecha: 2026-09-02

Propósito:
    Construir una PropuestaH1 a partir de una ObservacionH1,
    generando un HechoEconomico inferido y calculando métricas H₁.

No depende de Dictum ni H₂.
"""

import uuid
import hashlib
import time
from typing import Dict, Optional
from datetime import datetime

from scfv_dsr.epistemologico.models import (
    ObservacionH1,
    HechoEconomico,
    PropuestaH1,
    MetricasH1,
    EstadoPropuesta,
    EstadoEpistemico,
)


# Campos normativos para r
CAMPOS_NORMATIVOS = [
    "fecha",
    "monto",
    "moneda",
    "rif_emisor",
    "rif_receptor",
]

TOTAL_CAMPOS = len(CAMPOS_NORMATIVOS)


# Campos ontológicos para o
CAMPOS_ONTOLOGICOS = [
    "rif_emisor",
    "rif_receptor",
    "productos",
    "moneda",
]

TOTAL_CAMPOS_ONTOLOGICOS = len(CAMPOS_ONTOLOGICOS)


# Parámetros para t
LAMBDA_T = 0.001
TOP_CASOS = 10


# Parámetros para v
VOLATILIDAD_MAXIMA = 100.0


def _extraer_entidades_dict(
    observacion: ObservacionH1,
) -> Dict[str, object]:
    """Convierte la lista de entidades de una observación en un dict."""
    return {
        entidad.campo: entidad.valor
        for entidad in observacion.entidades
    }


def calcular_r(entidades: Dict[str, object]) -> float:
    """
    Calcula r = coherencia normativa.

    Cantidad de campos normativos presentes / total de campos normativos.
    """
    coincidencias = sum(
        1
        for campo in CAMPOS_NORMATIVOS
        if campo in entidades and entidades[campo] is not None
    )

    return coincidencias / TOTAL_CAMPOS


def calcular_o(entidades: Dict[str, object]) -> float:
    """
    Calcula o = consistencia ontológica.

    Cantidad de campos ontológicos presentes / total de campos ontológicos.
    """
    presentes = sum(
        1
        for campo in CAMPOS_ONTOLOGICOS
        if campo in entidades and entidades[campo] is not None
    )

    return presentes / TOTAL_CAMPOS_ONTOLOGICOS


def calcular_t() -> float:
    """
    Calcula t = peso temporal.

    Actualmente no existe repositorio de casos históricos,
    por lo que t permanece en 0.0.
    """
    return 0.0


def calcular_v(inflacion_anual: float = 0.0) -> float:
    """
    Calcula v = volatilidad contextual.

    v = 1 - min(inflacion_anual / VOLATILIDAD_MAXIMA, 1)
    """
    if inflacion_anual is None:
        return 0.0

    volatilidad = abs(inflacion_anual)

    v = 1.0 - min(
        volatilidad / VOLATILIDAD_MAXIMA,
        1.0,
    )

    return max(0.0, min(v, 1.0))


def generar_hecho_h1(
    observacion: ObservacionH1,
    inflacion_anual: Optional[float] = None,
) -> HechoEconomico:
    """
    Genera un HechoEconomico inferido a partir de una ObservacionH1.

    Responsabilidad:
        ObservacionH1 -> HechoEconomico

    El hecho conserva:
        - evidencia_id
        - correlation_id

    y queda en estado epistemológico INFERIDO.

    Las métricas H₁ se calculan aquí para mantener la semántica
    del generador F3A.1, aunque el modelo HechoEconomico actual
    no las almacena.
    """
    entidades_dict = _extraer_entidades_dict(observacion)

    r = calcular_r(entidades_dict)
    s = 0.0
    o = calcular_o(entidades_dict)
    t = calcular_t()
    v = (
        calcular_v(inflacion_anual)
        if inflacion_anual is not None
        else 0.0
    )

    hecho_id = str(uuid.uuid4())

    timestamp = (
        observacion.timestamp
        or int(time.time())
    )

    fecha_str = datetime.fromtimestamp(
        timestamp
    ).strftime("%Y-%m-%d")

    idempotency_key = hashlib.sha256(
        (
            hecho_id
            + observacion.correlation_id
            + str(timestamp)
        ).encode()
    ).hexdigest()

    hecho = HechoEconomico(
        hecho_id=hecho_id,
        descripcion="Hecho inferido desde observación",
        entidades=entidades_dict,
        temporalidad=fecha_str,
        magnitud=0.0,
        evidencia_ids=[
            observacion.evidencia_id
        ],
        estado=EstadoEpistemico.INFERIDO,
        origen="PERCEPTUM",
        correlation_id=observacion.correlation_id,
        idempotency_key=idempotency_key,
    )

    return hecho


def _generar_propuesta_desde_hecho(
    hecho: HechoEconomico,
    observacion: ObservacionH1,
    inflacion_anual: Optional[float] = None,
) -> PropuestaH1:
    """
    Construye una PropuestaH1 a partir de un HechoEconomico existente.

    Responsabilidad:
        HechoEconomico + ObservacionH1 -> PropuestaH1

    Esta función NO genera un nuevo HechoEconomico.

    Conserva la identidad del hecho recibido.
    """
    if not isinstance(hecho, HechoEconomico):
        raise TypeError(
            "GENERADOR_H1: se requiere una instancia de HechoEconomico"
        )

    if not isinstance(observacion, ObservacionH1):
        raise TypeError(
            "GENERADOR_H1: se requiere una instancia de ObservacionH1"
        )

    entidades_dict = _extraer_entidades_dict(
        observacion
    )

    r = calcular_r(entidades_dict)
    s = 0.0
    o = calcular_o(entidades_dict)
    t = calcular_t()
    v = (
        calcular_v(inflacion_anual)
        if inflacion_anual is not None
        else 0.0
    )

    metricas = MetricasH1(
        r=r,
        s=s,
        o=o,
        t=t,
        v=v,
    )

    soporte_C = (
        0.30 * r
        + 0.25 * s
        + 0.20 * o
        + 0.15 * t
        + 0.10 * v
    )

    propuesta_id = str(uuid.uuid4())

    timestamp = (
        observacion.timestamp
        or int(time.time())
    )

    idempotency_key = hashlib.sha256(
        (
            propuesta_id
            + observacion.correlation_id
            + str(timestamp)
        ).encode()
    ).hexdigest()

    propuesta = PropuestaH1(
        propuesta_id=propuesta_id,
        hecho_id=hecho.hecho_id,
        observacion_id=observacion.observacion_id,
        metricas=metricas,
        soporte_C=soporte_C,
        proposicion="Propuesta generada automáticamente por H₁",
        propuesta_padre_id=None,
        version_propuesta=1,
        estado_operacional=EstadoPropuesta.PROPUESTO,
        timestamp=timestamp,
        correlation_id=observacion.correlation_id,
        estado_epistemico=EstadoEpistemico.INFERIDO,
        idempotency_key=idempotency_key,
    )

    return propuesta


def generar_propuesta_h1(
    observacion: ObservacionH1,
    inflacion_anual: Optional[float] = None,
) -> PropuestaH1:
    """
    API pública conservada:

        ObservacionH1 -> PropuestaH1

    Flujo interno:

        ObservacionH1
            -> HechoEconomico
            -> PropuestaH1

    El mismo HechoEconomico generado internamente es utilizado
    por la PropuestaH1.
    """
    hecho = generar_hecho_h1(
        observacion,
        inflacion_anual,
    )

    return _generar_propuesta_desde_hecho(
        hecho,
        observacion,
        inflacion_anual,
    )
