# Bloque C-α · Matriz de los 21 cánones

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** C-α.3..5 (21 cánones leídos uno por uno).
**Naturaleza:** verificación de la matriz declarada por CONV §2.1.

---

## §0 · Método

Cada canon se verificó contra su acta individual. Los contadores declarados por `ACTO_6_0_CONV_CONVERGENCIA §2.1` se comparan con los contadores reales del acta.

Estados:
- **COINCIDE** · la fila del §2.1 = el acta individual
- **DISCREPA** · diferencia numérica

---

## §1 · Matriz verificada

| # | Canon | R | P | F | NA | Total | Estado |
|---|---|---|---|---|---|---|---|
| 6.0.01 | Accounting Theory 2004 | 4 | 1 | 4 | 2 | 11 | ✅ COINCIDE |
| 6.0.02 | Aho 2007 | 7 | 3 | 4 | 2 | 16 | ✅ COINCIDE |
| 6.0.03 | Angrisani 2019 | 11 | 2 | 7 | 2 | 22 | ✅ COINCIDE |
| 6.0.04 | Cervantes 2023 | 5 | 4 | 7 | 1 | 17 | ✅ COINCIDE |
| 6.0.05 | Cosmovisión 2004 | 1 | 2 | 3 | 2 | 8 | ✅ COINCIDE |
| 6.0.06 | Díaz Navarro 2014 | 1 | 4 | 5 | 2 | 12 | ✅ COINCIDE |
| 6.0.07 | Gadamer VM | 1 | 3 | 5 | 1 | 10 | ✅ COINCIDE |
| 6.0.08 | Hevner 2010 | 6 | 5 | 7 | 0 | 18 | ✅ COINCIDE |
| 6.0.09 | Huck 2024 | 1 | 4 | 5 | 0 | 10 | ✅ COINCIDE |
| 6.0.10 | Lakatos 1976/1989 | 4 | 3 | 4 | 0 | 11 | ✅ COINCIDE |
| 6.0.11 | Mandelbrot 1975/1982 | 3 | 3 | 3 | 1 | 10 | ✅ COINCIDE |
| 6.0.12 | Merkle 1979 | 3 | 2 | 1 | 1 | 7 | ✅ COINCIDE |
| 6.0.13 | NIST FIPS 180-4 | 2 | 3 | 4 | 1 | 10 | ✅ COINCIDE |
| 6.0.14 | Popper 1980 | 2 | 5 | 5 | 0 | 12 | ✅ COINCIDE |
| 6.0.15 | ProGit 2014 | 2 | 4 | 5 | 1 | 12 | ✅ COINCIDE |
| 6.0.16 | Reynoso/Kicillof 2004 | 5 | 3 | 4 | 0 | 12 | ✅ COINCIDE |
| 6.0.17 | Rodríguez 2016 | 6 | 4 | 2 | 1 | 13 | ✅ COINCIDE |
| 6.0.18 | Romero López 4ª ed. | 8 | 6 | 3 | 0 | 17 | ✅ COINCIDE |
| 6.0.19 | Romney 15th ed. | 3 | 4 | 4 | 0 | 11 | ✅ COINCIDE |
| 6.0.20 | Sampieri 2018 | 2 | 4 | 5 | 0 | 11 | ✅ COINCIDE |
| 6.0.21 | Sommerville 2005 | 1 | 6 | 8 | 1 | 16 | ✅ COINCIDE |
| | **Total** | **78** | **75** | **95** | **18** | **266** | **21/21** |

---

## §2 · Comparación con CONV §2.2

### §2.1 · Lo que el CONV declara en §2.2

```

Resiste   = 78/272 = 28,7 %
Parcial   = 77/272 = 28,3 %
Falla     = 99/272 = 36,4 %
No aplica = 18/272 =  6,6 %

```

### §2.2 · La suma real de §2.1

```

Resiste   = 78
Parcial   = 75
Falla     = 95
No aplica = 18
─────
266

```

### §2.3 · Discrepancia

```

Resiste             78           78               +0  ✅
Parcial             75           77               +2  ⚠️
Falla               95           99               +4  ⚠️
No aplica           18           18               +0  ✅
─────        ─────            ─────
Total              266          272               +6  ⚠️

```

**El CONV §2.2 declara 6 emergencias más que la suma real de los 21 cánones.**

**D-Cα-107 · Inconsistencia aritmética en `ACTO_6_0_CONV_CONVERGENCIA §2.2`.**

---

## §3 · Matriz por canon verificado · detalle

### §3.1 · Cánones 01-07

| Canon | R | P | F | NA | Total | Fuente |
|---|---|---|---|---|---|---|
| 01 Accounting Theory | 4 | 1 | 4 | 2 | 11 | ACTO_6_0_01 §5 |
| 02 Aho | 7 | 3 | 4 | 2 | 16 | ACTO_6_0_02 §5 |
| 03 Angrisani | 11 | 2 | 7 | 2 | 22 | ACTO_6_0_03 §5 |
| 04 Cervantes | 5 | 4 | 7 | 1 | 17 | ACTO_6_0_04 §5 |
| 05 Cosmovisión | 1 | 2 | 3 | 2 | 8 | ACTO_6_0_05 §5 |
| 06 Díaz Navarro | 1 | 4 | 5 | 2 | 12 | ACTO_6_0_06 §5 |
| 07 Gadamer | 1 | 3 | 5 | 1 | 10 | ACTO_6_0_07 §5 |
| **Subtotal** | **30** | **19** | **35** | **12** | **96** | — |

### §3.2 · Cánones 08-14

| Canon | R | P | F | NA | Total | Fuente |
|---|---|---|---|---|---|---|
| 08 Hevner | 6 | 5 | 7 | 0 | 18 | ACTO_6_0_08 §5 |
| 09 Huck | 1 | 4 | 5 | 0 | 10 | ACTO_6_0_09 §5 |
| 10 Lakatos | 4 | 3 | 4 | 0 | 11 | ACTO_6_0_10 §5 |
| 11 Mandelbrot | 3 | 3 | 3 | 1 | 10 | ACTO_6_0_11 §5 |
| 12 Merkle | 3 | 2 | 1 | 1 | 7 | ACTO_6_0_12 §5 |
| 13 NIST | 2 | 3 | 4 | 1 | 10 | ACTO_6_0_13 §5 |
| 14 Popper | 2 | 5 | 5 | 0 | 12 | ACTO_6_0_14 §5 |
| **Subtotal** | **21** | **25** | **29** | **3** | **78** | — |

### §3.3 · Cánones 15-21

| Canon | R | P | F | NA | Total | Fuente |
|---|---|---|---|---|---|---|
| 15 ProGit | 2 | 4 | 5 | 1 | 12 | ACTO_6_0_15 §5 |
| 16 Reynoso | 5 | 3 | 4 | 0 | 12 | ACTO_6_0_16 §5 |
| 17 Rodríguez | 6 | 4 | 2 | 1 | 13 | ACTO_6_0_17 §5 |
| 18 Romero López | 8 | 6 | 3 | 0 | 17 | ACTO_6_0_18 §5 |
| 19 Romney | 3 | 4 | 4 | 0 | 11 | ACTO_6_0_19 §5 |
| 20 Sampieri | 2 | 4 | 5 | 0 | 11 | ACTO_6_0_20 §5 |
| 21 Sommerville | 1 | 6 | 8 | 1 | 16 | ACTO_6_0_21 §5 |
| **Subtotal** | **27** | **31** | **31** | **3** | **92** | — |

### §3.4 · Totales por bloque

```

Cánones 01-07     30 R · 19 P · 35 F · 12 NA =  96
Cánones 08-14     21 R · 25 P · 29 F ·  3 NA =  78
Cánones 15-21     27 R · 31 P · 31 F ·  3 NA =  92
─────────────────────────────────
Total             78 R · 75 P · 95 F · 18 NA = 266

```

---

## §4 · Estructura de los resultados

### §4.1 · Distribución por categoría

```

Resiste   : 78/266 = 29,3 %
Parcial   : 75/266 = 28,2 %
Falla     : 95/266 = 35,7 %
No aplica : 18/266 =  6,8 %

```

**La categoría dominante es "falla" (35,7 %).** Coherente con `CONV §2.3`:
> *"La media de fallas está concentrada en capas declarativas, no en capas funcionales."*

### §4.2 · Cánones por densidad de fallas

**Cánones con mayor densidad de fallas:**
```

21 Sommerville   8/16 = 50,0 %
03 Angrisani     7/22 = 31,8 %
04 Cervantes     7/17 = 41,2 %
08 Hevner        7/18 = 38,9 %

```

**Cánones con menor densidad de fallas:**
```

12 Merkle        1/7  = 14,3 %
17 Rodríguez     2/13 = 15,4 %
05 Cosmovisión   3/8  = 37,5 %
11 Mandelbrot    3/10 = 30,0 %

```

**Cánones con más resistes absolutos:**
```

18 Romero López  8/17
03 Angrisani    11/22
02 Aho           7/16
08 Hevner        6/18
17 Rodríguez     6/13

```

**Los cánones disciplinares (Romero López, Angrisani) resisten más.** Los cánones de ingeniería/metodología (Sommerville, Cervantes, Hevner) fallan más. **Coherente con la distinción funcional/declarativo.**

---

## §5 · Reconstrucción de los 8 patrones

Del análisis de los 21 cánones se reconstruyen los 8 patrones declarados por CONV §4.1:

| Patrón | Nombre | Detectores declarados | Detectores verificados |
|---|---|---|---|
| **A** | Declaración parcial de alcance | 7 | 7 ✅ |
| **B** | Principios implícitos no declarados | 6 | 6 ✅ |
| **C** | Sin genealogía ni hermenéutica | 3 | 3 ✅ |
| **D** | Brecha parser-evaluador | 1 (Aho) | 1 ✅ |
| **E** | Firma no criptográfica | 3 (Merkle, NIST, ProGit) | 3 + Romney = **4** ⚠️ |
| **F** | Materialización sin congelamiento | 1 (ProGit) | 1 ✅ |
| **G** | Dimensión pedagógica ausente | 1 (Rodríguez) | 1 ✅ |
| **H** | Migración sin genealogía | emergent | emergente ✅ |

**Hallazgo:** el Patrón E tiene **4 detectores verificables** (Merkle + NIST + ProGit + Romney), no 3 como declara el CONV. Romney detecta confidencialidad/privacidad ausentes — misma familia.

**D-Cα-127 · Patrón E tiene 4 detectores verificables, no 3.**

---

## §6 · Verificación de IPVE del corpus 6.0

`CONV §5bis.2` declara 4 componentes IPVE:

**I — Invariantes:**
```

Hash maestro · estructura §1-§9 · firma tripartita §20 ·
registro GIRO_05/REGISTRO_ACTOS.log · contadores R/P/F/NA

```
✅ Verificable en cada acta.

**P — Propiedades auditadas:**
```

Núcleo algebraico (Baldor) · núcleo epistemológico (Perceptum/Intellectus/Dictum) ·
núcleo contable (motor/event_store) · DSL-SCFV con ADL formal · SHA-256 vía hashlib ·
firma ausente

```
✅ Verificable.

**V — Validaciones:**
```

21 falsaciones individuales · cita literal obligatoria (R6) ·
ubicación obligatoria (R7) · 272 emergencias

```
⚠️ **272 emergencias son en realidad 266.** D-Cα-107.

**E — Evidencias:**
```

21 actas firmadas · 79 líneas REGISTRO_ACTOS.log · hashes SHA256 de raws

```
✅ Verificable.

---

## §7 · Balance de la matriz

```

21/21 cánones coinciden con §2.1 del CONV
21/21 cánones tienen acta individual materializada
21/21 cánones citan loci del raw
21/21 cánones usan firma tripartita asimétrica
21/21 cánones declaran §6 CDEE del propio autor
21/21 cánones declaran §7 constancia de no opinión

```

**La auditoría multi-canon del corpus privado es 100 % reproducible por terceros.**

**Dos discrepancias detectadas:**

1. **D-Cα-107** · suma agregada §2.2 declara 272, la real es 266 (+6 error).
2. **D-Cα-127** · Patrón E tiene 4 detectores verificables, no 3.

**Ninguna de las dos invalida la matriz.** Los 21/21 cánones están correctos. Los errores están en los **agregados** del CONV, no en las filas.

---

**Fin de la matriz.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
