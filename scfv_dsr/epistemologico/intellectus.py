"""
SCFV v8.1 - Intellectus: Mapa Normativo Iluminado (con normalización)
Adaptado para soportar condiciones compuestas AND/OR (v8.2)
"""
from typing import Dict, List, Any

class Intellectus:
    """Intérprete hermenéutico-deconstructivo."""

    @staticmethod
    def _evaluar_condicion(condicion: Dict, senales: Dict, perfil_attrs: Dict) -> bool:
        """
        Evalúa una condición (simple o compuesta AND/OR) contra señales y perfil.
        """
        if not isinstance(condicion, dict):
            return False

        # Condición compuesta: AND
        if "AND" in condicion:
            return all(Intellectus._evaluar_condicion(sub, senales, perfil_attrs)
                       for sub in condicion["AND"])

        # Condición compuesta: OR
        if "OR" in condicion:
            return any(Intellectus._evaluar_condicion(sub, senales, perfil_attrs)
                       for sub in condicion["OR"])

        # Condición simple: {"campo": "valor"}
        for clave, valor_esperado in condicion.items():
            # Buscar en señales o en perfil
            valor_real = senales.get(clave, perfil_attrs.get(clave))
            if valor_real is None:
                return False  # La clave no existe en ningún lado
            # Comparar (convertir a string para flexibilidad)
            if str(valor_real).lower() != str(valor_esperado).lower():
                return False
        return True

    @staticmethod
    def construir_mapa_normativo(
        evidencia: Dict,
        perfil: Dict,
        normas: List[Dict]
    ) -> Dict:
        # 1. Normalizar señales de la evidencia
        senales = {k.lower(): v for k, v in evidencia.items()}
        if "moneda" not in senales:
            senales["moneda"] = "VES"
        if "monto" not in senales:
            senales["monto"] = 0

        # 2. Normalizar perfil (claves a minúsculas)
        perfil_lower = {k.lower(): v for k, v in perfil.items()}
        perfil_attrs = {
            "regimen_iva": perfil_lower.get("regimen_iva", "General"),
            "regimen_islr": perfil_lower.get("regimen_islr", "General"),
            "sector": perfil_lower.get("sector", "Comercio"),
            "marco_contable": perfil_lower.get("marco_contable", "NIIF_Completas"),
            "economia_hiperinflacionaria": perfil_lower.get("economia_hiperinflacionaria", "false"),
        }

        # 3. Filtrar normas aplicables usando _evaluar_condicion
        aplicables = []
        for norma in normas:
            condiciones = norma.get("condiciones_activacion", {})
            # Si no hay condiciones, la norma aplica por defecto
            if not condiciones:
                cumple = True
            else:
                cumple = Intellectus._evaluar_condicion(condiciones, senales, perfil_attrs)
            if cumple:
                aplicables.append(norma)

        # 4. Clasificar por jerarquía
        aplicables_ordenadas = sorted(aplicables, key=lambda x: x.get("jerarquia", 999))

        # 5. Detectar conflictos
        conflictos = []
        for i, n1 in enumerate(aplicables_ordenadas):
            for n2 in aplicables_ordenadas[i+1:]:
                accion1 = n1.get("accion_sugerida", {})
                accion2 = n2.get("accion_sugerida", {})
                if accion1.get("tipo") == accion2.get("tipo") and accion1.get("valor") != accion2.get("valor"):
                    conflictos.append({
                        "norma_a": n1.get("id"),
                        "norma_b": n2.get("id"),
                        "tipo": "conflicto_valor",
                        "descripcion": f"{n1.get('id')} sugiere {accion1.get('valor')} vs {n2.get('id')} sugiere {accion2.get('valor')}"
                    })

        # 6. Construir mapa
        mapa = {
            "normas_aplicables": aplicables_ordenadas,
            "conflictos": conflictos,
            "jerarquias": [
                {"jerarquia": n.get("jerarquia"), "norma": n.get("id")}
                for n in aplicables_ordenadas
            ],
            "resumen": f"Se activaron {len(aplicables_ordenadas)} normas. {len(conflictos)} conflictos detectados."
        }
        return mapa

    @staticmethod
    def interpretar(evidencia: Dict, perfil: Dict, normas: List[Dict]) -> Dict:
        return Intellectus.construir_mapa_normativo(evidencia, perfil, normas)
