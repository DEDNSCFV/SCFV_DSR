"""Evaluador de reglas de fractales. Activa por marco. No decide (H2)."""

import json
import re
from pathlib import Path


def cargar_kernel(ruta_kernel=None):
    if ruta_kernel is None:
        ruta_kernel = str(Path(__file__).parent / "kernel")
    base = Path(ruta_kernel)
    return {
        "operaciones": json.load(open(base / "operaciones.json"))["operaciones"],
        "cuentas":     json.load(open(base / "cuentas.json"))["cuentas"],
        "categorias":  json.load(open(base / "categorias.json"))["categorias"],
        "puente":      json.load(open(base / "puente.json"))["puente"],
    }


def _parsear_comparacion(expr):
    m = re.match(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*(==|!=|>=|<=|>|<)\s*(.+?)\s*$', expr)
    return (m.group(1), m.group(2), m.group(3)) if m else None


def _resolver_valor(tok, evidencia, marco):
    tok = tok.strip()
    if tok.startswith('"') and tok.endswith('"'):
        return tok[1:-1]
    if tok == "marco":
        return marco
    if tok in evidencia:
        return evidencia[tok]
    try:
        return float(tok)
    except ValueError:
        return tok


def _eval_expr(expr, evidencia, marco):
    parsed = _parsear_comparacion(expr)
    if not parsed:
        nombre = expr.strip()
        if nombre == "marco":
            return bool(marco)
        return bool(evidencia.get(nombre, False))
    campo, op, val = parsed
    i = _resolver_valor(campo, evidencia, marco)
    d = _resolver_valor(val, evidencia, marco)
    return {
        "==": i == d, "!=": i != d,
        ">": i > d, "<": i < d,
        ">=": i >= d, "<=": i <= d,
    }[op]


def evaluar_condicion(condicion, evidencia, marco):
    partes = re.split(r'\s+(Y|O)\s+', condicion)
    resultado = _eval_expr(partes[0], evidencia, marco)
    i = 1
    while i < len(partes):
        op = partes[i]
        val = _eval_expr(partes[i + 1], evidencia, marco)
        resultado = (resultado and val) if op == "Y" else (resultado or val)
        i += 2
    return resultado


def parsear_accion(accion_str):
    m = re.search(r'GENERAR\s+CONSECUENCIA\s*\((.*)\)', accion_str)
    if not m:
        return {}
    cuerpo = m.group(1)
    return {
        p[0]: (p[1] if p[1] else p[2])
        for p in re.findall(
            r'([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?:"([^"]*)"|([A-Za-z0-9_.\-]+))',
            cuerpo
        )
    }


def evaluar_operacion(op_id, ev, kernel, baldor):
    op = kernel["operaciones"].get(op_id)
    if not op:
        return 0.0
    # Operaciones compuestas con manejo directo (antes del fallback baldor)
    if op_id == "suma_montos":
        if "montos" in ev and isinstance(ev["montos"], list):
            return sum(float(x) for x in ev["montos"])
        return float(ev.get("monto", 0))
    if op_id == "menor_costo_vnr":        return min(ev.get("costo", 0), ev.get("valor_neto_realizable", 0))
    if op_id == "menor_costo_precio_venta": return min(ev.get("costo", 0), ev.get("precio_venta", 0) - ev.get("costos_terminacion_venta", 0))
    if op_id == "valor_neto_realizable":  return ev.get("precio_venta", 0) - ev.get("costos_realizacion", 0)
    if op_id == "depreciacion_lineal":
        v = ev.get("vida_util", 1) or 1
        return (ev.get("costo", 0) - ev.get("valor_residual", 0)) / v
    if op_id == "amortizacion_lineal":
        v = ev.get("vida_util", 1) or 1
        return ev.get("costo", 0) / v
    if op_id == "plusvalia":
        return ev.get("contraprestacion_transferida", 0) - ev.get("activos_netos_identificables", 0)
    if op_id == "subvencion_sistematica":
        p = ev.get("periodos", 1) or 1
        monto = ev.get("monto", ev.get("monto_subvencion", 0))
        return monto / p
    if op_id == "valor_presente_anualidad":
        pago, r, n = ev.get("pago", 0), ev.get("r", 0), ev.get("n", 0)
        return pago * n if r == 0 else pago * (1 - (1 + r) ** (-n)) / r
    if op_id == "valor_esperado":
        return sum(p * m for p, m in ev.get("desglose", []))
    if op_id == "valor_presente":
        return ev.get("C", 0) / ((1 + ev.get("r", 0)) ** ev.get("t", 0))
    if op_id == "conversion_moneda":
        return ev.get("monto", 0) * ev.get("tipo_cambio", 1)
    if op_id == "reexpresion_inflacion":
        o = ev.get("indice_origen", 1)
        return ev.get("monto_historico", 0) * (ev.get("indice_cierre", 1) / o) if o else 0
    if op_id == "suma_montos":
        if "montos" in ev and isinstance(ev["montos"], list):
            return sum(float(x) for x in ev["montos"])
        return float(ev.get("monto", 0))
    return 0.0


def evaluar_fractal(fractal, contexto, kernel, baldor, xnor):
    marco = contexto["marco_contable"]
    evidencia = contexto["evidencia"]
    out = []
    for nombre, reglas in fractal["fractales"].items():
        for regla in reglas:
            if not evaluar_condicion(regla["condition"], evidencia, marco):
                continue
            for acc in regla["actions"]:
                p = parsear_accion(acc)
                cuenta = p.get("cuenta")
                if not cuenta:
                    cat = kernel["puente"].get(p.get("categoria"), {})
                    cuentas = cat.get("cuentas", [])
                    if not cuentas:
                        continue
                    cuenta = cuentas[0]
                meta = kernel["cuentas"].get(cuenta, {})
                nat = meta.get("naturaleza", "DEUDORA")
                mov = p.get("movimiento", "AUMENTA")
                out.append({
                    "fractal": nombre,
                    "regla": regla["name"],
                    "marco": marco,
                    "fuente": p.get("fuente"),
                    "cuenta": cuenta,
                    "nombre_cuenta": meta.get("nombre"),
                    "naturaleza": nat,
                    "movimiento": mov,
                    "ubicacion": xnor.ubicacion_booleana(nat, mov),
                    "monto": evaluar_operacion(p.get("operacion"), evidencia, kernel, baldor),
                })
    return out
