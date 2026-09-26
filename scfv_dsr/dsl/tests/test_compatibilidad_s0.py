import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scfv_dsr.dsl.parser import SCFVParser

SCFV_V6 = Path.home() / "scfv_v6"
ARCHIVOS = ["ventas", "compras", "inventario", "fiscal"]
CLAVES_S0 = ["fractales", "contexto", "mandante", "tetrada", "booleano"]

def test_historico_parsea():
    p = SCFVParser()
    for nombre in ARCHIVOS:
        path = SCFV_V6 / "DOMINIOS" / nombre / "reglas" / f"{nombre}.scfv"
        r = p.parse_file(str(path))
        for k in CLAVES_S0:
            assert k in r, f"Falta clave {k} en {nombre}"
