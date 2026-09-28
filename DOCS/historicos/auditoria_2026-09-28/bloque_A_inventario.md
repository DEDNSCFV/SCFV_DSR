# BLOQUE A · INVENTARIO
### Auditoría 2026-09-28 · ~/scfv-dsr

---

## 0 · Alcance y método

Primer bloque del ciclo de diagnóstico completo (7 bloques A-G). Sólo lectura.
Objetivo: inventario puro del sistema. Sin conclusiones, sin recomendaciones,
sin patch.

Cinco sub-bloques ejecutados:

    A.0  herramientas · inventario
    A.1  herramientas faltantes · instalación
    A.2  estructura del repositorio
    A.3  tests · universo
    A.4  dependencias · declaradas vs observadas
    A.5  tamaños · imports · fractales · estado Git

Método: comandos descriptivos. Sin análisis semántico. Sin juicio sobre
calidad. Los hallazgos factuales se registran; su conversión en deuda
formal requiere evidencia de bloques posteriores.

---

## 1 · Herramientas

### 1.1 · Intérpretes

    Python     3.13.13
    pip        26.1.2
    git        2.54.0
    PREFIX     /data/data/com.termux/files/usr

### 1.2 · Herramientas disponibles antes de A.1

    pydeps     3.0.8
    vulture    2.16
    coverage   7.16.2
    radon      6.0.1
    pyflakes   4.0.0
    jq         1.8.2
    tree       2.3.2
    sqlite3    3.53.2

### 1.3 · Herramientas instaladas en A.1

    pylint     4.0.9
    bandit     1.9.4
    mypy       1.20.2    (1.x · sin ast-serialize)

### 1.4 · Herramientas descartadas

    ruff       sin wheel ARM64 · compilación desde Rust colgada
    pip-audit  universo declarado incompleto (ver §4)
    mypy 2.x   requiere ast-serialize (build atascado en Termux)
    fd, rg, bat  no aportan a auditoría estructural

### 1.5 · Paquetes Python relevantes

    coverage   7.16.2
    lark       1.3.1     ← única dependencia runtime
    pydeps     3.0.8
    pyflakes   4.0.0
    pytest     9.1.1
    radon      6.0.1
    vulture    2.16

---

## 2 · Estructura del repositorio

### 2.1 · Raíz

    11 archivos + 5 directorios
    README.md · CHANGELOG.md · CONTRIBUTING.md
    DOCUMENTO_FUNDACIONAL.md (22 KB) · GENEALOGIA.md (13 KB)
    HASHES.txt (10 KB) · LICENSE · VERSION
    pyproject.toml · .gitattributes · .gitignore
    DOCS/ · perfiles/ · scfv_dsr/ · var/ · .git/ · .pytest_cache/

### 2.2 · scfv_dsr/

    6 sub-paquetes + 5 archivos raíz
    raíz:  __init__.py · cli.py · evaluador.py · extractor.py · integrador.py
    contable/           14 .py
    dsl/                 4 archivos + tests/ + ejemplos/
    epistemologico/      7 .py
    fractales/          11 archivos
    infraestructura/     2 .py
    kernel/              7 archivos (3 .py + 4 .json)
    profesional/         3 .py

### 2.3 · Conteo por extensión en scfv_dsr/

    .py       43
    .scfv     14
    .json      4
    .md        1
    .lark      1
    ─────────────
    TOTAL    111 archivos (incluye __pycache__)

### 2.4 · Sub-paquetes por densidad

    contable           14 .py   33% del código
    epistemologico      7 .py
    kernel              3 .py
    profesional         3 .py
    infraestructura     2 .py
    dsl                 2 .py
    raíz                5 .py

---

## 3 · Tests

### 3.1 · Universo en el repositorio

    scfv_dsr/dsl/tests/                                 7 tests
      test_asiento_declarado_def.py    1
      test_compatibilidad_s0.py        1
      test_contract_def.py             3
      test_grammar_lalr.py             1
      test_invariant_def.py            1

    DOCS/historicos/evaluacion/verificacion/            7 tests
      test_soporte_minimo.py           7

    TOTAL en repo: 14 tests

### 3.2 · Tests externos

    ~/test_fase1_atomicidad.py      (fuera del repo)
    ~/test_fase2a_baldor.py         8 tests declarados

### 3.3 · Configuración de pytest

    pytest.ini      ausente
    conftest.py     ausente
    tox.ini         ausente
    [tool.pytest]   ausente

Sin configuración. pytest recorre el árbol completo por defecto.

### 3.4 · test_soporte_minimo.py · dependencias

El test importa:

    leer_eventos_asiento
    normalizar_partidas_para_saldos

Ambos módulos existen en el repo:

    DOCS/historicos/evaluacion/lectura/leer_eventos_asiento.py
    DOCS/historicos/evaluacion/normalizacion/normalizar_partidas_para_saldos.py

La hipótesis previa de módulos inexistentes queda falsificada. La ejecutabilidad
del test bajo configuración específica (PYTHONPATH) es distinta de su ejecución
efectiva; la segunda no fue verificada en este bloque.

---

## 4 · Dependencias

### 4.1 · Declaración

`pyproject.toml`:

    [project]
    name = "scfv-dsr"
    version = "0.1.0"
    requires-python = ">=3.10"
    dependencies = ["lark>=1.0"]

### 4.2 · Fuentes alternativas de declaración

    requirements.txt        ausente
    requirements-dev.txt    ausente
    setup.py                ausente
    setup.cfg               ausente
    Pipfile*                ausente
    poetry.lock             ausente
    environment.yml         ausente

`pyproject.toml` es la única fuente de declaración.

### 4.3 · Imports externos observados

    lark       2 archivos     declarada
    fpdf       1 archivo      NO declarada

`fpdf` se importa (probablemente en `reportes_motor.py`) pero no figura
en `pyproject.toml` ni está instalada.

### 4.4 · Imports sin namespace completo

`scfv_dsr/evaluador.py` es importado sin prefijo `scfv_dsr.` en al menos
un archivo consumidor. Detectado por script de análisis estático.

### 4.5 · Imports dinámicos

    evaluador.py:96                              getattr(baldor, fn_name, None)
    extractor.py:28                              __import__("hashlib")
    integrador.py:43                             __import__(mod, fromlist=[...])
    infraestructura/serializador_canonico.py:143 getattr(obj, campo.name)

El `__import__("hashlib")` inline es cosmético (hashlib es stdlib).

### 4.6 · pip-audit

No ejecutado. Universo declarado (`lark`) es incompleto respecto de
universo real (`lark` + `fpdf`). Auditar un universo parcial no produce
resultado accionable.

---

## 5 · Métricas

### 5.1 · Tamaño total

    5.530 líneas .py en scfv_dsr/

### 5.2 · Archivos más grandes (top 10)

    623  scfv_dsr/kernel/baldor.py
    490  scfv_dsr/contable/event_store.py
    394  scfv_dsr/infraestructura/serializador_canonico.py
    326  scfv_dsr/dsl/parser.py
    315  scfv_dsr/epistemologico/generador_propuesta.py
    284  scfv_dsr/epistemologico/perceptum.py
    280  scfv_dsr/contable/nucleo_consecuencias.py
    221  scfv_dsr/contable/motor.py
    183  scfv_dsr/integrador.py
    180  scfv_dsr/contable/maquina_estados_asiento.py

### 5.3 · Imports más frecuentes

    typing                            22
    pathlib                           10
    uuid                               8
    scfv_dsr.epistemologico.models     8
    dataclasses                        8
    scfv_dsr.contable.estados          8
    json                               7
    sys                                7
    hashlib                            7
    time                               7
    math                               6

Sistema predominantemente stdlib. `lark` no aparece en el top — se usa
sólo en `dsl/parser.py` y su test.

`baldor` no aparece en el top. Confirma acoplamiento dinámico vía `getattr`.

### 5.4 · Fractales

    10 fractales en scfv_dsr/fractales/
    42 invocaciones GENERAR CONSECUENCIA totales

    ARRENDAMIENTOS      12 L    4
    COMBINACIONES       12 L    4
    HIPERINFLACION      12 L    4
    INTANGIBLES         18 L    6
    INVENTARIOS         15 L    4
    MONEDA              12 L    4
    PPE                 18 L    6
    PROVISIONES         12 L    4
    SUBVENCIONES        12 L    4
    VENTAS               9 L    2

    4 .scfv adicionales en scfv_dsr/dsl/ejemplos/ (no son fractales
    de dominio; son ejemplos DSL).

### 5.5 · Estado Git al cierre del Bloque A

    HEAD = de5b7f5 · origin/main = de5b7f5
    git status --short:
      ?? .coverage
      ?? scfv_dsr.svg

---

## 6 · Corpus no leído

Documentos presentes en el repo que no fueron objeto de lectura en ninguna
ventana previa:

    DOCUMENTO_FUNDACIONAL.md     22 KB
    GENEALOGIA.md                13 KB
    HASHES.txt                   10 KB
    VERSION                       6 B
    pyproject.toml              497 B
    .gitattributes              274 B
    .gitignore                  354 B

Directorios con contenido no examinado:

    perfiles/       vacío (en DSR)
    var/            contiene scfv.db (425 KB)

---

## 7 · Correcciones a registros previos

### 7.1 · Retiradas

    D-AUDIT-11   "ausencia de .gitignore"
                 Falsa. .gitignore existe (354 B) y está bien formado.

    D-A4-4       "test_soporte_minimo no ejecutable"
                 Falsa. Los módulos importados existen en el repo.

### 7.2 · Nuevas formulaciones

    D-AUDIT-11'  ".gitignore no cubre .coverage ni scfv_dsr.svg"
                 (única limitación real del archivo)

---

## 8 · Registros de auditoría

Los siguientes hallazgos se registran como observaciones factuales. No
constituyen deuda formal hasta que evidencia adicional (bloques B-G)
determine su estatuto.

    8.1  fpdf importada en reportes_motor.py pero no declarada en
         pyproject.toml ni instalada. Bloque B (estático) puede evaluar
         si el módulo se ejecuta efectivamente.

    8.2  scfv_dsr/evaluador.py importado sin prefijo scfv_dsr. en al
         menos un consumidor. Bloque B puede cuantificar.

    8.3  extractor.py:28 usa __import__("hashlib") inline en lugar de
         import normal. Cosmético.

    8.4  var/scfv.db (425 KB · 2026-09-26) presente en el repo. Origen
         y función no identificados. Bloque D (DB) puede determinar
         si es copia, base de trabajo o artefacto de pruebas.

    8.5  perfiles/ existe en DSR pero está vacío. La resolución de
         perfiles en runtime (si existe) puede usar rutas externas
         (~/scfv_v6/perfiles/) o defaults en código. Bloque C
         (comportamiento) puede verificarlo.

    8.6  DOCUMENTO_FUNDACIONAL.md, GENEALOGIA.md, HASHES.txt, VERSION
         no fueron leídos en ninguna ventana previa. Material doctrinal
         potencialmente relevante para FASE 3.

    8.7  test_soporte_minimo.py (7 tests en DOCS/historicos/evaluacion/)
         contiene pruebas directamente relacionadas con
         validar_partida_doble (test_partida_doble · test_detecta_descuadre).
         Su alcance efectivo se evalúa en bloque posterior.

---

*Bloque A · inventario puro · sólo lectura · sin patch · sin modificación
de código ni DB.*

*Falsado por IA-2 · registros de auditoría distinguidos de deudas formales
antes de materialización.*
