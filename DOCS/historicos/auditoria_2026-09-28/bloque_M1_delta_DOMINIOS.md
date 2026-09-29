# M1.δ · DOMINIOS · auditoría del corpus técnico

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Ventana:** 12.
**Bloque:** M1.δ (sub-bloque de M1 · corpus técnico).
**Naturaleza:** inventario + lectura de contenido + cierre de M1.

---

## §0 · Metadatos

```

Ventana:               12
Fecha:                 2026-09-28
Bloque:                M1.δ
Subpasos:              M1.δ.0 ... M1.δ.1
Base medida:           ~/scfv_v6/DOMINIOS
HEAD scfv-dsr previo:  b70739c

```

---

## §1 · Magnitud

### Volumen bruto

```

26 archivos       53.391 B   ~53 KB

```

### Fuente activa (tras purificación)

```

Código Python:    10 archivos    378 L
Documentación:     2 archivos    483 L
Schemas DSL:       4 archivos     31 L

```

Cero `.json`, `.csv`, `.sql`, `.bak*`, `.BACKUP*`.

### Distribución por dominio

```

fiscal/fiscal.py         291 L   ← único con cuerpo real
ventas/ventas.py          39 L   ← stub
base_fractal.py           23 L   ← base común
compras/compras.py        15 L   ← stub
inventario/inventario.py   8 L   ← stub vacío
init.py (5)            2 L

```

Documentación:

```

ventas/README.md         255 L   ← 6,5x el código
compras/README.md        228 L   ← 15x el código

```

---

## §2 · Subpasos ejecutados

```

M1.δ.0  INVENTARIO DOMINIOS   ✓ estructura + fuente + reconciliación
M1.δ.1  CONTENIDO DOMINIOS    ✓ lectura de fiscal + stubs + schemas DSL

```

---

## §3 · Hallazgos estructurales

### DOMINIOS está desconectado del corpus operativo

Verificado por ausencia cruzada:

```

O8 (M1.δ.0)      DOMINIOS no importa PODERES
E1 (M1.α.5)      PODERES no importa DOMINIOS
H2 (M1.β.2)      Ningún test importa DOMINIOS
N1 (M1.γ.4)      DOMINIOS no aparece en sqlite3.connect

```

DOMINIOS es un subárbol aislado. No consumido, no consumidor. Presente físicamente pero desconectado.

### Estrato arqueológico v8.1

Los docstrings internos lo confirman:

```

ventas.py:       "Fractal de Ventas (v8.1 con I6)"
base_fractal.py: "BaseFractal - Clase base para todos los fractales (v8.1 con I6)"
fiscal.py:       "SCFV v6 — Fractal de Fiscal"

```

PODERES opera en v8.2 (`orquestador_v82`, `test_motor_v82`, `test_v82_nuevas_capacidades`).

DOMINIOS es la arquitectura precedente. No fue borrada, no fue migrada, no fue desconectada explícitamente. Quedó como estrato.

### Dos implementaciones paralelas del modelo "evidencia → consecuencias"

Camino PODERES (activo, v8.2):

```

evidencia → perceptum → generador_propuesta → H2 → orquestador_v82 → motor_contable → consecuencias

```

Camino DOMINIOS (huérfano, v8.1):

```

evidencia → Fractal.evaluar() → consecuencias (directo)

```

Mismo dominio conceptual, arquitecturas independientes. Nunca convergieron.

### Error de ejecución latente en BaseFractal

Contrato de clase base (`base_fractal.py`):

```python
class BaseFractal:
    def __init__(self):
        self.normas_aplicables = []
```

Constructor sin argumentos.

Implementación hija (fiscal.py):

```python
class FractalFiscal(BaseFractal):
    def __init__(self, db_connection, event_store):
        super().__init__(db_connection, 'fiscal', event_store)
```

Tres argumentos a un constructor que acepta cero.

FractalFiscal(db, es) lanzaría TypeError: BaseFractal.__init__() takes 1 positional argument but 4 were given.

DOMINIOS probablemente nunca se ejecutó en su estado actual.

Bug repetido en 3 archivos: docstring huérfano + import duplicado

fiscal.py:1-9:

```python
from typing import Dict, List, Optional      ← línea 1
"""                                          ← docstring huérfano
SCFV v6 — Fractal de Fiscal
"""
import uuid
from typing import Dict, Any, Optional, List ← typing por segunda vez
```

ventas.py:1-5, base_fractal.py:1-6: mismo patrón.

En Python el docstring de módulo debe ser la primera statement. Aquí la primera es un from, así que la triple-quoted string es expresión sin efecto. fiscal.__doc__ es None.

Fiscal accede a tablas no materializadas

Consultas en fiscal.py:

```sql
SELECT tasa FROM negocio_fiscal_config WHERE periodo_id = ? AND impuesto = 'IVA' AND activo = 1
```

```sql
UPDATE negocio_fiscal_declaraciones SET total_retenciones = total_retenciones + ?
```

negocio_fiscal_config y negocio_fiscal_declaraciones están en schema_final.sql y migración 006. No están en ninguna DB runtime inspeccionada. Falla con no such table.

Los 4 schemas DSL declaran más de lo que implementan

inventario.scfv declara dos reglas:

```
REGLA ENTRADA_INVENTARIO: ...
REGLA SALIDA_INVENTARIO: ...
```

inventario.py retorna lista vacía con comentario honesto:

```python
# Por ahora, no generamos consecuencias contables para no duplicar partidas.
return []
```

Inversión respecto a fiscal, donde .py implementa más que el .scfv.

Dos representaciones de la misma regla

.py usa cuentas hardcoded:

```python
{"cuenta": "110101", "naturaleza": "DEUDORA", ...}
{"cuenta": "410101", "naturaleza": "ACREEDORA", ...}
```

.scfv usa símbolos canónicos:

```
GENERAR CONSECUENCIA (cuenta=CUENTA_CAJA, naturaleza=DEUDORA, ...)
GENERAR CONSECUENCIA (cuenta=CUENTA_VENTAS, naturaleza=ACREEDORA, ...)
```

Sin puente. Nunca convergieron.

---

§4 · Observaciones

```
O37  fiscal/fiscal.py (291 L) sin test
O38  .scfv de DOMINIOS son instancias, no schemas
O39  base_fractal.py es paquete huérfano (23 L, no importado)
O40  .py con cuentas hardcoded vs .scfv con símbolos canónicos
O41  fiscal.py accede a tablas declaradas pero no materializadas
O42  ventas/README.md describe máquina de estados 6x más compleja que ventas.py
O43  inventario.py retorna [] pero inventario.scfv declara reglas
```

---

§5 · Errores propios declarados

Ninguno específico de M1.δ. Los acumulados en bloques previos (E1–E8) siguen vigentes.

---

§6 · Deudas

```
D-M1δ-1   DOMINIOS desconectado del runtime (O8 + E1 + H2 + N1)
D-M1δ-2   BaseFractal.__init__ incompatible con FractalFiscal
D-M1δ-3   Docstring huérfano + import duplicado en 3 archivos
D-M1δ-4   fiscal.py accede a tablas no materializadas
D-M1δ-5   READMEs documentan 6-15x lo implementado
D-M1δ-6   .scfv declaran reglas no implementadas y viceversa
D-M1δ-7   base_fractal.py huérfano
D-M1δ-8   inventario.py stub vacío con .scfv completo
D-M1δ-9   Dominio fiscal sin test
```

---

§7 · Cierre de M1

```
M1.0   SIZING GLOBAL                ✓
M1.α   PODERES (7 subpasos)         ✓ DAG, cero ciclos
M1.β   TESTS (4 subpasos)           ✓ 228/229 verde
M1.γ   INFRAESTRUCTURA (5 subpasos) ✓ divergencia estructural
M1.δ   DOMINIOS (2 subpasos)        ✓ estrato arqueológico
```

Corpus técnico total auditado: ~17.000 L fuente activa.

Firma estructural de M1:

1. PODERES es un DAG limpio · cero ciclos.
2. TESTS está verde · cobertura replica topología de PODERES.
3. INFRAESTRUCTURA declara 26 tablas que el runtime nunca materializa.
4. DOMINIOS es un estrato v8.1 desconectado del runtime v8.2.

El sistema tiene una arquitectura v8.2 coherente internamente (PODERES + TESTS), con dos estratos desconectados: la capa declarativa SQL (INFRAESTRUCTURA) y la capa precedente (DOMINIOS).

---

Fin del acta M1.δ.
Fin de M1.
