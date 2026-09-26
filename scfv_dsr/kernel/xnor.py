"""
XNOR contable — fuente única del axioma de cargo/abono.

Tres representaciones equivalentes de la misma regla estructural:

    1. Booleana  : tabla cerrada de 4 combinaciones
    2. GF(2)     : 1 ⊕ n ⊕ m  (1 → DEBE, 0 → HABER)
    3. Signos    : χ(n) · χ(m)  (+1 → DEBE, −1 → HABER)

Codificación:
    DEUDORA   → 1 / +1
    ACREEDORA → 0 / −1
    AUMENTA   → 1 / +1
    DISMINUYE → 0 / −1

Ninguna de las tres reemplaza a las otras: son tres vistas del mismo
invariante. La coincidencia entre ellas se verifica por test.
"""

NATURALEZAS_VALIDAS = ("DEUDORA", "ACREEDORA")
MOVIMIENTOS_VALIDOS = ("AUMENTA", "DISMINUYE")

_TABLA = {
    ("DEUDORA",   "AUMENTA"):   "DEBE",
    ("DEUDORA",   "DISMINUYE"): "HABER",
    ("ACREEDORA", "AUMENTA"):   "HABER",
    ("ACREEDORA", "DISMINUYE"): "DEBE",
}

_N_A_GF2 = {"DEUDORA": 1, "ACREEDORA": 0}
_M_A_GF2 = {"AUMENTA": 1, "DISMINUYE": 0}

_N_A_SIGNO = {"DEUDORA": +1, "ACREEDORA": -1}
_M_A_SIGNO = {"AUMENTA": +1, "DISMINUYE": -1}


def _validar(naturaleza: str, movimiento: str) -> None:
    if naturaleza not in NATURALEZAS_VALIDAS:
        raise ValueError(
            f"XNOR inválido para naturaleza='{naturaleza}', "
            f"movimiento='{movimiento}'"
        )
    if movimiento not in MOVIMIENTOS_VALIDOS:
        raise ValueError(
            f"XNOR inválido para naturaleza='{naturaleza}', "
            f"movimiento='{movimiento}'"
        )


def ubicacion_booleana(naturaleza: str, movimiento: str) -> str:
    """Cara 1 — tabla cerrada de 4 combinaciones."""
    _validar(naturaleza, movimiento)
    return _TABLA[(naturaleza, movimiento)]


def ubicacion_gf2(naturaleza: str, movimiento: str) -> str:
    """Cara 2 — suma módulo 2. DEBE = 1 ⊕ n ⊕ m."""
    _validar(naturaleza, movimiento)
    bit = 1 ^ _N_A_GF2[naturaleza] ^ _M_A_GF2[movimiento]
    return "DEBE" if bit == 1 else "HABER"


def ubicacion_signos(naturaleza: str, movimiento: str) -> str:
    """Cara 3 — producto de caracteres. DEBE = (+1)·(+1) = +1."""
    _validar(naturaleza, movimiento)
    producto = _N_A_SIGNO[naturaleza] * _M_A_SIGNO[movimiento]
    return "DEBE" if producto == +1 else "HABER"


# Alias canónico: la cara booleana es la que se expone por defecto,
# pero las tres son la misma función desde el punto de vista del contrato.
calcular_ubicacion = ubicacion_booleana
