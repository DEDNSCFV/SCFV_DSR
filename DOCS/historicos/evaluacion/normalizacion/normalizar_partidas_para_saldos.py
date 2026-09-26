"""
Soporte mínimo U-SEQ-01 · normalización
Convierte partidas de un asiento a saldos por cuenta con signo algebraico.

Convención: saldo positivo = deudor, saldo negativo = acreedor.
Un asiento cuadrado produce suma algebraica = 0.

Acto 11 · soporte mínimo · pre-registro vE vigente.
"""
NATURALEZAS_VALIDAS = {"DEUDORA", "ACREEDORA"}
MOVIMIENTOS_VALIDOS = {"AUMENTA", "DISMINUYE"}


def _delta(naturaleza, movimiento, monto):
    if naturaleza not in NATURALEZAS_VALIDAS:
        raise ValueError(f"Naturaleza desconocida: {naturaleza!r}")
    if movimiento not in MOVIMIENTOS_VALIDOS:
        raise ValueError(f"Movimiento desconocido: {movimiento!r}")

    if naturaleza == "DEUDORA":
        return +monto if movimiento == "AUMENTA" else -monto
    else:  # ACREEDORA
        return -monto if movimiento == "AUMENTA" else +monto


def normalizar_partidas_para_saldos(evento):
    """
    Recibe un evento (dict) tal como lo devuelve leer_eventos_asiento.
    Devuelve {cuenta: saldo} con signo algebraico.

    Si el asiento está cuadrado, sum(saldos.values()) ≈ 0.
    """
    payload = evento.get("payload", {})
    partidas = payload.get("partidas", [])
    if not partidas:
        return {}

    saldos = {}
    for p in partidas:
        cuenta = p.get("cuenta")
        if not cuenta:
            raise ValueError(f"Partida sin cuenta: {p!r}")
        monto = float(p.get("monto", 0.0))
        delta = _delta(p.get("naturaleza"), p.get("movimiento"), monto)
        saldos[cuenta] = saldos.get(cuenta, 0.0) + delta
    return saldos


if __name__ == "__main__":
    import json
    import sys
    evento = json.load(sys.stdin)
    saldos = normalizar_partidas_para_saldos(evento)
    print(json.dumps(saldos, ensure_ascii=False, indent=2))
    print(f"suma algebraica: {sum(saldos.values())}")
