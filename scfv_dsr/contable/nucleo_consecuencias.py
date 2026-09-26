"""
SCFV v8.1+ — Núcleo de Consecuencias (F3B.5)
Autor: Domingo E. Díaz N. (C.P.C. Nº 183594)
Fecha: 2026-09-03

Propósito: Traducir la decisión profesional (H₂) y la consecuencia candidata
del fractal en una ConsecuenciaAutorizada, enriqueciendo trazabilidad
y contexto contable.

El NC:
- NO decide.
- NO ejecuta el asiento.
- NO persiste.
- NO genera consecuencias económicas.
- NO sustituye al fractal.
- NO sustituye al Motor Contable.
"""

import time
from typing import List, Dict, Any
from enum import Enum

from scfv_dsr.epistemologico.models import DecisionProfesional
from scfv_dsr.contable.modelos import ConsecuenciaAutorizada, ContextoContable


class NucleoConsecuencias:
    """
    Núcleo de Consecuencias.

    Materializa una consecuencia candidata previamente generada
    por el dominio/fractal cuando existe una decisión H₂ de ACEPTAR
    y el estado se encuentra en ADMITIDO.
    """

    def __init__(self, verificador):
        """
        El NC depende únicamente del verificador de autorización.

        No existe dependencia con MotorContable.
        """
        self.verificador = verificador

    # ------------------------------------------------------------------
    # XNOR
    # ------------------------------------------------------------------

    def _calcular_ubicacion_xnor(
        self,
        naturaleza: str,
        movimiento: str
    ) -> str:
        """Wrapper de la fuente única en scfv_dsr/kernel/xnor.py."""
        from scfv_dsr.kernel.xnor import ubicacion_booleana
        return ubicacion_booleana(naturaleza, movimiento)

    # ------------------------------------------------------------------
    # Tipo de decisión
    # ------------------------------------------------------------------

    def _es_aceptar(self, tipo_decision: Any) -> bool:
        """
        Acepta tanto TipoDecisionH2 como representación string.
        """

        if isinstance(tipo_decision, Enum):
            return tipo_decision.name == "ACEPTAR"

        if isinstance(tipo_decision, str):
            return tipo_decision.upper() == "ACEPTAR"

        return False

    # ------------------------------------------------------------------
    # Construcción de ConsecuenciaAutorizada
    # ------------------------------------------------------------------

    def construir_consecuencia_autorizada(
        self,
        decision: DecisionProfesional,
        consecuencia_candidata: List[Dict],
        evidencia_hash: str,
        correlation_id: str,
        contexto_contable: ContextoContable,
        fecha: str,
        periodo_id: str,
        estado_actual: str = "ADMITIDO"
    ) -> ConsecuenciaAutorizada:
        """
        Construye una ConsecuenciaAutorizada.

        Precondiciones:

        1. La decisión H₂ debe estar autorizada.
        2. El estado debe ser ADMITIDO.
        3. La decisión debe ser ACEPTAR.
        4. Debe existir al menos una consecuencia candidata.
        5. Cada partida debe contener cuenta, monto, naturaleza y movimiento.
        6. La fiscalidad debe estar respaldada por norma_id.
        7. Fecha y período deben venir del contexto productivo.

        El método no persiste ni genera el asiento.
        """

        # ==============================================================
        # 1. Verificar autorización H₂
        # ==============================================================

        if not self.verificador.esta_autorizado(
            propuesta_id=decision.propuesta_h1_id,
            decision_id=decision.decision_id,
            firma_h2=decision.firma_h2,
            correlation_id=correlation_id,
            estado_actual=estado_actual
        ):
            raise ValueError(
                "NC_VIOLACION: consecuencia no autorizada por H₂"
            )

        # ==============================================================
        # 2. Verificar estado
        # ==============================================================

        if estado_actual != "ADMITIDO":
            raise ValueError(
                "NC_VIOLACION: estado debe ser ADMITIDO"
            )

        # ==============================================================
        # 3. Verificar decisión
        # ==============================================================

        if not self._es_aceptar(decision.tipo_decision):
            raise ValueError(
                "NC_VIOLACION: decisión debe ser ACEPTAR"
            )

        # ==============================================================
        # 4. Verificar existencia de consecuencias
        # ==============================================================

        if not consecuencia_candidata:
            raise ValueError(
                "NC_VIOLACION: consecuencia candidata vacía"
            )

        # ==============================================================
        # 5. Normalizar y enriquecer partidas
        # ==============================================================

        partidas_enriquecidas = []

        for idx, partida in enumerate(consecuencia_candidata):

            if not isinstance(partida, dict):
                raise ValueError(
                    f"NC_VIOLACION: partida {idx} no es un diccionario"
                )

            p = dict(partida)

            # ----------------------------------------------------------
            # 5.1 Normalización cuenta → cuenta_codigo
            #
            # IMPORTANTE:
            # Esta operación ocurre ANTES de exigir cuenta_codigo.
            # ----------------------------------------------------------

            if "cuenta_codigo" not in p:

                if "cuenta" in p:
                    p["cuenta_codigo"] = p["cuenta"]
                    del p["cuenta"]

                else:
                    raise ValueError(
                        f"NC_VIOLACION: partida {idx} sin cuenta_codigo"
                    )

            # ----------------------------------------------------------
            # 5.2 Validar monto
            # ----------------------------------------------------------

            if "monto" not in p:
                raise ValueError(
                    f"NC_VIOLACION: partida {idx} sin monto"
                )

            try:
                monto = float(p["monto"])
            except (TypeError, ValueError):
                raise ValueError(
                    f"NC_VIOLACION: partida {idx} con monto inválido"
                )

            if monto <= 0:
                raise ValueError(
                    f"NC_VIOLACION: partida {idx} con monto inválido"
                )

            p["monto"] = monto

            # ----------------------------------------------------------
            # 5.3 Cuenta versión
            # ----------------------------------------------------------

            if "cuenta_version" not in p:
                p["cuenta_version"] = "1.0"

            # ----------------------------------------------------------
            # 5.4 Moneda
            # ----------------------------------------------------------

            if "moneda" not in p:
                p["moneda"] = "VES"

            # ----------------------------------------------------------
            # 5.5 Ubicación mediante XNOR
            # ----------------------------------------------------------

            if "ubicacion" not in p:

                naturaleza = p.get("naturaleza")
                movimiento = p.get("movimiento")

                if naturaleza and movimiento:

                    p["ubicacion"] = self._calcular_ubicacion_xnor(
                        naturaleza,
                        movimiento
                    )

                else:
                    raise ValueError(
                        f"NC_VIOLACION: partida {idx} "
                        "sin ubicacion y sin naturaleza/movimiento"
                    )

            # ----------------------------------------------------------
            # 5.6 Fiscalidad
            # ----------------------------------------------------------

            if p.get("es_fiscal", False):

                norma_id = p.get("norma_id")

                if not norma_id:
                    raise ValueError(
                        f"NC_VIOLACION: partida {idx} "
                        "fiscal sin norma_id"
                    )

            # ----------------------------------------------------------
            # 5.7 Conservar partida enriquecida
            # ----------------------------------------------------------

            partidas_enriquecidas.append(p)

        # ==============================================================
        # 6. Construir ConsecuenciaAutorizada
        # ==============================================================

        consecuencia = ConsecuenciaAutorizada(
            decision_id=decision.decision_id,
            propuesta_id=decision.propuesta_h1_id,
            firma_h2=decision.firma_h2,
            correlation_id=correlation_id,
            fecha=fecha,
            periodo_id=periodo_id,
            descripcion=(
                f"Consecuencia autorizada para "
                f"{decision.decision_id}"
            ),
            evidencia_hash=evidencia_hash,
            partidas=partidas_enriquecidas,
            timestamp=int(time.time()),
            contexto_contable=contexto_contable
        )

        return consecuencia
