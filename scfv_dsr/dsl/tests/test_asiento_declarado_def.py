import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scfv_dsr.dsl.parser import SCFVParser

def test_asiento_minimo():
    p = SCFVParser()
    texto = "ASIENTO_DECLARADO VENTA_001: A B C"
    r = p.parse_string(texto)
    assert "VENTA_001" in r["asientos_declarados"]
    assert r["asientos_declarados"]["VENTA_001"]["cuerpo"] == ["A", "B", "C"]
