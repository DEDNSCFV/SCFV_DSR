# M1.β · TESTS · auditoría del corpus técnico

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Ventana:** 12.
**Bloque:** M1.β (sub-bloque de M1 · corpus técnico).
**Naturaleza:** inventario + mapa estructural + símbolos consumidos + ejecución pytest.

---

## §0 · Metadatos

```

Ventana:               12
Fecha:                 2026-09-28
Bloque:                M1.β
Subpasos:              M1.β.0 ... M1.β.3
Base medida:           ~/scfv_v6/TESTS
HEAD scfv-dsr previo:  464d935

```

---

## §1 · Magnitud

### Volumen bruto

```

120 archivos       840.878 B   ~841 KB

```

### Purificación

```

Fuente activa:       33 archivos     5.625 L
con contenido:     28 test_*.py
vacíos:             5 (4 init.py + test_integracion.py)
Documentación:        1 archivo          8 L (en .pytest_cache)
Datos ancilares:      2 archivos        47 L (resultados.txt + CSV)
Histórico (backup):   8 archivos     1.814 L

```

---

## §2 · Subpasos ejecutados

```

M1.β.0  INVENTARIO TESTS        ✓ estructura + fuente + reconciliación
M1.β.1  MAPA ESTRUCTURAL        ✓ conteo por archivo, imports, subdirs
M1.β.2  SIMBOLOS POR TEST       ✓ traza de símbolos + cobertura por import
M1.β.3  EJECUCION PYTEST        ✓ 228/229 verde en 36,79 s

```

---

## §3 · Hallazgo estructural

### Cobertura réplica el grafo de PODERES

Los módulos PODERES más importados internamente son también los más importados por los tests:

```

PODERES.CONTABLE.estados                  21 imports internos / 13 tests
PODERES.EPISTEMOLOGICO.modelos.models     varios            / 11 tests
PODERES.CONTABLE.modelos                  varios            /  7 tests
PODERES.EPISTEMOLOGICO.modelos.evidencia  varios            /  5 tests

```

TESTS prueba lo central, no lo periférico.

### Ejecución pytest

```

pytest 9.1.1
229 tests collected in 0,76 s
228 passed · 1 skipped · 0 failed · 36,79 s

```

El corpus TESTS está verde frente al corpus PODERES actual. No hay drift entre código y pruebas.

### Densidad real

```

229 def test_    en 28 archivos
Promedio: 24,5 L por función de test
Promedio: 2,5 módulos PODERES por test

```

### Cuatro tests monolíticos (integration tests disfrazados)

```

test_f3b4_infra_f.py              247 L / 1 def / 6 imports PODERES
test_orquestador_v82_contrato.py  155 L / 1 def / 4 imports PODERES
test_decision_externa.py          136 L / 1 def / 5 imports PODERES
test_orquestador_v82.py           125 L / 1 def / 5 imports PODERES

```

Preparan stack completo, ejecutan flujo, validan múltiples propiedades en una sola función.

### Gemelos orquestador_v82

```

test_orquestador_v82.py            smoke test (corre sin excepción)
test_orquestador_v82_contrato.py   contract test (propiedades del contrato)

```

Complementarios, no redundantes.

---

## §4 · Módulos PODERES sin test

19 módulos sin test directo por import textual (tras corregir falsos positivos del grep):

```

Interfaces (5):        cli/integrador · cli/main · cli/reportes · tui/curses_app · tui/main
Entrypoints DSL (4):   scfv_architect · scfv_validator · verificador_booleano · parser
Aislados (4):          event_store/db · event_store/logger · inflacion/factores · monedas/obtener_tasas
Puentes (4):           event_store/event_store · DEMOSTRATIVO/exportador ·
DEMOSTRATIVO/md_to_pdf · servicios/verificacion
Residuales (2):        sagas/orchestrator · intellectus/intellectus

```

---

## §5 · Observaciones

```

O14  Extensiones anómalas de M1.0 resueltas:
.tipo · .t7 · .pre eran sufijos de backups (.bak.dN.tag)
O15  test_integracion.py = 0 B con nombre canónico
O16  invariantes/ · propiedades/ · validaciones/ son packages vacíos
O17  libros/motor_diario_2026-09.csv: solo encabezado, sin filas
resultados.txt: registro histórico de 19 tests, fechado 26-Ago-2026
O18  5.625 L ≠ 5.625 L efectivos (229 def test_ reales)
O19  Densidad por archivo varía 17 a 247 L por función
O20  Par de tests gemelos sobre orquestador_v82
O21  test_f3b4_infra_f.py no sigue convención test_<módulo>.py
O22  Dos tests importan PODERES.CONTABLE como paquete (as)
O23  resultados.txt cubre 19 tests, no 229 (subsistema paralelo)

```

---

## §6 · Errores propios declarados

```

E5  Error de grep en H3
Patrón 'from $m( |$)' no captura 'from X import Y as Z'
Dos falsos positivos confirmados: reportes_motor · xnor

E6  Error de lectura en H3
intellectus.intellectus parecía sin test; test_v82 importa intellectus/init

```

---

## §7 · Deudas

```

D-M1β-1  19 módulos PODERES sin test directo
D-M1β-2  Cuatro tests monolíticos · taxonomía distinta a unit tests densos
D-M1β-3  test_integracion.py vacío con nombre fuerte
D-M1β-4  Subdirectorios invariantes/propiedades/validaciones sin contenido
D-M1β-5  resultados.txt cubre 19 tests, sistema paralelo de aceptación
D-M1β-6  Un test skipped sin identificar
D-M1β-7  Cero conftest.py · cero fixtures compartidas
D-M1β-8  test_f3b4_infra_f.py nombre no convencional

```

---

## §8 · Cierre

TESTS está actualmente verde (228/229). Cobertura estructural replicando la topología de PODERES. Cero fixtures compartidas. Cuatro integration tests disfrazados de unit. 19 módulos PODERES sin cobertura directa. Sin drift entre código y pruebas.

---

**Fin del acta M1.β.**
