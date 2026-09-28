# INFORME TÉCNICO · FASE 4 RECONOCIMIENTO
### Ventana 8 · 2026-09-28 · ~/scfv-dsr

---

## 0 · Encabezado

**Objeto.** Reconocimiento material de la cadena epistemológica declarada en
`npl-definitivo.md:13` y de los componentes contables contiguos, para
determinar qué opera en `scfv_dsr/` y qué no.

**Alcance.** Cinco bloques de lectura, sólo lectura. Sin patch, sin commit,
sin modificación de DB.

**Base.** HEAD `1db6c90` · origin/main sincronizado · repo limpio · 7 DSL ·
8 juez FASE 2.a · DB 285 eventos CADENA_INTEGRA (no tocada).

**Método.** Lectura cruzada entre tres fuentes: `scfv_dsr/` (implementación
DSR), `~/scfv_v6/PODERES/` (S0), `~/scfv_v6/DOCS/` (corpus doctrinal).
Diferenciales `diff` para separar port de divergencia. Greps acotados para
localizar consumidores. Cada hallazgo registra el comando que lo verifica.

**Convención.** Cuando la evidencia es parcial, el informe lo declara como
tal. Las conclusiones arquitectónicas se reservan para FASE 3.

---

## 1 · Correcciones al traspaso de entrada

**C-1 · La cadena del traspaso era inferida, no declarada.**
El traspaso afirmaba `perceptum → intellectus → dictum → evidencia`. En las
fuentes examinadas para este reconocimiento no se encontró una fuente que
enuncie esa secuencia. `npl-definitivo.md:13` declara:

    EVIDENCIA → OBSERVACIÓN (H₁) → PROPUESTA (H₁) → DICTUM (C) → H₂ (Contador)

`intellectus` no figura en esa declaración.

**C-2 · `perceptum` no está huérfano.**
El traspaso lo omitía del inventario (mencionaba sólo intellectus y dictum).
`perceptum.py` (284 L) existe y tiene consumidor activo identificado en
`extractor.py`.

**C-3 · El paquete `epistemologico/` contiene siete archivos, no tres.**

    __init__.py            · 0 B      · vacío
    perceptum.py           · 284 L    · 2026-09-26 12:14
    evidencia.py           · 4667 B   · 2026-09-26 12:14
    generador_propuesta.py · 6966 B   · 2026-09-26 12:14
    models.py              · 2193 B   · 2026-09-26 18:08
    intellectus.py         · 105 L    · 2026-09-26 18:08
    dictum.py              · 71 L     · 2026-09-26 18:08

Corte temporal entre dos grupos: 12:14 y 18:08.

**C-4 · El push ya estaba hecho.**
El traspaso declaraba "7 commits ahead origin/main · sin push". Al ejecutar
`git push` la respuesta fue `Everything up-to-date`. `git status -sb` reportó
`## main...origin/main` sin `ahead`.

---

## 2 · Hallazgos

Diecinueve hallazgos, agrupados por bloque donde fueron obtenidos.

### Bloque 1 · inventario y consumidores

**H1 · `perceptum.py` existe y es extenso.**
284 líneas. Docstring declara: `Evidencia -> ObservacionH1`. Autodenominado
`SCFV v6.1` con `S0 — Extensión DA-1` documentada en cabecera.
Verificación: `wc -l scfv_dsr/epistemologico/perceptum.py`.

**H2 · `perceptum` tiene un único consumidor externo identificado.**
El grep
`grep -rn "intellectus\|dictum\|perceptum" --include="*.py" scfv_dsr/ | grep -v epistemologico/`
identifica un único consumidor externo: `scfv_dsr/extractor.py`, con
importación en línea 19 e invocación en línea 42 (dentro de
`observacion_desde_evento`).
El grep no agota el universo de consumidores posibles (por ejemplo,
importaciones dinámicas o referencias no textuales). Lo declarado es el
consumidor identificado por el patrón textual aplicado.

**H3 · La cadena npl no menciona Intellectus.**
`~/scfv_v6/DOCS/npl/npl-definitivo.md:13` declara la secuencia sin
`intellectus`. El grep
`grep -n -i "intellectus\|dictum\|perceptum\|cadena" ~/scfv_v6/DOCS/npl/npl-definitivo.md`
devuelve coincidencias del tipo NPL `Cadena` (uso de la palabra como tipo) y
la línea 13 (`DICTUM`). No aparecen coincidencias de `intellectus` ni de
`perceptum`.

**H4 · Intellectus y Dictum tienen lógica real.**
`intellectus.py` implementa evaluación recursiva de condiciones compuestas
AND/OR (`_evaluar_condicion`) y normalización de señales con defaults
(`regimen_iva`, `sector`, `marco_contable`, `economia_hiperinflacionaria`).
`dictum.py` construye texto legible y estructura JSON con `estado="propuesta"`
+ `accion_sugerida` + `deontica`.
Verificación: `head -60` de ambos archivos.

### Bloque 2 · cabeceras y acoplamiento interno

**H5 · Dos caminos coexisten en `epistemologico/`.**

Camino A (tipado, dataclass):

    Evidencia → Perceptum → ObservacionH1 → GeneradorPropuesta
              → PropuestaH1 + MetricasH1(r,s,o,t,v)

Camino B (dict sin tipos):

    {evidencia: Dict} → Intellectus.construir_mapa_normativo → mapa
                      → Dictum.orientar → {texto, json}

No comparten tipos. Camino B no importa `models.py` ni `evidencia.py`.
Camino A no importa `intellectus` ni `dictum`.

**H6 · `generador_propuesta.py:10` declara la bifurcación.**
Docstring literal: `No depende de Dictum ni H₂.` La omisión del camino B está
escrita como propiedad, no como deuda.

### Bloque 3 · diferenciales y consumidores ampliados

**H7 · Los diffs examinados no muestran divergencia lógica; las diferencias
observadas son de imports.**
Los tres `diff` DSR↔S0 aplicados a `perceptum.py`, `intellectus.py` y
`dictum.py` muestran las siguientes diferencias textuales:

| archivo | diferencia |
|---|---|
| perceptum | `PODERES.CONTABLE.estados` → `scfv_dsr.contable.estados`; `PODERES.EPISTEMOLOGICO.*` → `scfv_dsr.epistemologico.*` |
| intellectus | `from typing import Dict, List, Any` → `from typing import Dict, List` |
| dictum | `from typing import Dict, List, Optional` → `from typing import Dict` |

Verificación: `diff -u ~/scfv_v6/PODERES/EPISTEMOLOGICO/{mod}/{mod}.py scfv_dsr/epistemologico/{mod}.py`.
Las diferencias observadas son de imports. El diff no revela cambios en el
cuerpo de las funciones comparadas dentro del rango inspeccionado; no se
afirma ausencia de divergencia fuera de ese rango.

**H8 · El camino A está cableado.**
Comando:
`grep -rn "generador_propuesta\|GeneradorPropuesta\|PropuestaH1\|ObservacionH1\|Evidencia\b\|Perceptum" --include="*.py" scfv_dsr/ | grep -v "scfv_dsr/epistemologico/"`
localiza:

    extractor.py:19,42          Perceptum.extraer(ev)
    integrador.py:52-54         ObservacionH1, EntidadExtraida
    orquestador.py:19           generar_propuesta_h1
    h2.py:13,42,54              PropuestaH1 como entrada de H₂

El pipeline DSR encadena `evento → extractor → Perceptum → ObservacionH1 →
generador_propuesta → PropuestaH1 → h2.H2Decision → DecisionProfesional →
EventStore`, sin invocar `intellectus` ni `dictum`.

**H9 · `c3-componentes.md` declara siete componentes del Núcleo Epistemológico.**
Líneas 213-260: Perceptum, Intellectus, Dictum, CBR Manager, Reglas
Normativas, Ontología, Aprendizaje. Intellectus en c3 se describe con cinco
subsistemas que producen r,s,o,t,v (Reglas→r, CBR→s, Ontología→o, Peso
temporal→t, Volatilidad→v).
En DSR existen **archivos correspondientes a tres nombres de componente**:
`perceptum.py`, `intellectus.py`, `dictum.py`. Que su contenido implemente el
componente c3 del mismo nombre es una cuestión distinta — para Intellectus,
el propio informe registra que no (ver H15).

**H10 · Los nombres de módulos citados en el traspaso Ventana 7 (§7.3) se
encuentran dispersos en DSR, no agrupados.**
El traspaso cita `ACTO_6_0_CONV_CONVERGENCIA §7.3` como fuente que enumera
cinco módulos: dictum, intellectus, examinador, reticulo, reportes_motor.
Esa lista **no proviene de `c3-componentes.md`** (cuyos componentes son siete
y distintos). Son dos fuentes doctrinales con listas distintas.

Ubicación material de los nombres de §7.3 en DSR, verificada por
`find` por nombre + `grep` por consumidores:

| módulo §7.3 | ubicación DSR | verificación de consumidor |
|---|---|---|
| `dictum` | `epistemologico/dictum.py` | ningún consumidor identificado (H12) |
| `intellectus` | `epistemologico/intellectus.py` | ningún consumidor identificado |
| `examinador` | `contable/examinador.py` | ningún consumidor identificado (H17) |
| `reticulo` | `contable/reticulo.py` | sólo `examinador` lo importa (H16) |
| `reportes_motor` | `contable/reportes_motor.py` | ver H10.b |

**H10.b · `reportes_motor` · propiedades verificadas por separado.**

- **Ubicación:** `scfv_dsr/contable/reportes_motor.py` (verificado por `find`).
- **Versión declarada:** el docstring leído en el reconocimiento lo identifica
  como `SCFV Motor 9.0.0 — Reportes desde EventStore`.
- **Alcance declarado:** el mismo docstring declara `Módulo EventStore-only.
  No lee proyecciones legacy (negocio_*)`.
- **Consumidor:** no verificado en este reconocimiento.
- **Estado:** la actividad del módulo no fue verificada por ejecución; sólo se
  registra la declaración de propósito en su docstring.

### Bloque 4 · journals y contexto c3

**H11 · El journal declara finalidad declarada, no intención.**
`~/scfv_v6/DOCS/journal/2026-09-02-evolucion-8.1-a-8.2.md:84`:

    ✅ Dictum estructurado: JSON para comunicación programática con H₂.

Las líneas 22 y 23 del mismo journal registran extensión de Intellectus
(AND/OR) y Dictum (JSON) como hitos completados.
Que esa comunicación con H₂ aparezca o no en el pipeline DSR es un hecho
distinto, registrado en H13.

**H12 · Con el filtro aplicado, el único resultado mostrado fuera de los
archivos `intellectus.py` y `dictum.py` es el siguiente.**
Comando:
`grep -rn -i "intellectus\|dictum" scfv_dsr/ --include="*.py" --include="*.md" --include="*.json" --include="*.scfv" | grep -v "epistemologico/\(intellectus\|dictum\).py:"`
Único resultado mostrado:

    scfv_dsr/epistemologico/generador_propuesta.py:10:No depende de Dictum ni H₂.

El filtro excluye únicamente las dos rutas `epistemologico/intellectus.py` y
`epistemologico/dictum.py`. Otras rutas dentro de `epistemologico/` no quedan
excluidas por el patrón; de hecho, el resultado mostrado pertenece a esa
carpeta. Lo declarado es que, con este filtro, sólo ese resultado aparece.

**H13 · La etapa DICTUM del npl no se ejecuta en DSR.**

| etapa npl | implementación DSR | estado |
|---|---|---|
| EVIDENCIA | `evidencia.py` (dataclass) | presente |
| OBSERVACIÓN (H₁) | `perceptum.py` | presente |
| PROPUESTA (H₁) | `generador_propuesta.py` | presente |
| DICTUM (C) | `dictum.py` consume `mapa` de Intellectus, no `PropuestaH1` | no integrado |
| H₂ | `h2.py` consume `PropuestaH1` directamente | presente |

El pipeline real no invoca `dictum.py`. La etapa DICTUM declarada en npl:13
no opera.

### Bloque 5 · verificación de roles

**H14 · `generador_propuesta.py` calcula r, s, o, t y v.**
Definiciones visibles por
`grep -n "def calcular\|MetricasH1" scfv_dsr/epistemologico/generador_propuesta.py`:

    calcular_r(entidades)         →  float
    calcular_o(entidades)         →  float
    calcular_t()                  →  float
    calcular_v(inflacion_anual)   →  float
    MetricasH1(r=, s=, o=, t=, v=)

El grep acotado no muestra la definición correspondiente a `s`, aunque sí
aparece la consolidación en `MetricasH1`. La implementación exacta puede
verificarse leyendo el archivo completo; este informe no afirma su forma.

**H15 · `GeneradorPropuesta` implementa actualmente el cálculo de r,s,o,t,v
que c3 atribuye a Intellectus.**
Superposición funcional observada, no equivalencia arquitectónica. c3 asigna
esos cálculos a Intellectus vía cinco subsistemas (CBR, Ontología, Reglas,
Aprendizaje, Peso). `generador_propuesta.py` realiza los cálculos sin esos
subsistemas. No se afirma que la responsabilidad de Intellectus "viva" en
`generador_propuesta.py`; se registra la coincidencia de firma matemática.

**H16 · `reticulo.py` implementa una estructura de retículo booleano sobre el
universo de cuentas.**
Docstring declara `(P(C), ⊆, ∪, ∩, ¬, △)`. Constructor
`desde_pcu(pcu, clave="marcos")` construye subconjuntos desde el PCU.
Sin dependencias de `xnor` ni `motor`.
En la lectura realizada no se identificó consumidor propio. El único import
identificado de `RetículoCuentas` en el reconocimiento está en
`contable/examinador.py:13` (`from scfv_dsr.contable.reticulo import RetículoCuentas`),
verificado mediante `head -40 scfv_dsr/contable/examinador.py`.
No se afirma integridad matemática ni corrección formal — sólo la estructura
declarada y los elementos visibles en cabecera.

**H17 · `examinador.py` se declara panel, no juez.**
Docstring: `Panel de consulta. No decide. No autoriza. No camino crítico.
Contrato: DOCS/H8P_EXAMINADOR_CONTRATO.md`. Usa `xnor` para
`NATURALEZAS_VALIDAS`, `MOVIMIENTOS_VALIDOS`, `ubicacion_booleana`,
`ubicacion_gf2`, `ubicacion_signos`.
Sin consumidor externo identificado.
Verificación: `grep -rn "Examinador\|examinador" --include="*.py" scfv_dsr/ | grep -v examinador.py`.

**H18 · Los contratos H8P no están en DSR.**
`DOCS/H8P_EXAMINADOR_CONTRATO.md` y `DOCS/H8P_RETICULO_CONTRATO.md` existen
en S0 (`~/scfv_v6/DOCS/`). No existen en `~/scfv-dsr/DOCS/`, que contiene
sólo cuatro entradas: dos actas FASE 2, la auditoría 2026-09-26 y un
directorio `historicos/`.
Verificación: `ls DOCS/`.

**H19 · No se encontraron archivos `test_*.py` que cubran la cadena
epistemológica.**
El comando
`find ~/scfv-dsr -type f -name "test_*.py"` devuelve:

    DOCS/historicos/evaluacion/verificacion/test_soporte_minimo.py
    scfv_dsr/dsl/tests/test_grammar_lalr.py
    scfv_dsr/dsl/tests/test_compatibilidad_s0.py
    scfv_dsr/dsl/tests/test_contract_def.py
    scfv_dsr/dsl/tests/test_invariant_def.py
    scfv_dsr/dsl/tests/test_asiento_declarado_def.py

Ninguno corresponde a `epistemologico/` ni a `contable/examinador|reticulo`.
El comando verifica ausencia bajo el patrón `test_*.py`; no verifica ausencia
de tests con otras convenciones de nombre ni cobertura configurada por otra
vía.

---

## 3 · Mapa de módulos examinados

### 3A · Cadena epistemológica (EVIDENCIA → H₂)

| módulo | ubicación | líneas | consumidor | test | contrato | estado |
|---|---|---|---|---|---|---|
| `evidencia` | `epistemologico/` | ~180 | perceptum, extractor | no test_*.py | npl + c3 | VIVO |
| `models` | `epistemologico/` | ~80 | perceptum, generador, h2 | no test_*.py | c3 | VIVO |
| `perceptum` | `epistemologico/` | 284 | extractor | no test_*.py | c3 | VIVO |
| `generador_propuesta` | `epistemologico/` | ~290 | orquestador | no test_*.py | npl (PROPUESTA) | VIVO |
| `intellectus` | `epistemologico/` | 105 | — | no test_*.py | c3 aspiracional | SIN CONSUMIDOR |
| `dictum` | `epistemologico/` | 71 | — | no test_*.py | npl (DICTUM) | SIN CONSUMIDOR |

### 3B · Componentes contables contiguos examinados

| módulo | ubicación | líneas | consumidor | test | contrato | estado |
|---|---|---|---|---|---|---|
| `examinador` | `contable/` | 85 | — | no test_*.py | H8P (no portado) | SIN CONSUMIDOR · SIN CONTRATO EN DSR |
| `reticulo` | `contable/` | ~110 | sólo examinador | no test_*.py | H8P (no portado) | SIN CONSUMIDOR PROPIO |
| `reportes_motor` | `contable/` | — | no verificado | no test_*.py | ninguno declarado | versión declarada v9 (docstring) |

**Nota.** `reportes_motor` aparece en §7.3 del traspaso por coincidencia de
nombre; su docstring lo identifica como `Motor 9.0.0 — Reportes desde
EventStore`, ajeno a la arquitectura interpretativa v8.1/v8.2 de los
restantes. Su consumidor no fue verificado en este reconocimiento.

Pipeline real en DSR:

    evento
      → extractor
      → Evidencia → Perceptum → ObservacionH1
      → generador_propuesta → PropuestaH1 + MetricasH1(r,s,o,t,v)
      → h2.H2Decision → DecisionProfesional
      → ciclo v8.2 (orquestador)
      → EventStore

Pipeline declarado en npl:

    EVIDENCIA → OBSERVACIÓN (H₁) → PROPUESTA (H₁) → DICTUM (C) → H₂

**Diferencias observadas respecto de la cadena declarada en npl.**
(i) La etapa DICTUM no se ejecuta en el pipeline.
(ii) La etapa Intellectus tampoco participa en el pipeline efectivo: la
implementación calcula r,s,o,t,v en `generador_propuesta.py` y alimenta
directamente a `h2.H2Decision`, sin invocar `intellectus.py`.
(iii) c3 declara componentes (CBR, Ontología, Reglas, Aprendizaje) sin
archivo correspondiente identificado en DSR.

---

## 4 · Fuentes arquitectónicas heterogéneas

Se identificaron tres fuentes que declaran algo sobre la organización de la
cadena. **No son tres declaraciones homogéneas de una misma cadena.**

**D-1 · `npl-definitivo.md:13` (v6.1, 2026-08-30).**
Declaración de secuencia NPL:
`EVIDENCIA → OBSERVACIÓN → PROPUESTA → DICTUM → H₂`. Sin Intellectus.

**D-2 · `c3-componentes.md:213-260` (v8.1, S0).**
Descripción de arquitectura de componentes:
`Perceptum → Intellectus → Dictum`, con Intellectus provisto de cinco
subsistemas que producen r,s,o,t,v. Cuatro componentes adicionales (CBR,
Ontología, Reglas, Aprendizaje) sin archivo correspondiente en DSR.

**D-3 · `generador_propuesta.py:10` (v8.2, DSR).**
Declaración de desacoplamiento en código:
`No depende de Dictum ni H₂`. El generador declara explícitamente su
independencia respecto de Dictum y H₂. Esta declaración entra en tensión con
la secuencia npl que coloca DICTUM antes de H₂.

**Síntesis.** D-1 es una secuencia declarada. D-2 es una arquitectura de
componentes. D-3 es una declaración de desacoplamiento a nivel de módulo. La
ruta operativa observada en código es implícita en `orquestador.py`; este
reconocimiento no le atribuye estatuto canónico.

---

## 5 · Estatuto por módulo

**VIVOS sin archivo test_*.py asociado.**
`evidencia`, `models`, `perceptum`, `generador_propuesta`. Cableados, sin
archivo test_*.py asociado.

**SIN CONSUMIDOR identificado.**
`intellectus`, `dictum`. Port literal v8.1, extensión v8.2 documentada en
journal, sin consumidor identificado en el pipeline.
`examinador` — sin consumidor y sin contrato portado a DSR.
`reticulo` — sin consumidor propio identificado; sólo `examinador` lo importa.

---

## 6 · Deudas formalizadas

**D-EPIST-1 · DICTUM ausente del pipeline.**
La etapa DICTUM(C) declarada en `npl-definitivo.md:13` no se ejecuta en DSR.
`generador_propuesta.py:10` declara la omisión como propiedad. FASE 3 debe
ratificarla, revertirla o reformularla.

**D-EPIST-2 · Intellectus implementa c3 aspiracional mínima.**
El `intellectus.py` de DSR (105 L) evalúa AND/OR sobre dict. No implementa
los cinco subsistemas de c3. Su docstring (`Intérprete
hermenéutico-deconstructivo`) utiliza vocabulario que no aparece en
`npl-definitivo.md` según la búsqueda realizada.

**D-EPIST-3 · c3 declara cinco subsistemas sin archivo correspondiente en DSR.**
CBR Manager, Ontología, Reglas Normativas, Aprendizaje, Peso temporal.
Ninguno tiene archivo identificado en DSR. La firma matemática (r,s,o,t,v)
se calcula en `generador_propuesta.py`.

**D-EPIST-4 · `examinador.py` referencia contrato inexistente en DSR.**
`DOCS/H8P_EXAMINADOR_CONTRATO.md` no está en DSR. Existe en S0.

**D-EPIST-5 · `reticulo.py` sin consumidor propio identificado.**
Sólo `examinador` lo importa.

**D-EPIST-6 · Ausencia de archivos test_*.py en la cadena epistemológica.**
Ni `epistemologico/` ni `contable/examinador|reticulo` tienen archivo con
patrón `test_*.py` en el repo.

**D-EPIST-7 · Fuentes arquitectónicas heterogéneas y no coincidentes.**
npl declara una secuencia; c3 describe componentes distintos; el código de
`generador_propuesta.py` declara un desacoplamiento. La ruta operativa
observada en código es implícita en `orquestador.py`; este reconocimiento no
le atribuye estatuto canónico.

Deudas heredadas de FASE 2 no reabiertas por este reconocimiento:

    D-BALDOR-VC · D-BALDOR-IVA-1 · D-BALDOR-IVA-2 · D-LIVA-LOADER
    D-IVA-PIPELINE · D-DSL-MULTI · D-NUC-1 · suma_montos
    motor.validar_partida_doble sin invocación desde generar_asiento

---

## 7 · Cierre

**Reconocimiento FASE 4 cerrado dentro del alcance definido.**
No quedan, dentro del alcance de esta FASE 4, lecturas pendientes
identificadas que impidan establecer el estatuto material descrito.

**Lo que este reconocimiento no hizo.** No decidió qué hacer con los módulos
sin consumidor identificado. No propuso cablear DICTUM. No propuso retirar
Intellectus. No tocó código. Eso es FASE 3.

**Lo que sí estableció.** Que la premisa "FASE 4 bloqueada por canon" no se
**Lo que sí estableció.** Que la premisa "FASE 4 bloqueada por canon" no se
sostiene contra la evidencia material. Que los nombres citados en §7.3 del
traspaso se encuentran dispersos en DSR, no agrupados. Que Intellectus,
Dictum, Examinador y Reticulo carecen de consumidor identificado, y que las
razones difieren entre ellos (código desconectado, contrato no portado,
arquitectura aspiracional). Que la etapa DICTUM declarada en npl no se
ejecuta en el pipeline real, y que Intellectus tampoco participa en él.

**Pregunta que FASE 3 hereda.** ¿La capa DICTUM (orientación C=f) debe operar
en DSR, o su omisión es decisión arquitectónica válida de v8.2? Las
respuestas legítimas (ratificar, revertir, reformular) requieren acta. El
estado actual, sin declarar, no lo es.

---

*Informe generado en Ventana 8 · FASE 4 reconocimiento · sólo lectura · sin
patch · sin commit · sin modificación de DB.*

*Verificación acumulada: 19 hallazgos · 5 bloques de lectura · 4 correcciones
al traspaso · 7 deudas formalizadas.*
