import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lark import Lark

def test_lalr_construye():
    g = (Path(__file__).parent.parent / "grammar.lark").read_text()
    p = Lark(g, start="start", parser="lalr")
    assert p is not None
