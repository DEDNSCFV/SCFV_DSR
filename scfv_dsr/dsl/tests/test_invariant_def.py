import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scfv_dsr.dsl.parser import SCFVParser

def test_invariant_completo():
    p = SCFVParser()
    texto = ("INVARIANTE BALANCE OBJETO: A EXPRESION: x == y DOMINIO: D "
             "SATISFACCION: x == y VERIFICACION: V EVIDENCIA: E")
    r = p.parse_string(texto)
    assert "BALANCE" in r["invariantes"]
    assert r["invariantes"]["BALANCE"]["dominio"] == "D"
