"""
Tests del soporte mínimo U-SEQ-01.
Ejecutable con: python3 test_soporte_minimo.py
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]  # evaluacion/
sys.path.insert(0, str(RAIZ / "lectura"))
sys.path.insert(0, str(RAIZ / "normalizacion"))

from leer_eventos_asiento import leer_eventos_asiento
from normalizar_partidas_para_saldos import normalizar_partidas_para_saldos


DB = str(Path.home() / "scfv_v6" / "scfv.db")


def test_lee_10_eventos():
    eventos = leer_eventos_asiento(DB)
    assert len(eventos) == 10, f"esperado 10, obtenido {len(eventos)}"
    print("OK  lee 10 eventos")


def test_evento_1_tiene_2_partidas():
    eventos = leer_eventos_asiento(DB)
    e1 = [e for e in eventos if e["id"] == 1][0]
    n = len(e1["payload"].get("partidas", []))
    assert n == 2, f"esperado 2 partidas, obtenido {n}"
    print("OK  evento id=1 tiene 2 partidas")


def test_saldos_evento_1():
    eventos = leer_eventos_asiento(DB)
    e1 = [e for e in eventos if e["id"] == 1][0]
    saldos = normalizar_partidas_para_saldos(e1)
    assert saldos.get("110101") == 1000.0, f"110101: {saldos.get('110101')}"
    assert saldos.get("410101") == -1000.0, f"410101: {saldos.get('410101')}"
    print(f"OK  saldos id=1: {saldos}")


def test_partida_doble():
    eventos = leer_eventos_asiento(DB)
    for e in eventos:
        saldos = normalizar_partidas_para_saldos(e)
        s = sum(saldos.values())
        assert abs(s) < 1e-9, f"evento {e['id']}: suma={s}"
    print(f"OK  partida doble en los {len(eventos)} eventos")


def test_rechaza_naturaleza_desconocida():
    try:
        normalizar_partidas_para_saldos({
            "payload": {"partidas": [
                {"cuenta": "X", "naturaleza": "MIXTA",
                 "movimiento": "AUMENTA", "monto": 1.0}
            ]}
        })
    except ValueError:
        print("OK  rechaza naturaleza desconocida")
        return
    raise AssertionError("no rechazó naturaleza desconocida")


def test_rechaza_movimiento_desconocido():
    try:
        normalizar_partidas_para_saldos({
            "payload": {"partidas": [
                {"cuenta": "X", "naturaleza": "DEUDORA",
                 "movimiento": "FLOTA", "monto": 1.0}
            ]}
        })
    except ValueError:
        print("OK  rechaza movimiento desconocido")
        return
    raise AssertionError("no rechazó movimiento desconocido")


def test_detecta_descuadre():
    """Un asiento descuadrado NO debe dar suma 0 — el detector debe verlo."""
    saldos = normalizar_partidas_para_saldos({
        "payload": {"partidas": [
            {"cuenta": "110101", "naturaleza": "DEUDORA",
             "movimiento": "AUMENTA", "monto": 1000.0},
            {"cuenta": "410101", "naturaleza": "ACREEDORA",
             "movimiento": "AUMENTA", "monto": 900.0},
        ]}
    })
    s = sum(saldos.values())
    assert abs(s - 100.0) < 1e-9, f"esperado 100, obtenido {s}"
    print(f"OK  descuadre detectado: {s}")


if __name__ == "__main__":
    test_lee_10_eventos()
    test_evento_1_tiene_2_partidas()
    test_saldos_evento_1()
    test_partida_doble()
    test_rechaza_naturaleza_desconocida()
    test_rechaza_movimiento_desconocido()
    test_detecta_descuadre()
    print()
    print("=== 7/7 PASSED ===")
