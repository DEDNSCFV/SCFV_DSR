# ARQUEOLOGÍA DIACRÓNICA · B.2 · INVENTARIO S0
### Auditoría 2026-09-28 · ~/scfv-dsr

---

## 0 · Alcance y método

Segundo bloque de arqueología diacrónica. Sólo lectura. Objetivo: reconstruir
la superficie materializada de S0 y contrastarla con el port DSR, para
determinar el estatuto de los módulos clasificados como huérfanos por FASE 4.

Fuentes leídas:

    ~/scfv_v6/DOCS/journal/
      2026-08-31-bitacora.md            (47 L)
      2026-09-01-evolucion-8.1.md       (33 L)
      2026-09-02-evolucion-8.1-a-8.2.md (137 L)
      bitacora_errores_v8.1.md          (22 L)

    ~/scfv_v6/DOCS/
      H8P_RETICULO_CONTRATO.md
      H8P_EXAMINADOR_CONTRATO.md
      H7H_CIERRE.md
      S0_CIERRE.md
      _EA_HALLAZGOS.md
      arquitectura/c3-componentes.md

    ~/scfv_v6/PODERES/CONTABLE/
      reticulo.py · examinador.py · importador_s0.py

    ~/scfv_v6/TESTS/                    (inventario)

Método: lectura completa de journals y contratos; grep dirigido sobre
huérfanos; verificación cruzada de archivos y tests; conteo de cobertura.

Nota terminológica. Las cifras de tests se refieren a conjuntos distintos:
"208" corresponde al universo ejecutable declarado en S0 según
`S0_CIERRE.md`; "15 DSR" corresponde a los archivos localizados en
`scfv_dsr/dsl/tests/` (7) más los tests externos `~/test_fase1_atomicidad.py`
y `~/test_fase2a_baldor.py` (9). No son conjuntos equivalentes. La
comparación es informativa, no simétrica.

---

## 1 · Timeline de journals

   2026-08-31   reestructuración V7 → V8
                jerarquía por Poderes y Dominios
                ajuste de imports, carga automática de fractales
                corrección de reglas de compras (sin IVA por escalado)

   2026-09-01   evolución v8.0 → v8.1
                H₁ hermenéutico, H₂ fusión de horizontes
                Módulos 1, 2, 4, 5 completados
                proyecciones (normas, decisiones, integridad, resumen)

   2026-09-02   evolución v8.1 → v8.2
                normas versionadas, condicionales, relacionadas
                H4: extensión de Intellectus para AND/OR
                H5: extensión de Dictum para estructura JSON
                FASE 1 · soberanía H₂ (modo_auto False por defecto)

Los tres journals caben en tres días. El sistema se declaró evolucionado
en un sprint corto. Toda la actividad de diseño visible ocurre entre
2026-08-31 y 2026-09-02.

---

## 2 · DAC #10 · principio de especificación ↔ silicio

Cita textual del journal 2026-09-02:

    ## DAC #10 — Rectificación de versión (2026-09-02)
    El SCFV no declara una versión hasta que el silicio la soporta.
    La especificación y el silicio deben estar sincronizados.
    Una discrepancia de versión es una falla de gobernanza. El
    sistema se declara oficialmente en v8.1+ hasta que las
    rectificaciones sean completadas.

Este principio es operativo, no retórico. Declara que el sistema no puede
declararse v8.2 mientras el silicio no lo soporte. Degrada la versión
oficial a v8.1+ hasta que la sincronía se restablezca.

El mismo journal, sección §8 "Declaración Formal", afirma:

    El SCFV ha evolucionado exitosamente de v8.1 a v8.2.
    FLUJO COMPLETO: ✅ Funciona.
    Dictum estructurado: JSON para comunicación programática con H₂.

Ambas declaraciones conviven en el mismo archivo, sin resolución explícita.
Ver §6.

---

## 3 · Familia α · huérfanos reales

Criterio: sin consumidor en el pipeline, sin contrato operativo verificado,
sin tests específicos en S0.

    intellectus
      ubicación DSR:   epistemologico/intellectus.py
      primer commit:   e0923e4 (c0)
      último commit:   ninguno posterior
      journal:         declarado completado en 2026-09-01 y 2026-09-02
      contrato:        c3-componentes.md (aspiracional, no implementado)
      tests S0:        sin test específico localizado
      consumidor DSR:  ninguno

    dictum
      ubicación DSR:   epistemologico/dictum.py
      primer commit:   e0923e4 (c0)
      último commit:   ninguno posterior
      journal:         declarado funcionando en 2026-09-01
      contrato:        npl-definitivo.md:13 (etapa DICTUM)
      tests S0:        sin test específico localizado
      consumidor DSR:  ninguno

    validar_partida_doble
      ubicación DSR:   contable/motor.py:61
      primer commit:   e0923e4 (c0)
      último commit:   ninguno posterior
      journal:         sin mención
      contrato:        sin mención en ningún documento del corpus
      tests S0:        sin test específico localizado
      consumidor DSR:  ninguno

Los tres comparten: nacimiento en c0, ausencia de consumidor, ausencia de
tests específicos, ausencia de registro documental de desconexión.

`validar_partida_doble` es el caso extremo: no aparece en journals, no
aparece en H8P, no aparece en S0_CIERRE, no aparece en H9_GATE. Nace sin
documentación y persiste sin consumidor.

---

## 4 · Familia β · port parcial

Criterio: contrato declarado en S0, tests S0 verdes, ausencia en DSR.
No son huérfanos en S0. Su estatuto en DSR es consecuencia de un port que
no trasladó la superficie completa.

    examinador
      ubicación S0:    PODERES/CONTABLE/examinador.py
      ubicación DSR:   contable/examinador.py (85 L)
      contrato S0:     H8P_EXAMINADOR_CONTRATO.md
      estado S0:       cerrado · E1-E16 · 15/15 activos verdes
      test S0:         TESTS/test_examinador.py (163 L)
      test DSR:        ausente
      nota:            el contrato declara "Panel de consulta. NO autoriza.
                       NO decide. NO se invoca en el camino crítico."
                       Su ausencia del pipeline DSR es conforme al contrato,
                       no violación de él.

    reticulo
      ubicación S0:    PODERES/CONTABLE/reticulo.py
      ubicación DSR:   contable/reticulo.py (3933 B)
      contrato S0:     H8P_RETICULO_CONTRATO.md
      estado S0:       cerrado · F1-F8 · 14/14 tests verdes
      test S0:         TESTS/test_reticulo.py (126 L)
      test DSR:        ausente
      nota:            su consumidor legítimo en S0 es examinador, que es
                       panel. Cadena fuera del pipeline por diseño.

    reportes_motor
      ubicación S0:    PODERES/CONTABLE/reportes_motor.py
      ubicación DSR:   contable/reportes_motor.py
      docstring:       "SCFV Motor 9.0.0 — Reportes desde EventStore"
      test S0:         TESTS/test_reportes_motor.py (59 L)
      test DSR:        ausente
      nota:            FASE 4 lo clasificó "vivo v9". En S0 tiene test.
                       En DSR no hay test portado. La etiqueta "vivo" en
                       FASE 4 se sostenía sobre el docstring, no sobre
                       verificación de consumidor.

    importador_s0
      ubicación S0:    PODERES/CONTABLE/importador_s0.py (321 L)
      ubicación DSR:   ausente
      contrato S0:     S0_CIERRE.md lo lista como código materializado
      estado S0:       cerrado · I1-I14
      test S0:         TESTS/test_importador_s0.py (431 L)
      test DSR:        ausente
      nota:            no mencionado en el informe FASE 4. Es una omisión
                       del port que FASE 4 no registró.

Total de tests S0 específicos de la familia β: 918 líneas distribuidas en
5 archivos.

---

## 5 · Cobertura no portada

Universo declarado en S0 según `S0_CIERRE.md`:

    Suite específica por capa:
      TESTS/test_reticulo.py          Ran 14 — OK
      TESTS/test_examinador.py        Ran 16 — OK (skipped=1)
      TESTS/test_perceptum_lote.py    Ran 10 — OK
      TESTS/test_importador_s0.py     Ran 17 — OK

    Suite global:  Ran 223 tests in 1.821s — OK (skipped=1)

Universo localizado en DSR:

    scfv_dsr/dsl/tests/               5 archivos · 7 tests
    ~/test_fase1_atomicidad.py        externo · 1 test
    ~/test_fase2a_baldor.py           externo · 8 tests

Diferencia: 208 tests declarados en S0 no tienen contraparte en DSR.

El único skip en S0 corresponde a E12 (examinador), aparcado por vacuidad
según su propio contrato.

Formulación del hallazgo. El port DSR no trasladó íntegramente la
superficie materializada de S0: omitió `importador_s0.py` y no trasladó la
suite específica de S0. Esto genera una diferencia de cobertura que
explica parte de las aparentes orfandades identificadas en FASE 4.

Precisión: "208 tests no portados" ≠ "208 tests que necesariamente debían
portarse". La obligación de portar cada test es una pregunta distinta,
dependiente del alcance declarado del port. Esa pregunta queda fuera de
B.2 y pertenece a FASE 3.

---

## 6 · Contradicción interna del journal 2026-09-02

El journal 2026-09-02 contiene dos declaraciones incompatibles sobre el
estado del sistema.

**§8 · Declaración Formal (positiva).**

    El SCFV ha evolucionado exitosamente de v8.1 a v8.2.
    Las siguientes propiedades están demostradas:
    1. Independencia evolutiva.
    2. Separación de poderes.
    3. Normas versionadas.
    4. Condiciones compuestas: AND/OR evaluadas por Intellectus.
    5. Dictum estructurado: JSON para comunicación programática con H₂.
    6. Compatibilidad hacia atrás.
    ## 7. ESTADO ACTUAL DEL SISTEMA
    - FLUJO COMPLETO: ✅ Funciona
    Estado: ✅ v8.2 DECLARADO

**DAC #10 · Rectificación de versión (negativa).**

    El SCFV no declara una versión hasta que el silicio la soporta.
    Una discrepancia de versión es una falla de gobernanza.
    El sistema se declara oficialmente en v8.1+ hasta que las
    rectificaciones sean completadas.

Ambas están en el mismo documento. §8 declara v8.2 operativo. DAC #10
degrada a v8.1+ por falta de sincronía silicio-especificación.

En DSR hoy, los elementos que §8 declara operativos presentan estados
distintos:

    Dictum comunica con H₂ (§8.5)      → sin consumidor en DSR
    FLUJO COMPLETO funciona (§7)        → Dictum no participa
    Intellectus evalúa AND/OR (§8.4)    → sin consumidor en DSR

La contradicción no está resuelta. DAC #10 es el mecanismo que el propio
sistema se dio para resolverla, pero no fue aplicado al port.

---

## 7 · Reinterpretación de FASE 4

La secuencia documental es:

    FASE 4 · clasificación preliminar
        ↓
    B.1    · arqueología diacrónica DSR
        ↓
    B.2    · arqueología diacrónica S0
        ↓
    reclasificación α / β

FASE 4 no se reescribe. Se registra que B.2 modifica la interpretación que
podía hacerse de sus hallazgos.

Reclasificación:

    clasificación FASE 4                 reclasificación B.2
    ──────────────────────────────────────────────────────────────
    H2   perceptum huérfano            sin cambio
    H9   examinador                   β · port parcial
    H10  dictum                       α · huérfano real
    H10  intellectus                  α · huérfano real
    H10  examinador                   β · port parcial
    H10  reticulo                     β · port parcial
    H10.b reportes_motor "vivo v9"    β · port parcial (test S0 no portado)
    H16  reticulo sin consumidor      β · port parcial
    H17  examinador sin contrato      contrato sí existe en S0 ·
                                      no portado
    D-EPIST-1 DICTUM ausente          sin cambio (α)
    D-EPIST-2 Intellectus mínimo      sin cambio (α)
    D-EPIST-4 contrato no portado     β · port parcial
    D-EPIST-5 reticulo sin consumidor β · port parcial

Correcciones puntuales:

    · "huérfano doble" para examinador es impreciso. Tenía contrato en S0
      y test verde. Su ausencia en el pipeline es conforme a su contrato
      (panel, no camino crítico).

    · "vivo v9" para reportes_motor se sostenía sobre el docstring, no
      sobre verificación. En S0 tiene test. En DSR no.

    · importador_s0.py no fue mencionado en FASE 4. Es una omisión del
      port registrada en B.2.

    · Los 918 L de tests S0 específicos de familia β no fueron registrados
      en FASE 4.

Limitación compartida de B.1 y B.2. La ausencia de historia Git posterior
en ambos repositorios (DSR: commits post-c0 sin cambios estructurales;
S0: un solo commit) limita la arqueología diacrónica basada en Git y obliga
a complementar la reconstrucción mediante journals, documentación,
snapshots `.bak` y artefactos de cierre. No se establece relación causal
entre ambas ausencias; se registra una limitación común de método.

---

*Bloque B.2 · sólo lectura · sin patch · sin modificación de código.*
*Falsado por IA-2 · alcance reformulado antes de redacción.*
