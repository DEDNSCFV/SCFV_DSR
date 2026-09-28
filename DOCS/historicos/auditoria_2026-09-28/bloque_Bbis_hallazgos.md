# Bloque B-bis · Hallazgos consolidados

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** B-bis.0..3 (25 archivos · 6864 L).
**Naturaleza:** catálogo de fichas de hallazgo. No es matriz. No es cuaderno. Es consolidación.

---

## §0 · Método

Cada hallazgo se registra con: ID · origen (bloque B-bis) · categoría · descripción · deuda asociada.

Vocabulario de categoría: CONTRACT · IMPLEMENTATION · EVIDENCE · HYPOTHESIS · FALSATION · VALIDATION · DESIGN DECISION · VERDICT.

Categorías especiales de B-bis:
- `ERROR-TRASPASO` · error del traspaso Ventana 10 descubierto en B-bis
- `REENCUADRE` · hallazgo Ventana 10 reinterpretado a la luz de B-bis
- `AUTORRECONOCIDO` · hallazgo que el propio corpus ya declaraba

---

## §1 · B-bis.0 · Verificación de arranque

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB0-1 | EVIDENCE | Corpus doctrinal sub-declarado · 86 entradas en `~/scfv_v6/DOCS/` vs 7 declaradas en traspaso | D-BB-1 |
| H-BB0-2 | EVIDENCE | Versionado por copia de archivo · 51 `.bak_*` en `~/scfv_v6/DOCS/` | D-BB-3 |
| H-BB0-3 | EVIDENCE | Truncamiento del `ls` a 40 líneas cortó archivos lowercase | — |
| H-BB0-4 | EVIDENCE | `GIRO_02/` contiene sólo `PROTOCOLO.md` | D-BB-30 |
| H-BB0-5 | EVIDENCE | `scfv-dsr` y `scfv_v6` son dos repos git separados · relación no declarada | D-BB-24 |

---

## §2 · B-bis.1 · ADRs 000-005

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB1-1 | EVIDENCE | `scfv_v6` desincronizado · ahead 1 / behind 3 respecto a origin/main | D-BB-1 |
| H-BB1-2 | EVIDENCE | Working tree `scfv_v6` con 155 entradas modificadas/eliminadas | D-BB-1 |
| H-BB1-3 | EVIDENCE | ADRs no tracked por git · sólo archivos en disco | D-BB-2 |
| H-BB1-4 | EVIDENCE | `.bak_*` no tracked · ruido del working tree | D-BB-3 |
| H-BB1-5 | EVIDENCE | Historia de `scfv_v6` comprimida · sólo 1 commit en log reciente | — |

**Hallazgos ADR (HC-BB):**

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| HC-BB-1 | CONTRACT | ADRs declaran lo que DSR no implementa · corpus doctrinal sin efecto en código | — |
| HC-BB-2 | CONTRACT | Discrepancia ADR-000 ↔ ADR-005 sobre cifrado · supersesión parcial no documentada | D-BB-4 |
| HC-BB-3 | CONTRACT | Pruebas 5–39 citadas por ADRs sin ubicación declarada ni implementación verificada | D-BB-5 |
| HC-BB-4 | HYPOTHESIS | `motor_causal.py` eliminado sin acta · incompatible con ADR-001 (4 autoridades) | D-BB-24 |
| HC-BB-5 | EVIDENCE | Tríada desalineada · ADR-000 pypdf/pillow · pyproject lark · código fpdf | D-BB-6 |
| HC-BB-6 | CONTRACT | ADR-005 exige selección de mandante + passphrase · no reportado en DSR | D-BB-35 |

---

## §3 · B-bis.2 · Corpus evaluativo previo

### §3.1 · H6/H7B/H7H (638 L)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB2-1 | CONTRACT | DSL periférico respecto a ruta canónica · contradicción con ADRs | D-BB-8 |
| H-BB2-2 | EVIDENCE | `scfv_validator.py` produce métrica sobre lista vacía · falso verde | D-BB-9 |
| H-BB2-3 | EVIDENCE | PCU descentralizado · 5 copias divergentes · cuenta `110101` no única | D-BB-10 |
| H-BB2-4 | EVIDENCE | `PODERES/` sin versionar (H5.7-FINDING-GIT-001) | D-BB-11 |
| H-BB2-5 | CONTRACT | Legacy y canónica cohabitan sin plan de convergencia declarado | D-BB-12 |
| H-BB2-6 | CONTRACT | "Tétrada epistemológica de H1 no operacionalizable" declarado explícitamente | D-BB-68 |
| H-BB2-7 | EVIDENCE | `H7B_MATRIZ.md` es documento híbrido (abierto + CLOSED) | D-BB-16 |
| H-BB2-8 | EVIDENCE | Duplicación textual H7B ↔ H7H · secciones B–G idénticas | D-BB-16 |
| H-BB2-9 | EVIDENCE | H7h Fases 1–7 sin archivo ni evidencia · memoria declarada | D-BB-16 |
| H-BB2-10 | EVIDENCE | H7c–H7g nunca abiertos como programa | D-BB-17 |
| H-BB2-11 | EVIDENCE | Rename S0 → SCFV Motor declarado, ambos nombres coexisten | D-BB-17 |
| H-BB2-12 | EVIDENCE | "Clausura de procesadores" sin detalle · término huérfano | — |

### §3.2 · H8P × 3 (911 L)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB2-13 | EVIDENCE | D.5 citada como heredada de H7H pero ausente en H7H leído | D-BB-21 |
| H-BB2-14 | CONTRACT | Cuatro marcas de versión concurrentes (v6 · v8.2 · 9.0.0 · v6.3) sin ADR de transición | D-BB-22 |
| H-BB2-15 | EVIDENCE | `H8P_RETICULO_CONTRATO.md` es documento híbrido ("borrador" + "operativo") | D-BB-16 |
| H-BB2-16 | EVIDENCE | Componentes canónicos no mapeados (Adquisidor, Perceptum, PropuestaH1, ConsecuenciaAutorizada, NucleoConsecuencias) | D-BB-19 |
| H-BB2-17 | EVIDENCE | Numeración de invariantes Motor (I2, I6, I7) sin catálogo visible | D-BB-20 |
| H-BB2-18 | CONTRACT | Referencia doctrinal externa "Contreras" sin cita verificable | D-BB-18 |
| H-BB2-19 | EVIDENCE | Suite 223 tests en `~/scfv_v6/TESTS/` no reflejada en traspaso | D-BB-23 |

### §3.3 · H9 × 3 + S0_CIERRE (1088 L)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB2-20 | EVIDENCE | `SCFV_MOTOR_CIERRE.md` citado 4+ veces · nunca leído | D-BB-24 |
| H-BB2-21 | CONTRACT | Colisión de nomenclatura I-números (Motor vs Importador vs Perceptum) | D-BB-26 |
| H-BB2-22 | DESIGN DECISION | Régimen tripartito (IA-1 + IA-2 + Operador) introducido sin ADR | D-BB-27 |
| H-BB2-23 | EVIDENCE | `Perceptum` no caracterizado en ningún contrato | D-BB-28 |
| H-BB2-24 | EVIDENCE | HL-42 y `BITACORA_GIRO_02.md` · hallazgo documental abierto | D-BB-25 |
| H-BB2-25 | EVIDENCE | Proliferación de 6 "actas" o "cierres" sin jerarquía explícita | — |
| H-BB2-26 | CONTRACT | "Giro 01/02" sin definición en corpus doctrinal | D-BB-30 |
| H-BB2-27 | CONTRACT | Nomenclatura IA-1/IA-2/IA-3 difiere entre régimen ventana y doctrinal | D-BB-31 |
| H-BB2-28 | EVIDENCE | Trazabilidad de conteo de tests (196→223→225) ejemplar y verificable | — |
| H-BB2-29 | EVIDENCE | 11 días de actividad (17→28 sep) fuera del corpus doctrinal leído | D-BB-32 |
| H-BB2-33 | EVIDENCE | `MotorContable(None)` tratado asimétricamente en H9_EVALUACION vs S0_CIERRE | D-BB-33 |

### §3.4 · _EA_HALLAZGOS (1222 L)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB2-30 | EVIDENCE | Bloques K-L-M del cuaderno ausentes en disco | D-BB-36 |
| H-BB2-31 | EVIDENCE | NPL es v6.1, no v6 · introduce 5ª marca de versión | D-BB-22 |
| H-BB2-32 | CONTRACT | NPL especifica event_store embebido vs migración 002 separada | D-BB-34 |
| H-BB2-33 | CONTRACT | NPL sin SQLCipher · contradicción directa con ADR-005 | D-BB-35 |
| H-BB2-34 | CONTRACT | Motor Causal + Motor Booleano separados en NPL · hoy fusionados sin acta | — |
| H-BB2-35 | EVIDENCE | Migración 007 · 1 de 4 tablas epistemic · contradice ADR-004 | D-BB-43 |
| H-BB2-36 | EVIDENCE | `seguridad/__init__.py` vacío con `test_cifrado` verde · falso verde | D-BB-41 |
| H-BB2-37 | EVIDENCE | 5 pares de hash SHA-256 idénticos pre/post | D-BB-40 |
| H-BB2-38 | EVIDENCE | `LIVA_Art4.json` duplicado literal | D-BB-40 |
| H-BB2-39 | EVIDENCE | Bloque R introduce "Giro 03" · numeración HL-NNN paralela | D-BB-38, D-BB-39 |
| H-BB2-40 | EVIDENCE | Defecto numérico IVA cuantificado · factor 10⁸ | H-DEUA13-01 |
| H-BB2-41 | EVIDENCE | `ACTAS/` directorio nuevo no mapeado | D-BB-37 |
| H-BB2-42 | EVIDENCE | Cuaderno declara PENDIENTE tras PASS del Gate | D-BB-45 |
| H-BB2-43 | EVIDENCE | Suite 21 componentes no mapeados en C3 | D-BB-42 |

### §3.5 · _EA_MATRIZ_SINTESIS (1021 L)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB2-44 | EVIDENCE | La matriz de síntesis ya existe · duplica trabajo planificado de B-bis.4 | — |
| H-BB2-45 | EVIDENCE | La matriz es anterior al acta del Gate S0 | D-BB-47 |
| H-BB2-46 | EVIDENCE | La matriz es anterior al Bloque R del cuaderno | D-BB-48 |
| H-BB2-47 | EVIDENCE | Bloques K-L-M del cuaderno no aparecen tampoco en la matriz | D-BB-36 |
| H-BB2-48 | EVIDENCE | Cifra "111 filas en 12 bloques" (o 13) · inconsistencia interna | D-BB-49 |
| H-BB2-49 | EVIDENCE | "Fase 3 cerrada" contradice hallazgos posteriores | D-BB-47 |
| H-BB2-50 | DESIGN DECISION | Regla 4 de admisión · reutilización legítima de H-XXX entre bloques | — |
| H-BB2-51 | EVIDENCE | HUECO-GENEALOGICO-03/04/05 no sintetizados · declarado explícitamente | — |
| H-BB2-52 | EVIDENCE | `SCFV_MOTOR_CIERRE.md` citado por H9 pero no por la matriz | D-BB-50 |
| H-BB2-53 | EVIDENCE | Estructura de 13 bloques no incluye corpus normativo/evaluativo/fundacional | D-BB-46 |
| H-BB2-54 | EVIDENCE | Vocabulario de estados subutilizado (`NO VERIFICADO`, `APARCADO`) | D-BB-51 |
| H-BB2-55 | EVIDENCE | Bloque 13 se autodestruye como meta-referencial | — |

---

## §4 · B-bis.3 · Corpus fundacional

### §4.1 · Carátula (VERSION · README · CONTRIBUTING · CHANGELOG)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB3-1 | EVIDENCE | Los dos repos (scfv-dsr / scfv_v6) comparten conceptos sin frontera declarada | — |
| H-BB3-2 | REENCUADRE | `scfv-dsr` es artefacto DSR · materialización derivada · no acto fundacional | — |
| H-BB3-3 | REENCUADRE | Materialización derivada, autocontenida, creada 2026-09-26 | — |
| H-BB3-4 | EVIDENCE | Acto fundacional 2026-09-10 · fecha intermedia no documentada en corpus doctrinal | D-BB-54 |
| H-BB3-5 | CONTRACT | Giro 06 y Episodio 3 introducidos · sistema de dos ejes | D-BB-55, D-BB-56 |
| H-BB3-6 | EVIDENCE | `~/SCFV_DSR/var/scfv.db` · dato faltante del Bloque A resuelto | — |
| H-BB3-7 | EVIDENCE | Licencia AGPL-3.0 · coherente con release público S0 | D-BB-57 |
| H-BB3-8 | EVIDENCE | GPG pendiente · commits sin firma criptográfica | D-BB-60 |
| H-BB3-9 | EVIDENCE | Componentes `Intellectus`, `Dictum` no vistos antes | D-BB-58 |
| H-BB3-10 | EVIDENCE | `baldor.py` vive en `kernel/` como primitiva fundacional | — |

### §4.2 · HASHES + GENEALOGIA (420 L)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB3-11 | EVIDENCE | Existen dos checkouts · `SCFV_DSR` (original) vs `scfv-dsr` (auditado) | D-BB-62 |
| H-BB3-12 | EVIDENCE | 9 archivos con SHA-256 de cadena vacía · `__init__.py` vacíos | — |
| H-BB3-13 | EVIDENCE | `HASHES.txt` es parcial · no certifica gobernanza | D-BB-63 |
| H-BB3-14 | EVIDENCE | Segunda ubicación del Documento Fundacional · `~/Programa-de-Investigacion-SCFV/` | D-BB-61 |
| H-BB3-15 | CONTRACT | Simón Rodríguez (1769-1854) como fuente doctrinal · no anticipado en ADRs | — |
| H-BB3-16 | REENCUADRE | Descubrimiento del Programa de Investigación · el software es una materialización | — |
| H-BB3-17 | EVIDENCE | Locus privado `~/Programa-de-Investigacion-SCFV/` · ~3000 L no accedidos | D-BB-61 |
| H-BB3-18 | EVIDENCE | Sistema de Giros completo · 01..06 con Episodios 1..3 | D-BB-56 |
| H-BB3-19 | EVIDENCE | Release público S0 emitido 26-09 · paradoja del acta (17-09) resuelta | D-BB-57 |
| H-BB3-20 | AUTORRECONOCIDO | Corpus declara etapa previa en GENEALOGIA §9 · reencuadra ~10 hallazgos | D-BB-3, 16, 40 |
| H-BB3-21 | CONTRACT | Motor filosófico: Simón Rodríguez, tres formulaciones | — |
| H-BB3-22 | EVIDENCE | Nomenclatura doble `SCFV_DSR` / `scfv-dsr` | D-BB-62 |
| H-BB3-23 | EVIDENCE | `HASHES.txt` no certifica gobernanza | D-BB-63 |
| H-BB3-24 | EVIDENCE | 21 cánones independientes · 21 actas · 272 emergencias · 8 patrones A-H | D-BB-64 |
| H-BB3-25 | EVIDENCE | 9 documentos fundacionales mencionados · no enumerados | D-BB-65 |
| H-BB3-26 | EVIDENCE | "BIBLIOTECA" mencionada sin definición | D-BB-66 |
| H-BB3-27 | EVIDENCE | "Hash maestro E3" del DSR sin definición | D-BB-67 |
| H-BB3-28 | CONTRACT | §4.2 GENEALOGIA ≠ ADR-001 · ontologías cuaternarias paralelas | D-BB-68 |
| H-BB3-29 | CONTRACT | Horizonte "hermenéutico → heurístico → performativo" · no en corpus doctrinal | D-BB-69 |
| H-BB3-30 | HYPOTHESIS | Antifragilidad con asterisco · hipótesis declarada | — |
| H-BB3-31 | CONTRACT | Modelo Git (§8.1) vs SQLite/EventStore · sin ADR que los relacione | D-BB-70 |
| H-BB3-32 | CONTRACT | §8.4 IA-1 como ejecutor técnico con autorización registrada | — |
| H-BB3-33 | AUTORRECONOCIDO | §9 declaración explícita de etapa previa · corpus sabe lo que tiene | — |

### §4.3 · DOCUMENTO_FUNDACIONAL (933 L)

| ID | Cat. | Descripción | Deuda |
|---|---|---|---|
| H-BB3-34 | CONTRACT | §31 define condición de cierre S0 que H9 NO evalúa (CONCEPTO, ARQUITECTURA) | D-BB-72 |
| H-BB3-35 | EVIDENCE | §10 menciona "estructura transversal de siete niveles" sin enumerar | D-BB-73 |
| H-BB3-36 | CONTRACT | §26 declara Sampieri como referencia metodológica central | — |
| H-BB3-37 | CONTRACT | §18 distingue IA como extensión cognitiva sin autoridad | — |
| H-BB3-38 | CONTRACT | §17 `propuesta → decisión → ejecución` · 4ª cadena cuaternaria | D-BB-68 |
| H-BB3-39 | EVIDENCE | §19 enumera 9 dimensiones de SCFV | — |
| H-BB3-40 | CONTRACT | §28 no inmunización teórica · regla de autoexposición | — |
| H-BB3-41 | EVIDENCE | §33 · 7 estados epistemológicos del Programa | — |
| H-BB3-42 | CONTRACT | §6 espiral hermenéutica · §32 cierre provisional · reversibilidad | — |

---

## §5 · Reencuadres de hallazgos Ventana 10

| Hallazgo Ventana 10 | Reencuadre B-bis |
|---|---|
| HC-1 "Constitución no aplicada" | FALSO · la Constitución rige M1 · DSR es M2 |
| HC-2 "Contradicción Constitución ↔ Glosario" | NO ES CONTRADICCIÓN · tensión temporal declarada |
| HC-3 "ADRs nunca leídos" | CONFIRMADO · contextualizado: rigen M1 |
| HC-4 "Tétrada sin consumidor" | AMBIGUA · 3 tétradas coexisten |
| HC-5/6 HUECOS genealógicos | CONFIRMADOS · reencuadrados como parte del método deconstruccionista |
| HC-7 `motor_causal.py` sin acta | CONFIRMADO |
| D-B-1..26 (Bloque B) | Sin invalidación · aplicables como deuda del port |
| Bloque A · `var/scfv.db` | RESUELTO · DB local `scfv_dsr.cli init` |
| Bloque A · `fpdf` no declarada | CONFIRMADO · deuda del port |
| Bloque A · corpus fundacional no leído | RESUELTO en B-bis.3 |

---

## §6 · Balance

```

Total hallazgos registrados:    ~120 fichas
B-bis.0:                          5
B-bis.1:                         11  (5 EVIDENCE + 6 HC-BB)
B-bis.2:                         55
B-bis.3:                         42
Reencuadres Ventana 10:          10

Deudas asociadas únicas:        D-BB-1..73

Familias:
F1 · Corpus sub-declarado
F2 · Confusión de repos en traspaso
F3 · Numeraciones paralelas
F4 · Documentos híbridos
F5 · Falsos verdes
F6 · Desincronización documental
F7 · Corpus autorreconocido

```

---

**Fin del catálogo.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
