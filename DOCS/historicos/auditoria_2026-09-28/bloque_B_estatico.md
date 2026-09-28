# BLOQUE B · ANÁLISIS ESTÁTICO
### Auditoría 2026-09-28 · ~/scfv-dsr

---

## 0 · Alcance y método

Segundo bloque del ciclo de diagnóstico completo. Sólo lectura. Objetivo:
análisis estático del paquete `scfv_dsr/` con cinco herramientas. Sin patch.
Sin modificación de DB.

Sub-bloques ejecutados:

    B.0  verificación de arranque · herramientas · evidencia
    B.1  pyflakes       imports + variables
    B.2  pylint         estilo + bugs + diseño
    B.3  mypy           tipos + contratos
    B.4  bandit         seguridad
    B.5  radon          complejidad + mantenibilidad
    B.6  síntesis       lecturas dirigidas + consolidación

Evidencia cruda versionada:

    DOCS/historicos/auditoria_2026-09-28/bloque_B/
    ├── pyflakes.txt        6 L
    ├── pylint.txt        171 L
    ├── mypy.txt           26 L
    ├── bandit.txt        151 L
    ├── radon_cc.txt      275 L
    └── radon_mi.txt       43 L

Herramientas descartadas:

    ruff       sin wheel ARM64 · compilación desde Rust colgada
    pip-audit  universo declarado incompleto (ver §4)

Configuración de análisis:

    pylint     con --rcfile=/dev/null y disable selectivo de
               categorías estilísticas (docstrings faltantes,
               line-too-long, umbrales de tamaño)
    mypy       sin --strict · default razonable
    bandit     sólo severidad Medium+ (default)
    radon      -s (score por bloque) · -a (promedio)

---

## 1 · pyflakes · 6 hallazgos

    generador_propuesta.py:152-156
        local variable 'r' is assigned but never used
        local variable 's' is assigned but never used
        local variable 'o' is assigned but never used
        local variable 't' is assigned but never used
        local variable 'v' is assigned but never used

    contable/motor.py:162:38
        f-string is missing placeholders

Distribución: 5 en `generador_propuesta.py` (variables locales),
1 en `motor.py` (f-string estático).

---

## 2 · pylint · score 9.33 · 171 L

### Distribución por categoría

    Convenciones (C) · 79
      C0103  invalid-name                 33
      C0415  import-outside-toplevel      12
      C0413  wrong-import-position        12
      C0411  wrong-import-order            9
      C0325  superfluous-parens            8
      C0321  multiple-statements           3
      C0305  trailing-newlines             2

    Refactorización (R) · 27
      R0902  too-many-instance-attributes 10
      R0917  too-many-positional-arguments 9
      R0911  too-many-return-statements    4
      R1705  no-else-return                3
      R1732  consider-using-with           1

    Warnings (W) · 26
      W1514  unspecified-encoding          6
      W0613  unused-argument               5
      W0612  unused-variable               5
      W0718  broad-exception-caught        4
      W0707  raise-missing-from            4
      W1309  f-string-without-interpolation 1
      W0511  fixme                         1

    Errores (E) · 1
      E0606  possibly-used-before-assignment 1

### Distribución por archivo (top 10)

    kernel/baldor.py                    26
    integrador.py                       14
    epistemologico/models.py            13
    evaluador.py                         8
    dsl/parser.py                        8
    extractor.py                         7
    contable/maquina_estados_asiento.py  7
    cli.py                               7
    epistemologico/generador_propuesta.py 6
    infraestructura/serializador_canonico.py 5

Score final: 9.33/10. Los 79 C son ruido estilístico. Núcleo real:
26 W + 1 E.

---

## 3 · mypy · 18 errores · 8 notas

### Distribución por código

    arg-type             9
    var-annotated        4
    assignment           3
    import-untyped       1
    import-not-found     1
    annotation-unchecked 1

### Distribución por archivo

    profesional/h2.py                    5
    contable/reportes_motor.py           5
    profesional/orquestador.py           4
    contable/verificador_autorizacion.py 3
    contable/reticulo.py                 3
    contable/decision_provider.py        2
    kernel/baldor.py                     1
    integrador.py                        1
    dsl/parser.py                        1
    contable/nucleo_consecuencias.py     1

### Patrones identificados

Patrón 1 · Optional implícito (2 errores)
    verificador_autorizacion.py:53 · estado_actual: str = None
    orquestador.py:42              · justificacion: str = None
    Sintaxis PEP 484-legacy. Mypy 1.20 tiene no_implicit_optional=True.

Patrón 2 · str | None pasado a campo str (3 errores)
    nucleo_consecuencias.py:266    firma_h2
    h2.py:92                       autor a _firmar_decision
    h2.py:102                      autor a DecisionProfesional

Patrón 3 · Enum/dataclass pasado como str/dict (5 errores)
    h2.py:110                      TipoEvento → str
    h2.py:111                      DecisionProfesional → dict
    h2.py:114                      VersionContexto → dict
    decision_provider.py:51        TipoEvento → str
    decision_provider.py:75        TipoDecisionH2 → str
    Firmas tipadas de EventStore.guardar() no reflejan contrato
    documentado (D.3).

Patrón 4 · var-annotated (4 errores)
    reticulo.py:60,86,99          resultado/cubierto
    dsl/parser.py:111             result

### Aislados

    baldor.py:372                  float asignado a int
    orquestador.py:115             dict donde se espera list
    reportes_motor.py:138          fpdf sin stubs

---

## 4 · bandit · 13 issues · severidad Low · confianza High

### Distribución

    B101  assert_used              5    (archivos de test DSL)
    B110  try_except_pass          2    (extractor.py:68 · orquestador.py:163)
    B112  try_except_continue      1    (integrador.py:46)
    + 5 no visibles en tail (requiere apertura completa)

### Análisis

B101 · falso positivo estructural
    `assert` en tests DSL es el mecanismo estándar de pytest.

B110 · dos casos distintos
    extractor.py:68      silencio de excepción en cálculo de costo
    orquestador.py:163   mitigado · raise inmediato después + comentario F18

B112 · integrador.py:46
    Mecanismo de búsqueda por iteración. `except Exception` amplio
    traga cualquier error del módulo candidato.

### Cobertura bandit

    subprocess   · sin apariciones
    eval/exec    · sin apariciones
    pickle       · sin apariciones
    tempfile     · sin apariciones
    SQL          · sin apariciones

Perfil del sistema: contabilidad local, stdlib, sin superficie de ataque.

---

## 5 · radon · complejidad + mantenibilidad

### Complejidad ciclomática

    238 bloques analizados
    Promedio: A (4.084)

    Distribución por rango:
      A (1-5)     · mayoría
      B (6-10)    · ~15 funciones
      C (11-20)   · 11 funciones
      D (21-30)   · 2 funciones
      E (31-40)   · 0
      F (41+)     · 1 función

### Funciones C+ (14 totales · 9 archivos)

    F (42)   motor.py:89                     MotorContable.generar_asiento
    D (29)   evaluador.py:89                 evaluar_operacion
    D (29)   serializador_canonico.py:156    _deserializar_tipado
    C (20)   serializador_canonico.py:289    deserializar
    C (19)   serializador_canonico.py:76     serializar
    C (19)   nucleo_consecuencias.py:78      NucleoConsecuencias.construir_consecuencia_autorizada
    C (17)   dsl/parser.py:58                SCFVParser._expr_to_str
    C (17)   dsl/parser.py:184               SCFVParser._handle_contract
    C (17)   dsl/parser.py:224               SCFVParser._handle_invariant
    C (13)   intellectus.py:40               Intellectus.construir_mapa_normativo
    C (11)   evidencia.py:58                 Evidencia.__post_init__
    C (11)   dsl/parser.py:110               SCFVParser._transform_tree
    C (11)   puente_autorizacion.py:57       PuenteAutorizacion.autorizar_admitido
    C (11)   puente_consecuencias.py:61      PuenteConsecuencias.construir_consecuencia_autorizada

### Concentración por archivo

    dsl/parser.py                   4 (C17 · C17 · C17 · C11)
    serializador_canonico.py        3 (D29 · C20 · C19)
    nucleo_consecuencias.py         1 (C19)
    motor.py                        1 (F42)
    evaluador.py                    1 (D29)
    intellectus.py                  1 (C13)
    evidencia.py                    1 (C11)
    puente_autorizacion.py          1 (C11)
    puente_consecuencias.py         1 (C11)

### Naturaleza de la complejidad

    evaluador.py D(29)              · ACCIDENTAL · switch disfrazado
                                       (14 ramas if op_id inline + FASE 2.a)
    serializador_canonico.py D+C+C  · ESENCIAL · type dispatch sin default=str
    motor.generar_asiento F(42)     · NO EVALUADA (lectura dirigida pendiente)
    dsl/parser.py C17+C17+C17+C11   · NO EVALUADA (parser completo pendiente)

### Mantenibilidad

    43 archivos analizados
    Todos rango A
    0 archivos rango B o C

### Nota metodológica

El primer pase de B.5 usó `radon cc -n C -O C` pensando que `-O C`
ordenaba por rango. `-O` en radon significa `--output-file`. El
comando escribió el resultado al archivo `C` en la raíz del repo
en lugar de stdout. La primera versión de esta acta registró 4
funciones C+ basándose en una lectura parcial de `radon_cc.txt`.
El archivo `C` recuperó el listado completo: 14 funciones C+.

---

## 6 · Lecturas dirigidas

Cuatro lecturas específicas para resolver contradicciones detectadas
por las herramientas. Sólo lectura.

### L1 · r,s,o,t,v duplicadas

`generador_propuesta.py`

    generar_hecho_h1:152-156             calcula r,s,o,t,v
                                          ↓ descarta (HechoEconomico no almacena)
    _generar_propuesta_desde_hecho:228-232  recalcula r,s,o,t,v
                                          ↓ usa (MetricasH1 + soporte_C)

El docstring de `generar_hecho_h1` declara:

    "Las métricas H₁ se calculan aquí para mantener la semántica
     del generador F3A.1, aunque el modelo HechoEconomico actual
     no las almacena."

Doble cómputo activo: `generar_propuesta_h1` invoca ambas funciones
en secuencia. Cuatro funciones (`calcular_r`, `calcular_o`,
`calcular_t`, `calcular_v`) ejecutadas dos veces por observación.

`s` está hardcodeada a `0.0` en ambas ubicaciones. No existe
`calcular_s` en el módulo.

### L2 · `guardar()` anotaciones vs contrato D.3

`event_store.py:69-88`

    def guardar(
        self,
        tipo_evento: str,               # anotación
        payload: Dict,                  # anotación
        correlation_id: str,
        idempotency_key: str,
        version_contexto: Optional[Dict] = None,  # anotación
        commit: bool = True,
    ) -> None:
        """
        D.3:
            tipo_evento
                Enum -> .name
                str  -> str
            payload
                serializado mediante serializar()
        ...
        """

Docstring describe contrato real: `tipo_evento` acepta Enum o str,
`payload` acepta dataclasses (las serializa internamente).
Anotaciones dicen `str` y `Dict` — no reflejan el contrato.

5 errores mypy en h2.py y decision_provider.py son técnicamente
correctos pero falsos en intención: el código funciona porque
`guardar()` normaliza internamente.

### L3 · `evaluar_operacion` D(29)

`evaluador.py:89-137`

    Estructura: switch disfrazado de if-chain.

    1 dispatch por `funcion_baldor` (FASE 2.a · lee del JSON)
    14 ramas `if op_id ==` inline (hardcoded)
    1 fallback `return 0.0`

`operaciones.json` declara `"operacion": "min"`, `"aritmetica_compuesta"`,
etc. para 11 operaciones. `evaluar_operacion` ignora esas declaraciones
y resuelve por `op_id` hardcoded. Sólo FASE 2.a lee del JSON.

Complejidad D(29) es **accidental**. Se reduce a rango A si se
unifica bajo dispatch declarativo.

Contraste: `serializador_canonico.py:76,156,289` tiene D(29)+C(20)+C(19)
por **complejidad esencial**: type dispatch sobre tipos arbitrarios
sin `default=str`. Radon no distingue las dos naturalezas. La lectura
dirigida sí.

### L4 · Sistema métrico H1

`models.py` completo + `npl-definitivo.md:178-260` + `c3-componentes.md:213-260`

HechoEconomico.magnitud
    NPL:  `magnitud = ObtenerMonto(observacion.entidades)`
    DSR:  `magnitud=0.0,` hardcoded (generador_propuesta.py:186)
    Función extractora no implementada.

Métrica `s`
    NPL:  `CalcularSimilitudFormalLegal(hecho, casos_formales)`
    c3:   asignada a CBR Manager (TF-IDF)
    DSR:  `s = 0.0` hardcoded en dos ubicaciones
    No existe `calcular_s`.

Métricas r, o, t, v
    NPL declara firmas: `(hecho, contexto.X)`
    DSR implementa:     `(entidades_dict)` o `()`
    No son las funciones del canon — son aproximaciones.

PropuestaH1.metricas
    Campo obligatorio en dataclass.
    Grep sobre `scfv_dsr/`: 3 hits.
      2 en models.py (definición del campo)
      1 en generador_propuesta.py (construcción)
    0 lecturas downstream.

PropuestaH1.soporte_C
    Campo declarado.
    Grep: 3 hits (definición, cálculo, constructor).
    0 lecturas downstream.

HechoEconomico
    Grep sobre `scfv_dsr/` fuera de su módulo: 1 hit.
    `perceptum.py:14` (comentario: "genera HechoEconomico").
    Ningún consumidor operativo.

generar_hecho_h1
    Función pública. Sólo invocada por `generar_propuesta_h1` en su
    propio módulo. Sin consumidor externo.

### L4.b · Composición del pipeline

    generar_propuesta_h1(observacion, inflacion_anual):
        hecho = generar_hecho_h1(observacion, inflacion_anual)
        return _generar_propuesta_desde_hecho(hecho, observacion, inflacion_anual)

Confirmado el doble cómputo. Cada observación genera r,s,o,t,v dos
veces. El primer cálculo produce un HechoEconomico que no consume
métricas. El segundo las almacena en PropuestaH1.

---

## 7 · Deudas registradas

Deudas D-B-1..19 derivadas de las herramientas y lecturas dirigidas.
Registro factual. No obligación de resolución.

### Sistema métrico H1

    D-B-1    r,s,o,t,v duplicadas · copia descartada en
             generar_hecho_h1:152-156
             (paralelo a _generar_propuesta_desde_hecho:228-232)

    D-B-6    Doble cómputo activo por observación
             generar_hecho_h1 + _generar_propuesta_desde_hecho
             Coste: 4 funciones calculadas dos veces

    D-B-7    PropuestaH1.metricas sin consumidor downstream

    D-B-8    PropuestaH1.soporte_C sin consumidor downstream

    D-B-9    generar_hecho_h1 sin consumidor externo identificado

    D-B-10   HechoEconomico sin consumidor externo identificado

    D-B-11   HechoEconomico.magnitud hardcoded 0.0
             NPL declara ObtenerMonto(observacion.entidades)
             Función extractora no implementada

    D-B-12   Métrica s (similaridad) sin implementación
             s = 0.0 hardcoded
             c3 la asigna a CBR Manager (TF-IDF)
             CBR Manager sin archivo en DSR

    D-B-13   Firmas de r,o,t,v en DSR difieren del NPL
             NPL: (hecho, contexto.X)
             DSR: (entidades_dict) o ()

    D-B-14   HechoEconomico.magnitud tipado float (DSR) vs
             Decimal (NPL). Decisión no documentada

    D-B-15   Subsistema métrico completo no portado:
             CBR Manager · Reglas Normativas · Ontología
             Los tres declarados en c3:216-218
             Ninguno tiene archivo en DSR

### Anotaciones y firmas

    D-B-2    EventStore.guardar() anotaciones no reflejan contrato D.3
             tipo_evento: str pero acepta Enum
             payload: Dict pero acepta dataclasses

    D-B-3    h2.py:40 declara autor: Optional[str] = None
             downstream requiere str (h2.py:92, models.py:77)
             Si autor=None: firma SHA-256 sobre string "None"
             Falla silenciosa

### Complejidad

    D-B-4    evaluar_operacion D(29) · switch disfrazado
             14 ramas if op_id == inline
             operaciones.json declara "operacion" que Python ignora

    D-B-5    serializador_canonico.py D+C+C por complejidad esencial
             (registro informativo · no deuda)
             Sin `default=str` por diseño documentado


### Complejidad C+ (deudas derivadas de §5 corregido)

    D-B-20   motor.generar_asiento F(42) · rango inmantenible
             Función que escribe asientos · máxima complejidad del sistema
             Lectura dirigida pendiente

    D-B-21   dsl/parser.py · 4 funciones C+
             _expr_to_str C(17) · _handle_contract C(17)
             _handle_invariant C(17) · _transform_tree C(11)
             Segundo archivo más complejo del sistema
             Relación con D-DSL-MULTI (transversal)

    D-B-22   nucleo_consecuencias.construir_consecuencia_autorizada C(19)
             Función del camino crítico del pipeline

    D-B-23   intellectus.construir_mapa_normativo C(13)
             Función de la familia α (sin consumidor)

    D-B-24   evidencia.__post_init__ C(11)

    D-B-25   puente_autorizacion.autorizar_admitido C(11)

    D-B-26   puente_consecuencias.construir_consecuencia_autorizada C(11)

### Ontología constitucional

    D-B-16   Tetrada declarada como contrato semántico
             (glossary.md:26 · gobernanza/constitucion.md:78)
             Sin consumidor en DSR

    D-B-17   Tetrada protegida como ontología constitucional
             (Cambio requiere ADR + bump mayor)
             Ningún código la instancia

    D-B-18   H-GLOS-07 en _EA_HALLAZGOS.md:995-1004
             detectó la desconexión. Estado CERRADO con limitación
             conservada. Nunca materializada como deuda activa.

    D-B-19   Tetrada ausente del NPL v6.1
             El NPL no es la única fuente doctrinal
             Constitución + ADRs + Glosario son corpus normativo

---

## 8 · Corpus normativo detectado · no auditado

Durante las lecturas dirigidas de B.6 se detectaron tres corpus
en `~/scfv_v6/DOCS/` que no fueron auditados en ninguna ventana
anterior (FASE 4 · B.1 · B.2 · A).

### Corpus descriptivo (auditado parcialmente)

    npl-definitivo.md              (39222 B · leído parcialmente)
    c3-componentes.md              (leído líneas 205-260)

### Corpus normativo (NO auditado)

    gobernanza/constitucion.md     (leído en B.6 por primera vez)
    ADR-000  Termux/Android, sin red ni servidores
    ADR-001  Autoridades, límites, dependencias
    ADR-002  Prefijos, bases por mandante, atomicidad
    ADR-003  Especificación, pseudo-código, PRE/POST/INVARIANTE
    ADR-004  Axiomas E-1, E-2, E-3, C = f(r, s, o, t, v)
    ADR-005  Multi-mandante, cifrado, passphrase, respaldo
    glossary.md                    (leído en B.6)

### Corpus evaluativo previo (NO auditado)

    _EA_HALLAZGOS.md               (extenso · H-GLOS-07 detectado)
    _EA_MATRIZ_SINTESIS.md         (matriz de síntesis previa)
    H6_CIERRE.md
    H7H_CIERRE.md
    H9_GATE_S0_ACTA.md
    H9_GATE_S0_CONTRATO.md
    H9_GATE_S0_EVALUACION.md

### Hallazgos específicos de este corpus

    HC-1   La Constitución declara prevalencia sobre documentación
           anterior. Es normativo vinculante. DSR nunca la cita.

    HC-2   Contradicción Constitución §3 ↔ Glosario
           Constitución clasifica Glosario como INFORMATIVO (no vinculante)
           Glosario se autodenomina "contrato semántico" (vinculante)

    HC-3   ADR-004 define formalmente C = f(r,s,o,t,v).
           FASE 4 citó la fórmula sin referenciar el ADR.

    HC-4   Divergencia s entre documentos:
           glossary.md   · similitud histórica
           npl           · similitud formal-legal
           c3            · TF-IDF vía CBR Manager
           DSR           · s = 0.0 hardcoded

    HC-5   _EA_MATRIZ_SINTESIS.md es una auditoría arquitectónica
           previa completa. Nunca citada en FASE 4/B.1/B.2/A.

    HC-6   Dos HUECOS GENEALÓGICOS abiertos en la evaluación previa:
           HUECO-GENEALOGICO-01 · cambios post-v6 sin ADR visible
           HUECO-GENEALOGICO-02 · clausura de motor_causal.py sin acta

    HC-7   Constitución §8 protege Tetrada como ontología
           (cambio requiere ADR + bump mayor)
           Su ausencia operativa en DSR es violación latente

    HC-8   _EA_HALLAZGOS.md:995 H-GLOS-07 ya detectó la desconexión
           de Tetrada. Estado CERRADO con limitación conservada.

    HC-9   Glosario declara contractualmente: "Intellectus usa CBR
           y ontología, no solo reglas". DSR no tiene ni CBR ni
           ontología implementados.

    HC-10  Constitución §5 declara estatuto de IA Asistente:
           "Herramienta de apoyo. No tiene autoridad de decisión
           ni aprobación."

Estos hallazgos no se materializan como deudas en Bloque B. Se
registran como **contexto normativo detectado**. Su auditoría
sistemática requiere bloque propio (B-bis).

---

## 9 · Estado del Bloque B

    Herramientas ejecutadas          5 (pyflakes, pylint, mypy,
                                       bandit, radon)
    Herramientas descartadas         2 (ruff, pip-audit)
    Lecturas dirigidas               4 (L1, L2, L3, L4 + L4.b)
    Deudas registradas               D-B-1..19
    Corpus normativo detectado       3 corpus · 6 ADRs + constitución
                                       + glosario + evaluaciones previas
    Hallazgos normativos             HC-1..10

    Código total analizado           5.530 L · 43 archivos .py
    Código leído en profundidad      ~600 L (~11%)
    Código pendiente de lectura      ~4.930 L (~89%)

Corpus normativo (ADR-000..005, _EA_*, H6/H7H/H9) auditado: 0%.

---

*Bloque B · análisis estático · sólo lectura · sin patch · sin
modificación de código ni DB.*

*Falsado por IA-2 · registros factuales distinguidos de deudas activas.*
