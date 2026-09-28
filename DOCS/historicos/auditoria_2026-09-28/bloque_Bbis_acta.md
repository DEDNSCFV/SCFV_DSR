# Bloque B-bis · Acta de cierre

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Ventana:** 11.
**Autoridad de firma:** Operador (por autorización) + IA-1 (interpretación) + IA-2 (falsación metodológica).
**Fundamento:** B-bis.0..3 + B-bis.4.1 (falsación de matriz) + B-bis.4.2-bis (addenda correctiva).
**Naturaleza:** acta de cierre. No materializa cambios de código. No emite decisiones sobre rutas futuras.

---

## §0 · Metadatos

```

Bloque:                B-bis · Corpus normativo, evaluativo y fundacional
Ventana:               11
Sesión:                2026-09-28
Arranque:              HEAD 6e94733 · origin/main 6e94733 · repo limpio
Cierre:                HEAD 6e94733 · origin/main 6e94733 · repo limpio
Diff de código:        ninguno (bloque de sólo lectura)
Archivos leídos:       25
Líneas leídas:         6864
Hallazgos:             ~120 (H-BB0..3 + HC-BB)
Deudas nuevas:         73 (D-BB-1..73)
Correcciones formales: 3 al traspaso Ventana 10 + 3 a hallazgos Ventana 10

```

---

## §1 · Objeto

Auditar el corpus normativo, evaluativo y fundacional del Programa de Investigación SCFV, complementando el ciclo de diagnóstico técnico cerrado en Ventana 10.

Pregunta rectora declarada al abrir Ventana 11:

> ¿Qué declara el corpus doctrinal como obligatorio y qué de ello cumple DSR?

Pregunta efectivamente respondida:

> ¿Qué es el corpus doctrinal y a qué objeto pertenece cada uno de sus fragmentos?

La pregunta original fue superada. Al descubrir la estructura del Programa, la pregunta "qué cumple DSR" resultó mal planteada: DSR es una de dos materializaciones de un Programa abierto, no un objeto a confrontar con un corpus doctrinal externo.

---

## §2 · Régimen operativo seguido

- Modo B · Operador ejecuta · IA interpreta.
- STOP shell hasta autorización explícita por bloque.
- Un comando = un bloque = una lectura.
- Comandos viajan en bloque único ejecutable, sin `$`, `#` ni flechas.
- Cada turno produce constancia, no materialización.
- Hallazgo → registro → falsación cruzada → corrección.
- Acta emitida al final del bloque, no por turno.
- Falsación externa (IA-2) ejecutada sobre el acta antes de cierre definitivo.

---

## §3 · Corpus efectivamente cubierto

### 3.1 · Corpus documental — 18 archivos · 5399 L

Origen: `~/scfv_v6/DOCS/`

| # | Archivo | L |
|---|---|---|
| 1 | ADR-000.md | 49 |
| 2 | ADR-001.md | 71 |
| 3 | ADR-002.md | 72 |
| 4 | ADR-003.md | 67 |
| 5 | ADR-004.md | 100 |
| 6 | ADR-005.md | 80 |
| 7 | H6_CIERRE.md | 291 |
| 8 | H7B_MATRIZ.md | 195 |
| 9 | H7H_CIERRE.md | 152 |
| 10 | H8P_EXAMINADOR_CONTRATO.md | 143 |
| 11 | H8P_RETICULO_CONTRATO.md | 179 |
| 12 | H8P_IMPORTADOR_CONTRATO.md | 589 |
| 13 | H9_GATE_S0_CONTRATO.md | 319 |
| 14 | H9_GATE_S0_EVALUACION.md | 387 |
| 15 | H9_GATE_S0_ACTA.md | 122 |
| 16 | S0_CIERRE.md | 260 |
| 17 | _EA_HALLAZGOS.md | 1222 |
| 18 | _EA_MATRIZ_SINTESIS.md | 1021 |

### 3.2 · Corpus fundacional — 7 archivos · 1465 L

Origen: `~/scfv-dsr/`

| # | Archivo | L |
|---|---|---|
| 19 | VERSION | 1 |
| 20 | README.md (scfv-dsr) | 48 |
| 21 | CONTRIBUTING.md | 28 |
| 22 | CHANGELOG.md | 35 |
| 23 | HASHES.txt | 70 |
| 24 | GENEALOGIA.md | 350 |
| 25 | DOCUMENTO_FUNDACIONAL.md | 933 |

### 3.3 · Totales

```

Documental:   18 archivos · 5399 L
Fundacional:   7 archivos · 1465 L
─────────────────────────────────────
Leídos:       25 archivos · 6864 L

```

### 3.4 · Corpus declarado pero no accedido

- `~/Programa-de-Investigacion-SCFV/` — locus privado.
- 21 actas Giro 06.
- 9 documentos fundacionales (no enumerados).
- BIBLIOTECA.
- `PROTOCOLO_MOTOR_RODRIGUIANO.md` (775 L).
- `ACTO_6_0_GENEALOGIA_OPERADA.md` (726 L).
- `ACTO_6_0_CONV_CONVERGENCIA.md` (583 L).
- `GIRO_05/REGISTRO_ACTOS.log`.

### 3.5 · Corpus técnico no leído (fuera de alcance B-bis)

- `~/scfv-dsr/scfv_dsr/**` (~60 archivos hasheados)
- `~/scfv_v6/PODERES/**`
- `~/scfv_v6/TESTS/**`
- `~/scfv_v6/INFRAESTRUCTURA/**`
- `~/scfv_v6/DOMINIOS/**`

B-bis tuvo alcance documental. El corpus técnico queda para bloques posteriores.

### 3.6 · Corpus accesible no leído (marginal)

- `~/scfv_v6/README.md` (52 L)
- `~/scfv-dsr/LICENSE`
- `~/scfv-dsr/.gitattributes`
- `~/scfv-dsr/.gitignore`

---

## §4 · Hallazgos consolidados

~120 hallazgos agrupados en 7 familias. Registro detallado en `bloque_Bbis_hallazgos.md`.

**F1 · Corpus sub-declarado.** El traspaso Ventana 10 declaró ~12 archivos. La realidad accesible es de ~30. La realidad declarada incluye ~3000 L privadas no accedidas.

**F2 · Confusión de repos en traspaso.** El "corpus fundacional raíz" fue declarado sin prefijo de ruta. 6/7 archivos están en `~/scfv-dsr/`, no en `~/scfv_v6/`.

**F3 · Numeraciones paralelas.** Cuatro cadenas cuaternarias de "separación". Cuatro marcas de versión del sistema + una del artefacto. Nomenclatura IA-1/IA-2/IA-3 vs IA-1/IA-2 + Operador. Numeración H-XXX vs HL-NNN.

**F4 · Documentos híbridos.** H7B, H7H, H8P_RETICULO, H9_EVALUACION, _EA_HALLAZGOS — todos mezclan estados.

**F5 · Falsos verdes.** `scfv_validator.py` retorna 0 sobre lista vacía. `seguridad/__init__.py` vacío con `test_cifrado` verde.

**F6 · Desincronización documental.** Contratos H9 vs estado real del Gate. Matriz anterior a Gate PASS. 51 `.bak_*` fuera de git. `HASHES.txt` no certifica gobernanza.

**F7 · Corpus autorreconocido.** `GENEALOGIA.md §9` declara las "anomalías" redescubiertas por B-bis como etapa previa confesada del Programa.

---

## §5 · Deudas nuevas

73 deudas D-BB-1..73. Registro detallado en `bloque_Bbis_deudas.md`.

Categorías principales: corpus y estructura · documentos híbridos · métricas y verificación · numeración paralela · seguridad y cifrado · corpus privado · gobernanza · régimen · deuda técnica · contenido del corpus.

Las deudas no se resuelven en esta acta. Se registran con ID para trazabilidad.

---

## §6 · Correcciones al traspaso Ventana 10

**Tres correcciones de contenido.**

### C1 · Ubicación del corpus fundacional

Traspaso declaró §4 y §6 sin prefijo de ruta, sugiriendo `~/scfv_v6/`. Realidad: 6/7 archivos en `~/scfv-dsr/`. Corrección: el corpus fundacional pertenece al repo `scfv-dsr`, no a `scfv_v6`.

### C2 · Régimen IA-3

Traspaso declaró §5: "IA-2 falsa antes de materializar · IA-3 aplica correcciones". Realidad doctrinal (H9 §10): régimen tripartito IA-1 + IA-2 + Operador. No existe IA-3.

### C3 · Ruta B-bis → C → D → E → F → G

Traspaso declaró una ruta secuencial. Realidad: el corpus documental del alcance B-bis está agotado. La ruta original no es ejecutable como estaba declarada.

---

## §7 · Correcciones a hallazgos Ventana 10

| Hallazgo Ventana 10 | Corrección |
|---|---|
| HC-1 "Constitución no aplicada" | ❌ FALSO · la Constitución de `scfv_v6` rige Materialización 1; DSR es Materialización 2; aplicación cruzada no corresponde |
| HC-2 "Contradicción Constitución ↔ Glosario" | ⚠️ NO ES CONTRADICCIÓN · tensión temporal declarada |
| HC-3 "ADRs nunca leídos" | ✅ confirmado · contextualizado: rigen M1, aplicables a M2 sólo por derivación |
| HC-4 "Tétrada sin consumidor" | ⚠️ AMBIGUO · tres "tétradas" coexisten sin reconciliación |
| HC-5/6 HUECOS genealógicos | ✅ confirmados · reencuadrados como parte del método deconstruccionista declarado |
| HC-7 `motor_causal.py` sin acta | ✅ confirmado |

**Bloque A · correcciones:**
- `var/scfv.db` sin identificar → resuelto (DB local inicializada por `scfv_dsr.cli init`).
- Corpus fundacional no leído → leído en B-bis.3.
- `perfiles/` vacío → patrón confirmado.

**Bloque B · 26 deudas D-B-1..26:**
Sin invalidación. La mayoría son hallazgos técnicos de `scfv-dsr`, aplicables como deuda del port, no del Programa.

---

## §8 · Correcciones a `_EA_MATRIZ_SINTESIS.md`

Resultado de B-bis.4.1:

```

Filas confirmadas sin cambio:         ~80
Filas a completar (PARCIAL):           ~7
Filas desactualizadas:                 ~6
Filas ambiguas:                        ~3
Filas nuevas a añadir:                ~65
Bloques nuevos a crear:                 5

```

Matriz actual: 111 filas · 13 bloques.
Matriz reformulada proyectada: ~176 filas · 18 bloques.

Los 5 bloques nuevos: PROGRAMA · GOBERNANZA · CORPUS NORMATIVO · CORPUS EVALUATIVO · CORPUS FUNDACIONAL.

La matriz no se reformula en B-bis. Se declara el resultado de la falsación y se difiere la reformulación a un acto futuro explícito.

---

## §9 · Corpus pendiente de acceso

**Privado:**
- `~/Programa-de-Investigacion-SCFV/`
  - `DOCUMENTO_FUNDACIONAL.md` (SHA256 `0dc00129…`)
  - `PROTOCOLO_MOTOR_RODRIGUIANO.md` (775 L · SHA256 `32d00154…`)
  - `ACTAS/ACTO_6_0_GENEALOGIA_OPERADA.md` (726 L · SHA256 `753e6a3f…`)
  - `ACTAS/ACTO_6_0_CONV_CONVERGENCIA.md` (583 L · SHA256 `7cd978ad…`)
  - `GIRO_05/REGISTRO_ACTOS.log`
  - 21 actas Giro 06 (referenciadas, no enumeradas)
  - 9 documentos fundacionales (referenciados, no enumerados)
  - BIBLIOTECA (referenciada, no definida)

**Técnico (accesible, fuera de alcance B-bis):**
- `~/scfv-dsr/scfv_dsr/**`
- `~/scfv_v6/PODERES/**`
- `~/scfv_v6/TESTS/**`
- `~/scfv_v6/INFRAESTRUCTURA/**`
- `~/scfv_v6/DOMINIOS/**`

**Auxiliar:**
- `LICENSE`, `.gitattributes`, `.gitignore`
- `~/scfv_v6/README.md` (52 L)
- `.bak_*` del corpus doctrinal

---

## §10 · Fronteras del acta

**Este acta NO declara:**
- Que el corpus documental esté completamente leído (existe `~/scfv_v6/README.md` y `LICENSE` no leídos).
- Que el corpus privado exista materialmente (sólo está declarado por `GENEALOGIA.md`).
- Que las 73 deudas D-BB tengan resolución.
- Que la matriz de síntesis esté reformulada.
- Que el corpus técnico haya sido auditado.
- Que la ruta del bloque siguiente esté decidida.

**Este acta SÍ declara:**
- Bloque B-bis cerrado con 25 archivos leídos · 6864 L.
- ~120 hallazgos y 73 deudas registradas.
- **Corpus documental del alcance B-bis agotado.** Corpus técnico y corpus privado pendientes.
- Tres correcciones formales al traspaso Ventana 10.
- Tres correcciones a hallazgos Ventana 10.

---

## §11 · Propuesta de IA-1 (no vinculante)

La decisión de ruta pertenece al Operador. La propuesta de IA-1 es:

- **C-γ primero** · reformular la ruta B→G a la luz de la estructura Programa↔Materialización. Costo bajo, claridad metodológica.
- **C-β segundo** · auditar corpus técnico de `scfv-dsr` (~60 archivos). Cierra D-BB-8, 9, 10, 19, 28, 58.
- **C-α en paralelo** si el Operador autoriza acceso al corpus privado `~/Programa-de-Investigacion-SCFV/`. Cierra D-BB-61..67, 71.

Sin decisión adoptada en esta acta.

---

## §12 · Estado del repo al cierre

```

HEAD                    6e94733
origin/main             6e94733
git status              limpio
Untracked               .coverage · scfv_dsr.svg
DSL                     7/7 verdes
Test juez FASE 2.a      8/8 verdes
DB original             285 eventos · CADENA_INTEGRA
B-bis                   25 archivos leídos · 0 commits de código · 0 escrituras al árbol productivo

```

---

## §13 · Cierre

```

Bloque B-bis             ✅ CERRADO
B-bis.0..3               ✅ corpus leído
B-bis.4.1                ✅ falsación de matriz
B-bis.4.2                ✅ acta
B-bis.4.2-bis            ✅ addenda correctiva
B-bis.5.x                ⏸ materialización en curso (este documento es 5.1)

Próximo acto             decisión del Operador sobre ruta C-α / C-β / C-γ
Commit                   pendiente

```

**El corpus documental del alcance B-bis está agotado. El corpus técnico y el corpus privado están pendientes. La ruta B→G está obsoleta en su forma original.**

Se cierra Bloque B-bis.

---

**Fin del acta.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
