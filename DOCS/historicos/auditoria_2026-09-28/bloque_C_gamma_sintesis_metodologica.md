# C-γ · Síntesis global metodológica

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Ventana:** 12.
**Bloque:** C-γ.
**Naturaleza:** síntesis metodológica sobre el corpus auditado V10–V12.
**Shell:** no requerido. Análisis puro sobre actas materializadas.

---

## §0 · Metadatos

```

Ventana:               12
Fecha:                 2026-09-28
Bloque:                C-γ
Base:                  actas V10 + V11 + M1.α + M1.β + M1.γ + M1.δ
HEAD scfv-dsr previo:  aa934a6

```

---

## §1 · Corpus recorrido

```

V10   A · inventario puro                       ~14.400 L leídos
V10   B · análisis estático
V11   B-bis · corpus doctrinal/fundacional      1.375 L
V11   C-β · corpus técnico DSR                  1.449 L
V11   C-α · corpus privado Programa             1.502 L
V12   M1.0 · sizing global                       (medición)
V12   M1.α · PODERES                            9.038 L
V12   M1.β · TESTS                              5.625 L
V12   M1.γ · INFRAESTRUCTURA                    1.748 L
V12   M1.δ · DOMINIOS                             892 L

```

Total auditado: ~20.000 L fuente primaria. 21 archivos de auditoría en scfv-dsr. 9 commits en la sesión 2026-09-28.

---

## §2 · Método declarado vs método operado

Régimen declarado al cierre de V11:

```

Modo B · Operador ejecuta · IA interpreta
STOP shell hasta autorización por bloque
Un diff = un commit
Comandos copy-pasteables literales, sin $ ni comentarios
Hallazgo → IA-2 → materialización → acta
Fuente primaria antes que mediación
Falsación cruzada obligatoria
Reconocimiento explícito de errores propios
Régimen tripartito asimétrico (Operador + IA-1 + IA-2)
Mensajes de commit en español con prefijo docs:
Bloqueos resueltos antes de avanzar

```

| Principio | Cumplido | Nota |
|---|---|---|
| Modo B | Sí | Sin excepciones. |
| STOP shell | Parcial | Saltos puntuales en M1.α.6 → M1.β.0. |
| Un diff = un commit | Sí | 4 actas · 4 commits. |
| Comandos literales | Parcial | 8 errores propios declarados. |
| Hallazgo → IA-2 | Parcial | IA-2 no siempre en turno separado. |
| Fuente primaria | Sí | Todo juicio sobre código o salida real. |
| Falsación cruzada | Sí | 4 ciclos → 0 ciclos. |
| Reconocimiento de errores | Sí | 8 declarados y trazados. |
| Tripartito asimétrico | Parcial | Sin separación estricta de turnos. |
| Mensajes en español | Sí | Prefijo docs: uniforme. |
| Bloqueos resueltos | Sí | V11 corregido antes de V12. |

Lo que funcionó: falsación cruzada. Cuatro hipótesis propias falsadas por pasos sucesivos sin intervención externa.

Lo que no funcionó: la sintaxis de los comandos. Cuatro grep con bugs (`! -path`, patrón sin dígitos, patrón sin `as`, filtro `.bak_` vs `.bak.`). El vacío devuelto parecía evidencia. La disciplina "fuente primaria antes que mediación" no protege contra comandos mal escritos: el vacío también es salida.

Lección operativa: antes de interpretar un vacío como evidencia, verificar el comando. Aplicado retroactivamente en M1.γ.4.

---

## §3 · Hallazgos estructurales consolidados

**A1 · PODERES es un DAG a nivel módulo.**
72 módulos, 9.038 L. AST + Tarjan: 0 SCCs no-triviales. Cuatro ciclos inter-poderes hipotetizados y falsados.

**A2 · TESTS verde, cobertura replicando topología.**
229 tests, 228 passed, 1 skipped, 36,79 s. Los módulos más importados internamente son los más testeados. 19 módulos PODERES sin test directo.

**A3 · INFRAESTRUCTURA declara 26 tablas, runtime materializa 2.**
`schema_final.sql` + 17 migraciones vs `scfv.db` runtime (2 tablas, 24 filas). Sin aplicador activo.

**A4 · DOMINIOS es estrato arqueológico v8.1 desconectado del runtime v8.2.**
No importa PODERES, no es importado por PODERES, sin tests, sin SQLite. `BaseFractal.__init__` incompatible con `FractalFiscal`. Error de ejecución latente.

**A5 · Cuatro corpus declarativos paralelos sin converger.**
`INFRAESTRUCTURA/db/` + `proyecciones/sql/` + SQL embebido en Python + `.scfv` DSL.

---

## §4 · Correlación con el Programa

V11 declaró: la auditoría externa es correlativa al Giro 06 · Sección 1 · Genealogía Operada del Programa.

Verificación post-M1: la arqueología de capas (v8.1 huérfano, v8.2 activo, corpus declarativo histórico, runtime mínimo) converge con la genealogía de la operación misma. Ambas líneas detectan estratos sin exhumarlos, reconocen deuda sin resolverla, distinguen capa declarativa de capa operativa.

La correlación se sostiene tras M1. No requiere postularse desde afuera.

---

## §5 · Falsaciones metodológicas

```

Hipótesis inicial          →  Estatuto tras auditoría
─────────────────────────────────────────────────────
4 ciclos inter-poderes     →  0 ciclos (AST + Tarjan)
event_store.py = runtime   →  ~30 puntos de conexión SQLite
schema_final = bootstrap   →  corpus declarativo sin aplicador
M1 = 5-15K L               →  17K L efectivos (~2x sobreestimación)

```

Cada una declarada en su acta. Convergencia con canon Hevner (autofalsación declarada, registrado en C-α).

---

## §6 · Deudas metodológicas

```

DM-1  Comandos grep con sintaxis incorrecta (4 casos)
DM-2  Saltos en la secuencia declarada
DM-3  IA-1 e IA-2 sin separación de turnos
DM-4  Numeración O1..O43 sin índice
DM-5  Deudas fragmentadas por bloque (D-B · D-BB · D-C · D-Cα · D-M1α · D-M1β · D-γ · D-M1δ)
DM-6  Correcciones retroactivas no siempre versionadas

```

Ninguna invalida hallazgos. Todas afectan reproducibilidad futura.

---

## §7 · Lo no auditado

```

M-higiene           raíz ~/scfv_v6 contaminada
proyecciones/sql/   tercer corpus declarativo (D-γ-CORPUS-1)
.bak.py (9)         backups .py en PODERES raíz (D-M1α-1)
scfv_diario.db      séptima DB referenciada (D-γ-DB-2)
Programa            Ciclo 6.0 auditado pero no abierto en V12
corpus privado      HL-1..412 no verificados en V12

```

Regla del acta: la auditoría declara lo que no auditó. Sin esta sección, la síntesis sería cierre falso.

---

## §8 · Firma de C-γ

Tres resultados demostrables:

1. El corpus técnico SCFV v8.2 es internamente coherente. PODERES DAG, TESTS verde, cobertura replicando topología.
2. El corpus declara mucho más de lo que opera. 26 tablas declaradas vs 2 materializadas. Cuatro corpus declarativos sin convergencia. READMEs 6–15x el código.
3. Hay estratos históricos no exhumados. DOMINIOS v8.1 huérfano. INFRAESTRUCTURA/db declarativa sin aplicador. scfv.db.baseline_v81 como fósil.

La intervención posterior elige qué deuda resolver. C-γ no elige. Nombra el corpus como es hoy.

---

**Fin del acta C-γ.**
