"""Examinador de evidencia — Camino 3, capa integración.

Panel de consulta. No decide. No autoriza. No camino crítico.
Contrato: DOCS/H8P_EXAMINADOR_CONTRATO.md
"""
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field

from scfv_dsr.kernel import xnor
from scfv_dsr.contable.reticulo import RetículoCuentas


@dataclass
class Reporte:
    linea: dict = field(default_factory=dict)
    conjunto: dict = field(default_factory=dict)


def _nivel(ok: bool, hallazgos: list[str], detalles: dict | None = None) -> dict:
    return {"ok": ok, "hallazgos": hallazgos, "detalles": detalles or {}}


class ExaminadorEvidencia:
    def __init__(self, pcu: Mapping[str, Mapping]):
        self._pcu = dict(pcu)
        self._reticulo = RetículoCuentas.desde_pcu(pcu)

    def examinar(self, evidencia: Mapping) -> Reporte:
        if not isinstance(evidencia, Mapping):
            raise TypeError(
                f"examinar() espera Mapping, recibió {type(evidencia).__name__}"
            )
        partidas = evidencia.get("partidas", []) or []
        marco = evidencia.get("marco_contable", "NIIF_Completas")
        linea = self.nivel_linea(partidas)
        cuentas = [p.get("cuenta_codigo") for p in partidas if p.get("cuenta_codigo")]
        conjunto = self.nivel_conjunto(cuentas, marco=marco)
        return Reporte(linea=linea, conjunto=conjunto)

    def nivel_linea(self, partidas: list[dict]) -> dict:
        hallazgos: list[str] = []
        detalles: dict = {"n_partidas": len(partidas)}
        for i, p in enumerate(partidas):
            cc = p.get("cuenta_codigo")
            if not cc:
                hallazgos.append(f"partida[{i}]: partida_incompleta (sin cuenta_codigo)")
                continue
            if cc not in self._pcu:
                hallazgos.append(f"partida[{i}]: cuenta_ausente '{cc}'")
                continue
            naturaleza = self._pcu[cc].get("naturaleza")
            if naturaleza not in xnor.NATURALEZAS_VALIDAS:
                hallazgos.append(f"partida[{i}]: naturaleza_invalida '{naturaleza}' en cuenta '{cc}'")
                continue
            mov = p.get("movimiento")
            if mov not in xnor.MOVIMIENTOS_VALIDOS:
                hallazgos.append(f"partida[{i}]: movimiento_invalido '{mov}'")
                continue
            b = xnor.ubicacion_booleana(naturaleza, mov)
            g = xnor.ubicacion_gf2(naturaleza, mov)
            s = xnor.ubicacion_signos(naturaleza, mov)
            if not (b == g == s):
                hallazgos.append(f"partida[{i}]: XNOR_inconsistente b={b} g={g} s={s}")
                continue
            if "ubicacion" in p and p["ubicacion"] != b:
                hallazgos.append(f"partida[{i}]: ubicacion_declarada '{p['ubicacion']}' != '{b}'")
        return _nivel(ok=not hallazgos, hallazgos=hallazgos, detalles=detalles)

    def nivel_conjunto(self, cuentas: Iterable[str],
                       marco: str | None = None) -> dict:
        hallazgos: list[str] = []
        cuentas = list(cuentas)
        detalles: dict = {"n_cuentas": len(cuentas), "marco": marco}
        if marco is not None and marco not in self._reticulo.nombres():
            hallazgos.append(f"marco_ausente_en_pcu '{marco}'")
            return _nivel(ok=False, hallazgos=hallazgos, detalles=detalles)
        universo = self._reticulo.universo_set()
        C_marco = self._reticulo.subconjunto(marco) if marco is not None else universo
        for i, c in enumerate(cuentas):
            if c not in universo:
                hallazgos.append(f"cuenta[{i}]: '{c}' no en universo")
                continue
            if c not in C_marco:
                hallazgos.append(f"cuenta[{i}]: '{c}' no pertenece a marco '{marco}'")
        return _nivel(ok=not hallazgos, hallazgos=hallazgos, detalles=detalles)
