"""
SCFV v8.1 - Dictum: Orientación a partir del mapa normativo
Adaptado para generar estructura JSON (v8.2) además de texto
"""
from typing import Dict, List, Optional

class Dictum:
    @staticmethod
    def orientar(mapa: Dict, formato: str = "texto") -> Dict:
        """
        Genera orientación a partir del mapa normativo.
        - formato="texto": retorna mensaje de texto (compatibilidad v8.1)
        - formato="json": retorna estructura JSON (v8.2)
        - por defecto retorna ambos: {"texto": ..., "json": ...}
        """
        # Construir texto (compatibilidad v8.1)
        lineas = []
        lineas.append("📋 Mapa Normativo Iluminado")
        lineas.append(f"  {mapa['resumen']}")
        lineas.append("")

        if mapa['normas_aplicables']:
            lineas.append("📜 Normas aplicables (por jerarquía):")
            for n in mapa['normas_aplicables']:
                jer = n.get('jerarquia', '?')
                nombre = n.get('nombre', n.get('id', 'Desconocida'))
                fuente = n.get('fuente', 'Sin fuente')
                lineas.append(f"  • {nombre} (jerarquía {jer}) - {fuente}")
        else:
            lineas.append("⚠️ No se encontraron normas aplicables.")

        if mapa['conflictos']:
            lineas.append("")
            lineas.append("⚡ Conflictos normativos detectados:")
            for c in mapa['conflictos']:
                lineas.append(f"  • {c['descripcion']}")
            lineas.append("")
            lineas.append("💡 H₂ debe resolver el conflicto y documentar su decisión.")
        else:
            lineas.append("")
            lineas.append("✅ No se detectaron conflictos normativos.")

        texto = "\n".join(lineas)

        # Construir estructura JSON (v8.2)
        estructura = {
            "estado": "propuesta",
            "resumen": mapa.get('resumen', ''),
            "normas_aplicables": [
                {
                    "id": n.get('id', ''),
                    "nombre": n.get('nombre', ''),
                    "jerarquia": n.get('jerarquia', 0),
                    "fuente": n.get('fuente', ''),
                    "accion_sugerida": n.get('accion_sugerida', {}),
                    "deontica": n.get('deontica', ''),
                    "version_norma": n.get('version_norma', '')
                }
                for n in mapa.get('normas_aplicables', [])
            ],
            "conflictos": mapa.get('conflictos', []),
            "jerarquias": mapa.get('jerarquias', [])
        }

        # Retornar según formato solicitado
        if formato == "texto":
            return {"texto": texto}
        elif formato == "json":
            return {"json": estructura}
        else:
            return {"texto": texto, "json": estructura}
