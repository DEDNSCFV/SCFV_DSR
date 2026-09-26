"""
SCFV v8.1 - Motor Contable con I2, I13 e I6 enriquecidas
"""
import sqlite3
import hashlib
import json
import uuid
from scfv_dsr.kernel.xnor import (
    ubicacion_booleana,
    ubicacion_gf2,
    ubicacion_signos,
)
from typing import Dict, List, Any, Optional

from scfv_dsr.contable.modelos import ConsecuenciaAutorizada, ContextoContable
from scfv_dsr.contable.verificador_autorizacion import VerificadorAutorizacion


class MotorContable:
    def __init__(self, db_connection, pcu: Dict, moneda_funcional: str = "VES", verificador: Optional[VerificadorAutorizacion] = None):
        self.db = db_connection
        self.pcu = pcu
        self.moneda_funcional = moneda_funcional
        self.verificador = verificador

    # --------------------------------------------------------------------
    # I2: Cuenta existe y es compatible con el marco contable
    # --------------------------------------------------------------------
    def _verificar_cuenta_con_marco(self, cuenta: str, marco_contable: str) -> bool:
        if cuenta not in self.pcu:
            return False
        marcos_permitidos = self.pcu[cuenta].get("marcos", ["NIIF_Completas"])
        if marco_contable not in marcos_permitidos:
            return False
        return True

    def validar_partida(self, partida: Dict, marco_contable: str = "NIIF_Completas") -> bool:
        # I2: cuenta existe y es compatible
        cuenta = partida.get("cuenta")
        if not cuenta:
            raise ValueError("I2_VIOLATION: Partida sin cuenta")
        if not self._verificar_cuenta_con_marco(cuenta, marco_contable):
            raise ValueError(f"I2_VIOLATION: Cuenta {cuenta} no existe o no es compatible con el marco {marco_contable}")

        # I13: moneda definida y soportada
        self._validar_moneda(partida)

        # I6: se validará externamente (en el integrador) porque necesita el catálogo de normas
        return True

    # --------------------------------------------------------------------
    # I13: Moneda definida y soportada por el perfil
    # --------------------------------------------------------------------
    def _validar_moneda(self, partida: Dict) -> bool:
        """Valida que la moneda esté definida y sea la funcional (I13)."""
        moneda = partida.get("moneda", "VES")
        if moneda != self.moneda_funcional:
            raise ValueError(f"I13_VIOLATION: Moneda '{moneda}' no permitida. Solo '{self.moneda_funcional}'")
        return True

    # --------------------------------------------------------------------
    # I1: Partida doble
    # --------------------------------------------------------------------
    def validar_partida_doble(self, partidas: List[Dict]) -> bool:
        total_debe = sum(p.get("monto", 0) for p in partidas if p.get("ubicacion") == "DEBE")
        total_haber = sum(p.get("monto", 0) for p in partidas if p.get("ubicacion") == "HABER")
        if total_debe <= 0 or total_haber <= 0:
            raise ValueError(f"I1_VIOLACION: debe={total_debe}, haber={total_haber} (valores deben ser > 0)")
        if abs(total_debe - total_haber) > 0.001:
            raise ValueError(f"I1_VIOLACION: debe={total_debe}, haber={total_haber}")
        return True

    # --------------------------------------------------------------------
    # I6: Regla fiscal identificada (se llama externamente)
    # --------------------------------------------------------------------
    def validar_I6(self, partidas: List[Dict], normas_catalogo: List[Dict]) -> bool:
        normas_ids = {n.get('id') for n in normas_catalogo if n.get('id')}
        for p in partidas:
            if p.get('es_fiscal') and not p.get('norma_id'):
                raise ValueError(f"I6_VIOLATION: Partida fiscal sin norma_id: {p}")
            if p.get('norma_id') and p.get('norma_id') not in normas_ids:
                raise ValueError(f"I6_VIOLATION: norma_id {p.get('norma_id')} no existe en el catálogo")
        return True

    # --------------------------------------------------------------------
    # F3B.3-D — Motor v8.2: generar_asiento con barrera de autorización
    # --------------------------------------------------------------------

    def _calcular_ubicacion_xnor(self, naturaleza: str, movimiento: str) -> str:
        """Wrapper de la fuente única en scfv_dsr/kernel/xnor.py."""
        return ubicacion_booleana(naturaleza, movimiento)
    def generar_asiento(
        self,
        consecuencia: ConsecuenciaAutorizada,
        verificador: VerificadorAutorizacion,
        estado_actual: str,
        catalogo_normas: Optional[List[Dict]] = None
    ) -> Dict:
        """
        Genera un asiento contable técnico a partir de una consecuencia autorizada.
        """
        # 1. Barrera de autorización
        if verificador is None:
            raise ValueError("MOTOR_VIOLACION: Motor sin verificador de autorización")

        if not verificador.esta_autorizado(
            propuesta_id=consecuencia.propuesta_id,
            decision_id=consecuencia.decision_id,
            firma_h2=consecuencia.firma_h2,
            correlation_id=consecuencia.correlation_id,
            estado_actual=estado_actual
        ):
            raise ValueError("MOTOR_VIOLACION: consecuencia no autorizada")

        # 2. Validación estructural
        if not consecuencia.decision_id or not consecuencia.propuesta_id or not consecuencia.firma_h2 or not consecuencia.correlation_id:
            raise ValueError("MOTOR_VIOLACION: identificadores ausentes en consecuencia")
        if not consecuencia.contexto_contable:
            raise ValueError("MOTOR_VIOLACION: contexto_contable ausente")
        if len(consecuencia.partidas) < 2:
            raise ValueError("MOTOR_VIOLACION: se requieren al menos 2 partidas")

        # 3. I6: Verificar catálogo si hay partidas fiscales
        if any(p.get("es_fiscal", False) for p in consecuencia.partidas):
            if catalogo_normas is None:
                raise ValueError("MOTOR_VIOLACION: I6_VIOLATION - partidas fiscales requieren catálogo normativo")

        # 4. Validaciones por partida
        normas_ids = {n.get('id') for n in (catalogo_normas or []) if n.get('id')}
        marco_contable = consecuencia.contexto_contable.marco_contable

        for idx, p in enumerate(consecuencia.partidas):
            # Validación estructural de partida
            if "cuenta_codigo" not in p or "cuenta_version" not in p:
                raise ValueError(f"MOTOR_VIOLACION: partida {idx} sin cuenta_codigo o cuenta_version")
            if not p["cuenta_version"]:
                raise ValueError(f"MOTOR_VIOLACION: partida {idx} con cuenta_version vacía")
            if "ubicacion" not in p or p["ubicacion"] not in ("DEBE", "HABER"):
                raise ValueError(f"MOTOR_VIOLACION: partida {idx} sin ubicacion válida")
            if "movimiento" not in p or p["movimiento"] not in ("AUMENTA", "DISMINUYE"):
                raise ValueError(f"MOTOR_VIOLACION: partida {idx} sin movimiento válido")
            if "monto" not in p:
                raise ValueError(f"MOTOR_VIOLACION: partida {idx} sin monto")
            if not isinstance(p["monto"], (int, float)):
                raise ValueError(f"MOTOR_VIOLACION: partida {idx} con monto no numérico")
            if p["monto"] < 0:
                raise ValueError(f"MOTOR_VIOLACION: partida {idx} con monto inválido (debe ser > 0)")

            # I2: cuenta existe y compatible con marco
            cuenta_codigo = p["cuenta_codigo"]
            if cuenta_codigo not in self.pcu:
                raise ValueError(f"MOTOR_VIOLACION: I2_VIOLATION - cuenta '{cuenta_codigo}' no existe en PCU")
            marcos_permitidos = self.pcu[cuenta_codigo].get("marcos", ["NIIF_Completas"])
            if marco_contable not in marcos_permitidos:
                raise ValueError(f"MOTOR_VIOLACION: I2_VIOLATION - cuenta '{cuenta_codigo}' no compatible con marco '{marco_contable}'")

            # I13: moneda
            moneda = p.get("moneda", "VES")
            if moneda != self.moneda_funcional:
                raise ValueError(f"MOTOR_VIOLACION: I13_VIOLATION - moneda '{moneda}' no permitida. Solo '{self.moneda_funcional}'")

            # I6: partidas fiscales
            if p.get("es_fiscal", False):
                if not p.get("norma_id"):
                    raise ValueError(f"MOTOR_VIOLACION: I6_VIOLATION - partida fiscal sin norma_id")
                if p["norma_id"] not in normas_ids:
                    raise ValueError(f"MOTOR_VIOLACION: I6_VIOLATION - norma_id '{p['norma_id']}' no existe en el catálogo")

        # 5. XNOR: calcular y verificar ubicacion
        for idx, p in enumerate(consecuencia.partidas):
            naturaleza = self.pcu[p["cuenta_codigo"]]["naturaleza"]
            movimiento = p["movimiento"]

            # Tres caras del XNOR — verificación mutua
            b = ubicacion_booleana(naturaleza, movimiento)
            g = ubicacion_gf2(naturaleza, movimiento)
            sig = ubicacion_signos(naturaleza, movimiento)

            if not (b == g == sig):
                raise ValueError(
                    f"MOTOR_VIOLACION: XNOR_INCONSISTENTE partida {idx} - "
                    f"booleana={b}, gf2={g}, signos={sig} "
                    f"(naturaleza='{naturaleza}', movimiento='{movimiento}')"
                )

            if p["ubicacion"] != b:
                raise ValueError(
                    f"MOTOR_VIOLACION: XNOR contradictorio en partida {idx} - "
                    f"recibida {p['ubicacion']}, calculada {b} "
                    f"(naturaleza='{naturaleza}', movimiento='{movimiento}')"
                )

        # 6. I1 endurecida
        total_debe = sum(p["monto"] for p in consecuencia.partidas if p["ubicacion"] == "DEBE")
        total_haber = sum(p["monto"] for p in consecuencia.partidas if p["ubicacion"] == "HABER")
        if total_debe <= 0 or total_haber <= 0:
            raise ValueError(f"MOTOR_VIOLACION: I1_VIOLACION - DEBE={total_debe}, HABER={total_haber} (valores deben ser > 0)")
        if abs(total_debe - total_haber) > 0.001:
            raise ValueError(f"MOTOR_VIOLACION: I1_VIOLACION - DEBE={total_debe}, HABER={total_haber}")

        # 7. Construir asiento técnico (no persistido)
        asiento = {
            "id": str(uuid.uuid4()),
            "fecha": consecuencia.fecha,
            "periodo_id": consecuencia.periodo_id,
            "descripcion": consecuencia.descripcion,
            "partidas": consecuencia.partidas,
            "total_debe": total_debe,
            "total_haber": total_haber,
            "evidencia_hash": consecuencia.evidencia_hash,
            "decision_id": consecuencia.decision_id,
            "propuesta_id": consecuencia.propuesta_id,
            "firma_h2": consecuencia.firma_h2,
            "correlation_id": consecuencia.correlation_id,
            "timestamp": consecuencia.timestamp,
            "version_motor": "8.2",
            "contexto_contable": {
                "marco_contable": consecuencia.contexto_contable.marco_contable,
                "PCU_version": consecuencia.contexto_contable.PCU_version,
                "reglas_version": consecuencia.contexto_contable.reglas_version,
                "politica_monetaria_version": consecuencia.contexto_contable.politica_monetaria_version
            }
        }
        return asiento
