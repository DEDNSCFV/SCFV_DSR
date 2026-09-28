# Bloque B-bis · Deudas registradas

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** B-bis.0..3 (25 archivos · 6864 L).
**Naturaleza:** registro de deudas nuevas. No resuelve. No prioriza. Trazabiliza.

---

## §0 · Método

Cada deuda se registra con: ID · categoría · origen (hallazgo o turno B-bis) · descripción · estado (ABIERTA).

Sin priorización. Sin asignación de destino. El acto de clasificar destino corresponde a un acto posterior.

---

## §1 · Corpus y estructura (D-BB-1..7)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-1 | H-BB0-1, H-BB1-1, H-BB1-2 | `scfv_v6` fuera de control de versión consistente · ahead 1 / behind 3 · 155 sucio |
| D-BB-2 | H-BB1-3 | ADRs son fuente primaria de facto, no canónica de iure · untracked |
| D-BB-3 | H-BB0-2, H-BB1-4 | 51 `.bak_*` en `~/scfv_v6/DOCS/` sin resolver · no tracked |
| D-BB-4 | HC-BB-2 | ADR-000 ↔ ADR-005 supersesión parcial no documentada (SQLite → SQLCipher) |
| D-BB-5 | HC-BB-3 | Pruebas 5–39 citadas por ADRs sin ubicación declarada ni implementación |
| D-BB-6 | HC-BB-5 | Tríada desalineada: ADR-000 dice `pypdf`+`pillow` · pyproject dice `lark` · código importa `fpdf` |
| D-BB-7 | HC-BB-1 | ADRs aprobados 2026-08-26 no consumidos en código DSR |

---

## §2 · DSL, métricas, verificabilidad (D-BB-8..12)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-8 | H-BB2-1 | DSL periférico respecto a ruta canónica · contradicción con ADRs |
| D-BB-9 | H-BB2-2 | `scfv_validator.py` produce métrica sobre lista vacía · falso verde |
| D-BB-10 | H-BB2-3 | PCU descentralizado · 5 copias divergentes · cuenta `110101` no única |
| D-BB-11 | H-BB2-4 | `PODERES/` sin versionar (H5.7-FINDING-GIT-001) |
| D-BB-12 | H-BB2-5 | Legacy y canónica cohabitan sin plan de convergencia declarado |

---

## §3 · Documentos híbridos y estructura del corpus evaluativo (D-BB-13..17)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-13 | H7B/H7H | `anillo.py` aparcado · `nivel_composicion` no existe · Camino 3 parcial |
| D-BB-14 | H8P_IMPORTADOR | `MotorContable(None)` en `exportador.py:66` (bug latente) |
| D-BB-15 | H7B/H7H D.3 | Desincronización documental en `H8P_EXAMINADOR_CONTRATO.md` (resuelta) |
| D-BB-16 | H-BB2-7, H-BB2-8, H-BB2-15 | Documentos híbridos · H7B, H7H, H8P_RETICULO mezclan estados |
| D-BB-17 | H-BB2-10, H-BB2-11 | H7c–H7g no desarrollados · "Clausura de procesadores" sin detalle |

---

## §4 · Referencias y numeraciones (D-BB-18..23)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-18 | H-BB2-18 | Referencia doctrinal externa "Contreras" sin cita verificable |
| D-BB-19 | H-BB2-16 | ≥5 componentes canónicos no caracterizados (Adquisidor, Perceptum, PropuestaH1, ConsecuenciaAutorizada, NucleoConsecuencias) |
| D-BB-20 | H-BB2-17 | Numeración de invariantes Motor (I2, I6, I7) sin catálogo visible |
| D-BB-21 | H-BB2-13 | D.5 citada como heredada de H7H pero ausente en H7H leído |
| D-BB-22 | H-BB2-14, H-BB2-31 | Drift de versión (v6 · v6.1 · v8.2 · 9.0.0 · v6.3) sin ADR de transición |
| D-BB-23 | H-BB2-19 | Suite 223 tests en `~/scfv_v6/TESTS/` no reflejada en traspaso |

---

## §5 · Corpus doctrinal no leído / huérfano (D-BB-24..29)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-24 | H-BB2-20, HC-BB-4 | `SCFV_MOTOR_CIERRE.md` (cierre histórico S0) nunca leído · citado 4+ veces |
| D-BB-25 | H-BB2-24 | HL-42 abierto en `BITACORA_GIRO_02.md` línea 28 |
| D-BB-26 | H-BB2-21 | Colisión nomenclatura I-números (Motor vs Importador vs Perceptum) |
| D-BB-27 | H-BB2-22 | Régimen tripartito introducido sin ADR |
| D-BB-28 | H-BB2-23 | `Perceptum` no caracterizado en ningún contrato |
| D-BB-29 | H-BB2-24 | `BITACORA_GIRO_02.md` no leído |

---

## §6 · Régimen y nomenclatura (D-BB-30..33)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-30 | H-BB0-4, H-BB2-26 | "Giro 01/02/03" sin definición en corpus |
| D-BB-31 | H-BB2-27 | Nomenclatura IA-1/IA-2/IA-3 difiere entre régimen ventana y doctrinal |
| D-BB-32 | H-BB2-29 | 11 días de actividad (17→28 sep) fuera del corpus doctrinal leído |
| D-BB-33 | H-BB2-33 | `MotorContable(None)` tratado asimétricamente en H9_EVALUACION vs S0_CIERRE |

---

## §7 · Contradicciones internas del corpus (D-BB-34..35)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-34 | H-BB2-32 | NPL (event_store embebido) vs migración 002 (auditoria_hash_chain separada) |
| D-BB-35 | H-BB2-33, HC-BB-6 | NPL sin SQLCipher vs ADR-005 cifrado obligatorio |

---

## §8 · Cuaderno `_EA_HALLAZGOS` (D-BB-36..45)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-36 | H-BB2-30, H-BB2-47 | Bloques K-L-M del cuaderno ausentes en disco |
| D-BB-37 | H-BB2-41 | `ACTAS/` directorio nuevo · `ACTA_A-1.3` no mapeado |
| D-BB-38 | H-BB2-39 | Sistema de numeración `HL-NNN` paralelo a `H-XXX-NN` |
| D-BB-39 | H-BB2-39 | "Giro 03" introducido sin definición |
| D-BB-40 | H-BB2-37, H-BB2-38 | 5 pares de hash SHA-256 idénticos pre/post · `LIVA_Art4` duplicado |
| D-BB-41 | H-BB2-36 | `seguridad/__init__.py` vacío con `test_cifrado` verde · falso verde |
| D-BB-42 | H-BB2-43 | 21 componentes de test S0 no mapeados en C3 |
| D-BB-43 | H-BB2-35 | Migración 007 materializa 1 de 4 tablas epistemic · contradice ADR-004 |
| D-BB-44 | H-BB2-20 | Corpus referenciado no leído: `SCFV_MOTOR_CIERRE`, `FRACTALIDAD_ACOTADA`, `provenance`, `requirements`, `matrix`, `pruebas_camino_critico`, C1/C3 |
| D-BB-45 | H-BB2-42 | Cuaderno declara "PENDIENTE" tras PASS del Gate · sin actualización |

---

## §9 · Matriz `_EA_MATRIZ_SINTESIS` (D-BB-46..51)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-46 | H-BB2-53 | La matriz no tiene bloque específico para corpus normativo, evaluativo previo, ni gobernanza |
| D-BB-47 | H-BB2-45, H-BB2-49 | Matriz desactualizada respecto a Gate S0 PASS (17-09) |
| D-BB-48 | H-BB2-46 | Matriz desactualizada respecto a Bloque R del cuaderno (18-09) |
| D-BB-49 | H-BB2-48 | Inconsistencia 12 vs 13 bloques en §13.1 vs cierre |
| D-BB-50 | H-BB2-52 | `SCFV_MOTOR_CIERRE.md` citado por H9 pero no por la matriz |
| D-BB-51 | H-BB2-54 | Vocabulario de estados subutilizado (`NO VERIFICADO`, `APARCADO` sin uso) |

---

## §10 · Carátula fundacional (D-BB-52..60)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-52 | B-bis.3.0 | (revisada) Traspaso confundió repos · corpus fundacional = `scfv-dsr` |
| D-BB-53 | H-BB3-7 | `SCFV_DSR` 0.1.0 vs SCFV v6→9.0.0 · dos líneas de versionado sin ADR de bifurcación |
| D-BB-54 | H-BB3-4 | Acto fundacional 2026-09-10 sin documentación en `scfv_v6/DOCS/` |
| D-BB-55 | H-BB3-5 | Giro 06 con 11 enmiendas pendientes · no materializadas |
| D-BB-56 | H-BB3-5, H-BB3-18 | Sistema de dos ejes (Giro × Episodio) sin definición |
| D-BB-57 | H-BB3-7, H-BB3-19 | Release público S0 (26-09) posterior a acta "RELEASE NO EMITIDO" (17-09) |
| D-BB-58 | H-BB3-9 | Componentes `Intellectus`, `Dictum` no caracterizados |
| D-BB-59 | H-BB3-2, H-BB3-22 | Layout DSR ≠ layout `scfv_v6` · sin ADR que declare el cambio |
| D-BB-60 | H-BB3-8 | GPG pendiente · commits sin firma criptográfica |

---

## §11 · Corpus privado y accesos (D-BB-61..67)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-61 | H-BB3-14, H-BB3-17 | Corpus privado `~/Programa-de-Investigacion-SCFV/` · ~3000 L + 21 actas · no accedido |
| D-BB-62 | H-BB3-11, H-BB3-22 | `SCFV_DSR` (original) vs `scfv-dsr` (checkout) · ¿mismo repo o clon divergente? |
| D-BB-63 | H-BB3-13, H-BB3-23 | `HASHES.txt` no certifica documentos de gobernanza |
| D-BB-64 | H-BB3-24 | 21 cánones · 21 actas · 272 emergencias · 8 patrones A-H no leídos |
| D-BB-65 | H-BB3-25 | 9 documentos fundacionales no enumerados |
| D-BB-66 | H-BB3-26 | "BIBLIOTECA" mencionada sin definición |
| D-BB-67 | H-BB3-27 | "Hash maestro E3" del DSR sin definición |

---

## §12 · Ontologías paralelas (D-BB-68..70)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-68 | H-BB2-6, H-BB3-28, H-BB3-38 | 4 cadenas cuaternarias paralelas sin reconciliación (ADR-001 · GENEALOGIA §4.2 · Fundacional §17 · Fundacional §21) |
| D-BB-69 | H-BB3-29 | Horizonte "hermenéutico → heurístico → performativo" no en corpus doctrinal |
| D-BB-70 | H-BB3-31 | Modelo Git (§8.1 GENEALOGIA) vs SQLite/EventStore sin ADR que los relacione |

---

## §13 · Corpus privado, actas y hash (D-BB-71)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-71 | H-BB3-24 | `ACTAS/ACTO_6_0_GENEALOGIA_OPERADA.md` · "11 distinciones A-K" y "14 lecturas L-01..L-14" · no leídas |

---

## §14 · Documento Fundacional (D-BB-72..73)

| ID | Origen | Descripción |
|---|---|---|
| D-BB-72 | H-BB3-34 | Gate H9 no evalúa el nivel CONCEPTO de §31 del Documento Fundacional |
| D-BB-73 | H-BB3-35 | "Estructura transversal de siete niveles" mencionada sin enumerar |

---

## §15 · Deudas registradas en el propio corpus (heredables a DSR)

Deudas que el corpus declara y que B-bis recoge sin resolución:

| ID | Origen | Descripción |
|---|---|---|
| D-IMP-01 | H8P_IMPORTADOR §22.4 | Rechazo de unidad duplicado en `ReporteImportacion.rechazos` y en `LOTE_PROCESADO.payload.unidades` |
| D-IMP-02 | H8P_IMPORTADOR §22.4 | No valida localmente marco_contable vs `pcu[c]["marcos"]` |
| DESC-01 | H8P_IMPORTADOR §22.4 | Descripción de unidad no llega hasta la descripción del asiento |
| H-PER-CONF | H8P_IMPORTADOR §22.4 | Perceptum emite `ALTA_INCERTIDUMBRE` en lotes controlados |
| D.5 | H7H / H8P_IMPORTADOR §12 | `EventStore.obtener_por_correlation` devuelve payload sin parsear |
| H6.10-FINDING-SCHEMA-001 | H6_CIERRE | Normas `BA_VEN_NIF_01.json` y `LIVA_Art4.json` no cumplen schema v8.2.1 |
| H6.10-FINDING-REF-001 | H6_CIERRE | `V'` con criterio (3) de validación cruzada abierto |
| H5.7-FINDING-GIT-001 | H6_CIERRE | `PODERES/` sin archivos bajo control de versiones |
| HL-42 | H9_GATE_S0_ACTA §8 | `BITACORA_GIRO_02.md` línea 28 · formulación ambigua no bloqueante |
| H-DEUA13-01 | _EA_HALLAZGOS Bloque R | Defecto numérico IVA · `iva = monto * IVA_TASA / 100000000` en `scfv_architect.py` |
| MotorContable(None) | H9_EVALUACION §3 E3 | `exportador.py:66` · firma exige `pcu: Dict` sin default |
| Extensión multi-período | H9_EVALUACION §3 E3 | Deuda histórica delegada |
| Consolidación NIIF real | H9_EVALUACION §3 E3 | Deuda histórica delegada |
| Operacionalización tétrada H1 | H9_EVALUACION §3 E3 | Deuda histórica delegada |

---

## §16 · Total

```

D-BB-1..73                 73 deudas nuevas
Deudas corpus heredadas    14 (registradas en §15)
──────────────────────────────────────────
Total registrado            87

```

---

## §17 · Estados

```

D-BB-1..73              ABIERTAS · sin resolución
Deudas corpus           ABIERTAS · ya declaradas por el corpus mismo

```

Ninguna deuda se resuelve en este documento. El registro es para trazabilidad futura.

---

**Fin del catálogo de deudas.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
