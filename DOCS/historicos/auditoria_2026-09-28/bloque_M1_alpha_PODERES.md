# M1.α · PODERES · auditoría del corpus técnico

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Ventana:** 12.
**Bloque:** M1.α (sub-bloque de M1 · corpus técnico).
**Naturaleza:** inventario + purificación + mapa estructural + grafo de dependencias + falsación de ciclos.

---

## §0 · Metadatos

```

Ventana:               12
Fecha:                 2026-09-28
Bloque:                M1.α
Subpasos:              M1.α.0 ... M1.α.6
Base medida:           ~/scfv_v6/PODERES
HEAD scfv-dsr previo:  583e42b

```

---

## §1 · Magnitud

### Volumen bruto

```

202 archivos       977.971 B   ~978 KB

```

### Purificación

```

Fuente activa:       72 módulos      9.038 L
Documentación:       10 archivos     1.739 L
Datos/config:         9 archivos        97 L
Histórico (backup):  34 archivos     6.775 L

```

`__pycache__/`, `*.pyc`, `*.bak*`, `*.BACKUP*` excluidos.

### Distribución por poder (fuente activa)

```

CONTABLE          29 archivos   3.289 L
PROFESIONAL       12 archivos   2.778 L
EPISTEMOLOGICO    11 archivos   1.049 L
FORMAL            11 archivos     919 L
INFRAESTRUCTURA    3 archivos     681 L
DEMOSTRATIVO       6 archivos     322 L
TOTAL             72 archivos   9.038 L

```

CONTABLE + PROFESIONAL concentran 67,1 % de la superficie activa.

---

## §2 · Subpasos ejecutados

```

M1.α.0  INVENTARIO PODERES        ✓ estructura + fuente
M1.α.1  PURIFICACIÓN              ✓ activo vs histórico
M1.α.2  MAPA FUNCIONAL            ✓ entrypoints + grafo por poder
M1.α.3  RECIPROCIDADES            ✓ traza de imports cruzados
M1.α.4  CIERRE DIRECTO            ✓ falsación de back-edges
M1.α.5  TRAZA DE CAMINO           ✓ falsación transitiva
M1.α.6  GRAFO REAL / AST+Tarjan   ✓ CICLOS = 0

```

---

## §3 · Hallazgo estructural

### PODERES es un DAG a nivel módulo

Verificado por AST + Tarjan sobre 72 módulos.

```

SCCs no-triviales:  0
Raíces reales:      46 (incluyendo init.py)
Hojas reales:       49 (incluyendo init.py)
Raíces funcionales: 26
Hojas funcionales:  29

```

Los cuatro "ciclos" hipotetizados en M1.α.2/α.3 (PROFESIONAL↔CONTABLE, CONTABLE↔EPISTEMOLOGICO, CONTABLE↔INFRAESTRUCTURA, EPISTEMOLOGICO↔INFRAESTRUCTURA) fueron **falsados** en M1.α.4, M1.α.5 y M1.α.6. Todos los back-edges mueren en hojas.

### Núcleo estable (hojas con alta in-degree)

```

CONTABBLE/estados.py                  21 líneas importándolo
CONTABBLE/modelos.py                  múltiples
CONTABBLE/xnor.py                     múltiples
CONTABBLE/verificador_autorizacion.py múltiples
INFRAESTRUCTURA/serializador_canonico.py  4 módulos · 3 poderes

```

### Entrypoints reales

8 módulos con `if __name__ == '__main__'`:

```

CONTABBLE/proyecciones/proyeccion_diario.py
DEMOSTRATIVO/auditoria/md_to_pdf.py
FORMAL/dsl/scfv_architect.py
FORMAL/dsl/scfv_validator.py
FORMAL/dsl/verificador_booleano.py
PROFESIONAL/interfaces/cli/main.py
PROFESIONAL/interfaces/tui/curses_app.py
PROFESIONAL/interfaces/tui/main.py

```

---

## §4 · Observaciones

```

O1   Discrepancia 72+9=81 vs 82 *.py declarados
O2   Sufijos históricos potencialmente no cubiertos (.old, .orig, ...)
O3   Tres invariantes nombrados sin contenido en FORMAL/
IF-01_partida_doble.md · P-01_soberania.md · V-01_venta_estandar.md
O4   A2 pudo tener doble conteo por línea
O5   Imports en strings/docstrings no distinguidos por grep
O6   A3 tuvo 8 falsos positivos (entrypoints)
O7   Los 7 back-edges son top-level (no defensivos)
O8   Poderes-level ≠ módulo-level
O9   Cuatro módulos destino concentran todo el retorno
O10  23 hojas de 72 módulos activos = 32 %
O11  estados.py es hoja y núcleo simultáneamente
O12  serializador_canonico.py es el adapter canónico de persistencia
O13  Bridges terminales sin declaración de entrypoint:
importador_s0 · exportador · evidencia_provider

```

---

## §5 · Errores propios declarados

```

E1  Filtro de backups incompleto
'! -name .bak_' no captura '.bak.py'
Los 9 archivos .bak.py entraron a "FUENTE PURA"
Corregido en M1.α.1

E2  Patrón de grep truncó nombres con dígitos
'[A-Za-z_.]+' excluye [0-9]
orquestador_v82 → orquestador_v
h2 → h
Corregido en M1.α.6 (AST)

E3  A3 generó falsos positivos por no excluir entrypoints

E4  A2 pudo inflar por doble for other in ...

```

---

## §6 · Deudas

```

D-M1α-1  9 archivos .bak.py en raíz de PODERES · no auditados
D-M1α-2  Tres invariantes .md vacíos en FORMAL/
D-M1α-3  Candidatos a no-consumidos por import textual:
examinador · importador_s0 · inflacion/factores ·
monedas/obtener_tasas · sagas/orchestrator ·
auditoria/exportador · INFRAESTRUCTURA/evidencia_provider
D-M1α-4  Módulos aislados puros:
event_store/db · event_store/logger ·
inflacion/factores · monedas/obtener_tasas ·
dsl/parser · dsl/schema_validator
D-M1α-5  Discrepancia 82 vs 72+9 en *.py

```

---

## §7 · Cierre

PODERES es un DAG a nivel módulo. Cero ciclos dirigidos. La hipótesis inicial de cuatro ciclos inter-poderes fue falsada por AST + Tarjan. El corpus activo (9.038 L) es 43 % del volumen textual total medido; el resto es histórico/documental/datos.

La arquitectura efectiva de PODERES es de grafo ancho con núcleo estable. No presenta acoplamiento circular en tiempo de importación.

---

**Fin del acta M1.α.**
