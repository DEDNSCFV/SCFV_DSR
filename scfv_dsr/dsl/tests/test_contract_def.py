import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scfv_dsr.dsl.parser import SCFVParser

def test_contract_minimo():
    p = SCFVParser()
    texto = "CONTRATO VENTA OBJETO: O INVARIANTE: I ELEMENTO: E"
    r = p.parse_string(texto)
    assert "VENTA" in r["contratos"]

def test_contract_completo():
    p = SCFVParser()
    texto = ("CONTRATO VENTA OBJETO: O PRE: x > 0 POST: y == 1 "
             "INVARIANTE: I ELEMENTO: E EVIDENCIA: F")
    r = p.parse_string(texto)
    assert r["contratos"]["VENTA"]["pre"] == "x > 0"
    assert r["contratos"]["VENTA"]["post"] == "y == 1"

def test_contract_negativo():
    p = SCFVParser()
    try:
        p.parse_string("CONTRATO")  # incompleto
        assert False, "Debería haber fallado"
    except SyntaxError:
        pass
