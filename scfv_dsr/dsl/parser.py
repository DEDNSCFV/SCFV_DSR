"""
SCFV_DSR — Parser ADL-SCFV
Extiende SCFV S0 v7.2 (parser.py, hash eebba48b…) para reconocer
CONTRATO, INVARIANTE y ASIENTO_DECLARADO.
"""
import lark
from pathlib import Path
from typing import Dict, List, Any


class SCFVParser:
    def __init__(self):
        grammar_path = Path(__file__).parent / "grammar.lark"
        with open(grammar_path, "r") as f:
            grammar = f.read()
        self.parser = lark.Lark(grammar, start="start", parser="lalr")

    def parse_file(self, filepath: str) -> Dict[str, Any]:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        try:
            tree = self.parser.parse(text)
        except lark.exceptions.UnexpectedInput as e:
            raise SyntaxError(f"Error de sintaxis en {filepath}: {e}")
        return self._transform_tree(tree)

    def parse_string(self, text: str) -> Dict[str, Any]:
        try:
            tree = self.parser.parse(text)
        except lark.exceptions.UnexpectedInput as e:
            raise SyntaxError(f"Error de sintaxis: {e}")
        return self._transform_tree(tree)

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------

    def _get_node_value(self, node):
        if hasattr(node, 'value') and not hasattr(node, 'data'):
            raw = node.value
            if isinstance(raw, str) and raw.startswith('"') and raw.endswith('"'):
                raw = raw[1:-1]
            if raw == "VERDADERO":
                return True
            elif raw == "FALSO":
                return False
            return raw
        elif hasattr(node, 'children') and node.children:
            return self._get_node_value(node.children[0])
        return None

    def _is_token(self, node):
        return hasattr(node, 'value') and not hasattr(node, 'data')

    def _token_str(self, node):
        return str(node.value) if self._is_token(node) else None

    def _expr_to_str(self, node) -> str:
        if self._is_token(node):
            return str(node.value)
        if not hasattr(node, 'data'):
            return str(node)

        d = node.data
        if d == 'comparison':
            if len(node.children) == 3:
                return (f"{self._expr_to_str(node.children[0])} "
                        f"{self._expr_to_str(node.children[1])} "
                        f"{self._expr_to_str(node.children[2])}")
            return self._expr_to_str(node.children[0])
        if d in ('arith', 'term'):
            out = []
            for c in node.children:
                if hasattr(c, 'data') and c.data == 'arith':
                    out.append('(' + self._expr_to_str(c) + ')')
                else:
                    out.append(self._expr_to_str(c))
            return ' '.join(out)
        if d == 'factor':
            return self._expr_to_str(node.children[0])
        if d == 'value':
            return self._expr_to_str(node.children[0])
        if d == 'list_value':
            inner = ', '.join(self._expr_to_str(c) for c in node.children)
            return f"[{inner}]"
        if d == 'condition':
            out = []
            for c in node.children:
                if self._is_token(c):
                    out.append(str(c.value))
                else:
                    out.append(self._expr_to_str(c))
            return ' '.join(out)
        return ' '.join(self._expr_to_str(c) for c in node.children)

    def _as_expr_node(self, node):
        """Devuelve el nodo de expresión (comparison u hoja)."""
        if self._is_token(node):
            return node
        if hasattr(node, 'data') and node.data == 'comparison':
            return node
        if hasattr(node, 'children') and node.children:
            return node.children[0]
        return node

    # ------------------------------------------------------------------
    # Transformación
    # ------------------------------------------------------------------

    def _transform_tree(self, tree: lark.Tree) -> Dict[str, Any]:
        result = {
            "fractales": {}, "contexto": {}, "mandante": {},
            "tetrada": {}, "booleano": {},
            "contratos": {}, "invariantes": {}, "asientos_declarados": {}
        }

        for child in tree.children:
            if not hasattr(child, 'data'):
                continue

            if child.data == "fractal_def":
                self._handle_fractal(child, result)
            elif child.data == "contexto_def":
                self._handle_assignments(child, "assignment", result["contexto"])
            elif child.data == "mandante_def":
                self._handle_assignments(child, "assignment", result["mandante"])
            elif child.data == "tetrada_def":
                self._handle_assignments(child, "tetrada_item", result["tetrada"])
            elif child.data == "booleano_def":
                self._handle_assignments(child, "booleano_item", result["booleano"])
            elif child.data == "contract_def":
                self._handle_contract(child, result)
            elif child.data == "invariant_def":
                self._handle_invariant(child, result)
            elif child.data == "asiento_declarado_def":
                self._handle_asiento_declarado(child, result)

        return result

    def _handle_fractal(self, child, result):
        name = self._get_node_value(child.children[0])
        rules = []
        for node in child.children[1:]:
            if hasattr(node, 'data') and node.data == "rule":
                rule_name = self._get_node_value(node.children[0])
                cond_expr = self._extract_condition(node)
                actions = self._extract_actions(node)
                rules.append({"name": rule_name, "condition": cond_expr,
                              "actions": actions})
        result["fractales"][name] = rules

    def _handle_assignments(self, child, item_data, target):
        for item in child.children:
            if hasattr(item, 'data') and item.data == item_data:
                name = self._get_node_value(item.children[0])
                value = self._get_node_value(item.children[1])
                target[name] = value

    # ---- contract_def -----------------------------------------------

    def _extraer_por_keywords(self, tokens, keywords):
        """Devuelve dict {kw: [value_tokens]} escaneando tokens por
        posiciones de keywords. Ignora ':' si aparecen."""
        # Encontrar posiciones de keywords
        posiciones = []
        for idx, t in enumerate(tokens):
            if self._is_token(t) and self._token_str(t) in keywords:
                posiciones.append((idx, self._token_str(t)))
        posiciones.append((len(tokens), None))

        resultado = {}
        for k in range(len(posiciones) - 1):
            idx, kw = posiciones[k]
            next_idx, _ = posiciones[k + 1]
            value_tokens = tokens[idx + 1:next_idx]
            # Filtrar ':' literales si están presentes
            value_tokens = [
                v for v in value_tokens
                if not (self._is_token(v) and str(v.value) == ":")
            ]
            resultado[kw] = value_tokens
        return resultado

    def _handle_contract(self, child, result):
        tokens = list(child.children)
        name = self._get_node_value(tokens[1])
        data = {"nombre": name, "objeto": None, "pre": None, "post": None,
                "invariantes": [], "elementos": [], "evidencia": []}

        campos = self._extraer_por_keywords(
            tokens,
            {"OBJETO", "PRE", "POST", "INVARIANTE", "ELEMENTO", "EVIDENCIA"}
        )

        if "OBJETO" in campos and campos["OBJETO"]:
            v = campos["OBJETO"][0]
            data["objeto"] = self._token_str(v) if self._is_token(v) else self._expr_to_str(v)

        if "PRE" in campos and campos["PRE"]:
            data["pre"] = self._expr_to_str(campos["PRE"][0])

        if "POST" in campos and campos["POST"]:
            data["post"] = self._expr_to_str(campos["POST"][0])

        if "INVARIANTE" in campos:
            data["invariantes"] = [
                self._token_str(v) for v in campos["INVARIANTE"] if self._is_token(v)
            ]

        if "ELEMENTO" in campos:
            data["elementos"] = [
                self._token_str(v) for v in campos["ELEMENTO"] if self._is_token(v)
            ]

        if "EVIDENCIA" in campos:
            data["evidencia"] = [
                self._token_str(v) for v in campos["EVIDENCIA"] if self._is_token(v)
            ]

        result["contratos"][name] = data

    # ---- invariant_def ----------------------------------------------

    def _handle_invariant(self, child, result):
        tokens = list(child.children)
        name = self._get_node_value(tokens[1])
        data = {"nombre": name, "objeto": None, "expresion": None,
                "dominio": None, "satisfaccion": None,
                "verificacion": None, "evidencia": []}

        campos = self._extraer_por_keywords(
            tokens,
            {"OBJETO", "EXPRESION", "DOMINIO", "SATISFACCION",
             "VERIFICACION", "EVIDENCIA"}
        )

        if "OBJETO" in campos and campos["OBJETO"]:
            v = campos["OBJETO"][0]
            data["objeto"] = self._token_str(v) if self._is_token(v) else self._expr_to_str(v)

        if "EXPRESION" in campos and campos["EXPRESION"]:
            data["expresion"] = self._expr_to_str(campos["EXPRESION"][0])

        if "DOMINIO" in campos and campos["DOMINIO"]:
            v = campos["DOMINIO"][0]
            data["dominio"] = self._token_str(v) if self._is_token(v) else self._expr_to_str(v)

        if "SATISFACCION" in campos and campos["SATISFACCION"]:
            data["satisfaccion"] = self._expr_to_str(campos["SATISFACCION"][0])

        if "VERIFICACION" in campos and campos["VERIFICACION"]:
            v = campos["VERIFICACION"][0]
            data["verificacion"] = self._token_str(v) if self._is_token(v) else self._expr_to_str(v)

        if "EVIDENCIA" in campos:
            data["evidencia"] = [
                self._token_str(v) for v in campos["EVIDENCIA"] if self._is_token(v)
            ]

        result["invariantes"][name] = data

    # ---- asiento_declarado_def --------------------------------------

    def _handle_asiento_declarado(self, child, result):
        tokens = list(child.children)
        name = self._get_node_value(tokens[1])

        cuerpo = []
        for t in tokens[2:]:
            if self._is_token(t) and str(t.value) != ":":
                cuerpo.append(self._token_str(t))

        result["asientos_declarados"][name] = {"nombre": name,
                                               "cuerpo": cuerpo}

    # ---- rules (heredado de S0) -------------------------------------

    def _extract_condition(self, node) -> str:
        for child in node.children:
            if hasattr(child, 'data') and child.data == "condition":
                parts = []
                for sub in child.children:
                    if self._is_token(sub):
                        parts.append(str(sub.value))
                    elif hasattr(sub, 'data'):
                        parts.append(self._expr_to_str(sub))
                    else:
                        parts.append(str(sub))
                return " ".join(parts)
        return ""

    def _extract_actions(self, node) -> List[str]:
        actions = []
        for child in node.children:
            if hasattr(child, 'data') and child.data == "action":
                sub = child.children[0]
                if not hasattr(sub, 'data'):
                    continue
                if sub.data == "assignment":
                    name = self._get_node_value(sub.children[0])
                    value = self._expr_to_str(sub.children[1])
                    actions.append(f"{name} = {value}")
                elif sub.data == "generate":
                    params = self._extract_param_list(sub)
                    acciones_str = ', '.join(f'{k}={v}' for k, v in params.items())
                    actions.append(f"GENERAR CONSECUENCIA ({acciones_str})")
        return actions

    def _extract_param_list(self, node) -> Dict[str, str]:
        plist = None
        if hasattr(node, 'data') and node.data == "param_list":
            plist = node
        else:
            for c in node.children:
                if hasattr(c, 'data') and c.data == "param_list":
                    plist = c
                    break
        if plist is None:
            return {}
        params = {}
        for p in plist.children:
            if hasattr(p, 'data') and p.data == "param":
                name = self._get_node_value(p.children[0])
                value = self._expr_to_str(p.children[1])
                params[name] = value
        return params
