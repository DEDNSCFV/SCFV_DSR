# Bloque C-α · Correcciones a hallazgos previos

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** C-α.0..6 (31 archivos · ~9,800 L).
**Naturaleza:** registro de correcciones formales. No modifica archivos previos.

---

## §0 · Objeto

La auditoría del corpus privado (`~/Programa-de-Investigacion-SCFV/`) descubre hechos que precisan, reformulan o contradicen hallazgos de bloques previos (Ventana 10 · Bloque A/B · Ventana 11 · B-bis · C-β).

Este documento registra cuatro tipos de corrección:

- **RETIRADA** · hallazgo previo que resultó ser artefacto o error de lectura.
- **REUBICACIÓN** · hallazgo previo correcto pero mal ubicado.
- **REFORMULACIÓN** · hallazgo previo correcto pero mal formulada la deuda asociada.
- **AMPLIACIÓN** · hallazgo previo correcto pero incompleto.
- **MATIZACIÓN** · hallazgo previo correcto pero con alcance mal precisado.

---

## §1 · Retiradas

### RET-α-1 · D-Cα-100

**Hallazgo declarado en C-α.5.20:** *"Contradicción: README declara DSR vs ACTA_ACTIVACION_HEVNER_GIRO_03 'No se adopta DSR'"*.

**Verificación en C-α.6.1:** `ACTA_ACTIVACION_HEVNER_GIRO_03 §2` establece con precisión:

> *"No se adopta DSR como metodología rectora. Se activa Hevner como fuente metodológica externa de contraste."*

Y distingue explícitamente dos categorías:
- **Adoptar DSR como metodología** — no.
- **Usar Hevner como canon externo de contraste** — sí.

**No hay contradicción.** El README declara *"Artefacto Design Science Research"*. La ACTA distingue la naturaleza del artefacto de la metodología rectora del Programa.

**RETIRADA.** Error de lectura de la IA.

### RET-α-2 · Referencias a D-CONV-4 (23 commits ahead)

**Hallazgo declarado en B-bis:** *"23 commits ahead de origin"*.

**Verificación en C-α.7.0:** el corpus privado está **sincronizado con origin** (`## main...origin/main` sin ahead/behind).

**REFORMULACIÓN:** la deuda D-CONV-4 estaba saldada al 28-09. Los 23 commits pendientes fueron pusheados entre el 26-09 (ProGit 6.0.15) y el 28-09 (verificación actual).

**RETIRADA como deuda activa.** Queda como constancia histórica.

---

## §2 · Reubicaciones

### REU-α-1 · D-BALDOR-IVA-1/2

**Hallazgo declarado en Ventana 10 Bloque B:** defecto IVA en Baldor.

**Verificación en C-α.2-bis:** `ACTA_A-1.3_CLASIFICACION_DEFECTO_NUMERICO.md` confirma:

> *"`iva = monto * IVA_TASA / 100000000` materializa una escala incompatible con `IVA_TASA = 0.12`."*
> *"El defecto es reproducible y no posee origen documental identificado en el corpus, `scfv_v6` ni en la historia Git revisada."*

**Ubicación real:** `scfv_architect.py` (M1 · plantilla histórica/inactiva de compras).

**REFORMULACIÓN:** el defecto NO está en `baldor.py` (M2) — está en `scfv_architect.py` (M1). El port corrigió la fórmula.

### REU-α-2 · D-CONV-15 (ubicación declarada)

**Hallazgo declarado en `_EA_HALLAZGOS` Bloque R:** deuda IVA del Giro 03.

**Realidad:** el hallazgo debe citar `ACTA_A-1.3_CLASIFICACION_DEFECTO_NUMERICO.md` como fuente primaria. La numeración `HL-176..180` son los hallazgos asociados en el corpus privado.

**REFORMULACIÓN:** D-CONV-15 = `H-DEUA13-01` = `ACTA_A-1.3` = `scfv_architect.py`. Cuatro nombres para el mismo objeto.

---

## §3 · Reformulaciones

### REF-α-1 · H-BB3-16 · "Descubrimiento del Programa"

**Hallazgo declarado en B-bis:** *"Descubrimiento del Programa de Investigación SCFV."*

**Realidad verificada en C-α.1:** el Programa tiene nombre, motor, protocolo y ancla formal desde 2026-09-10 (Documento Fundacional) y 2026-09-21 (Acta de Anclaje). El ciclo 6.0 (25-26 sep) cerró con 21 cánones.

**REFORMULACIÓN:** no fue *"descubrimiento"*. Fue **redescubrimiento** desde fuera. La auditoría externa (Ventana 11) redescubrió lo que el Programa ya había declarado en su corpus privado.

### REF-α-2 · H-BB3-17 · "Corpus privado no accedido"

**Hallazgo declarado en B-bis:** `~/Programa-de-Investigacion-SCFV/` no accedido.

**Realidad verificada en C-α.0:** existe · 813 archivos · 6.3 MB · verificado. Leído en C-α.1..6.

**REFORMULACIÓN:** el corpus privado está auditado externamente. La deuda D-BB-61 se cierra.

### REF-α-3 · Régimen tripartito asimétrico

**Hallazgo declarado en B-bis:** régimen tripartito (IA-1 + IA-2 + Operador).

**Realidad verificada en C-α.1:** el corpus privado nombra el régimen **"tripartito asimétrico"**. No es un tripartito simétrico.

- **Operador:** decide + suscribe + autoriza.
- **IA-1:** construye, redacta, integra. **Sin co-decisión.**
- **IA-2:** falsa, verifica. **Sin co-decisión.**

**REFORMULACIÓN:** el término correcto es **"tripartito asimétrico"** (o "suscripción + constancias"). No es "tripartito" simple.

### REF-α-4 · Patrón E · 3 detectores → 4 detectores

**Declarado por CONV §4.1:** Patrón E (firma no criptográfica) tiene 3 detectores: Merkle · NIST · ProGit.

**Verificado en C-α.5.19:** Romney (19) detecta **confidencialidad + privacidad ausentes** — misma familia del Patrón E.

**REFORMULACIÓN:** Patrón E tiene **4 detectores verificables**.

**D-Cα-127.**

### REF-α-5 · Nombres del Programa y artefactos

**Confusión acumulada:**

| Nombre | Referente |
|---|---|
| `SCFV` | Corpus doctrinal general |
| `SCFV v6` · `v6.1` | Corpus doctrinal M1 |
| `SCFV v8.2` | Ruta canónica M1 |
| `SCFV Motor 9.0.0` | Nombre declarado 13-09 |
| `SCFV_DSR` | Artefacto DSR (repo M2) |
| `SCFV_DSR E3` | Estado específico del artefacto auditado en Giro 06 |
| `SCFV_S0_V1.0.0` | Release público (commit `ca56309`) |
| `scfv_v6` | Directorio local del laboratorio S0 |
| `scfv-dsr` | Directorio local del artefacto DSR |
| `scfv_github` | Intento previo (3 commits · sin remote) |
| `Programa-de-Investigacion-SCFV` | Directorio local del corpus canónico |

**REFORMULACIÓN:** 5 árboles de ecosistema (declarados por GENEALOGIA_OPERADA §3.1), no 2. Cada nombre tiene referente distinto.

### REF-α-6 · Taxonomía canónica

**Hallazgo declarado en B-bis:** 4 cadenas cuaternarias paralelas (ADR-001 · GENEALOGIA §4.2 · Fundacional §17 · Fundacional §21).

**Realidad verificada en C-α.2:** la taxonomía canónica tiene **4 categorías**: aporía · frontera · límite · deuda.

**REFORMULACIÓN:** la cuaternidad del corpus privado **no son 4 cadenas** — es **una taxonomía de 4 estados** aplicable a hallazgos. Coherente con `GENEALOGIA_OPERADA D-9` (el CONV colapsó las 4 en 1).

**Nota sobre el uso propio:** la auditoría externa (B-bis · C-β · C-α) usa "deuda" como categoría única. **No aplica la taxonomía de 4.** Es una simplificación de la IA.

### REF-α-7 · D-CONV-11 (ruta metodológica)

**Declarado en CONV §9.1:** sin declaración de ruta metodológica.

**Verificado en C-α.6.1:** `GENEALOGIA_OPERADA` Enmienda C la declara *"resuelta en E-C: declarada, no migrada"*.

**Realidad:** la ruta está declarada en `Fundacional §26` (Sampieri como referencia central) y en `GIRO_02 §1` (método sampieriano ruta mixta CUAL-cuan).

**REFORMULACIÓN:** no es deuda de declaración — es **deuda de migración al E3**.

---

## §4 · Ampliaciones

### AMP-α-1 · H-Cα-51 (Lakatos) · núcleo firme declarado

**Declarado en C-α.4.10:** *"SCFV es programa lakatosiano de facto."*

**Verificado en C-α.6.1:** el `ACTA_ANCLAJE_PROGRAMA_SCFV §3` **materializa literalmente** el modelo lakatosiano:

```

NÚCLEO FIRME:      Rodríguez + XNOR + Máquina estados + DECISION_H2 + Fractalidad acotada
CINTURÓN:          SCFV_DSR + v8.2 + PODERES + corpus normativo + PCU + frameworks
FUERA:             Analogías privadas sin estatuto público

```

**AMPLIACIÓN:** Lakatos **no sólo audita** el artefacto (6.0.10). **El Programa lo aplica como marco declarado** desde 21-09.

### AMP-α-2 · H-Cα-2 (régimen) · precisión terminológica

**Declarado en C-α.1:** régimen tripartito asimétrico.

**Verificado en C-α.6.1:** el propio corpus privado declara el término exacto en `ACTA_ANCLAJE §0.1`:

```

Operador: emite, decide, firma
IA-1: construye (sin co-decisión)
IA-2: falsa (sin co-decisión)
Materializa: el Operador o IA-1 con delegación expresa (§19.3 Protocolo)

```

**AMPLIACIÓN:** el régimen incluye **delegación expresa** del Operador a IA-1 para materializar. No es sólo tripartito asimétrico; es tripartito con delegación.

### AMP-α-3 · H-Cα-42 (autofalsación Hevner)

**Declarado en C-α.4.08:** Hevner produce autofalsación del método.

**Verificado en C-α.6.1:** `ACTA_ACTIVACION_HEVNER_GIRO_03 §13` lista 7 condiciones cumplidas y una **pendiente**:

> *"6. Coordinación de la corrección de L80 — pendiente, acto paralelo."*

**AMPLIACIÓN:** la autofalsación del método es **verificable y trazable**. No es sólo declaración retórica. Tiene constancia documental.

---

## §5 · Matizaciones

### MAT-α-1 · H-Cα-52 (progresivo/regresivo)

**Declarado en C-α.4.10:** *"El Programa no declara si es progresivo o regresivo."*

**Verificado en C-α.6.1:** `ACTA_ANCLAJE §3` **sí declara núcleo/cinturón**.

**MATIZACIÓN:** el ancla declara núcleo/cinturón/fuera. **Falta sólo el calificativo "progresivo/regresivo"**. El programa sí tiene la estructura lakatosiana; lo que falta es el autodiagnóstico.

### MAT-α-2 · H-Cα-73 (decisiones tempranas)

**Declarado en C-α.5.16 (Reynoso):** *"Sin decisiones arquitectónicas tempranas registradas como ADR."*

**Verificado en C-α.6.1:** el corpus privado **sí tiene actas de decisiones tempranas**:
- `ACTA_ACTIVACION_HEVNER_GIRO_03`
- `ACTA_ANCLAJE_PROGRAMA_SCFV`
- `ACTA_CIERRE_GIRO_03`
- `ACTA_ENMIENDA_FRACTALIDAD_ACOTADA`

**MATIZACIÓN:** el corpus privado **tiene** las decisiones tempranas documentadas. **El E3 (`scfv-dsr`) no las referencia**. La deuda no es ausencia de ADR — es **falta de migración de las actas del Programa al artefacto**.

---

## §6 · Correcciones al traspaso Ventana 10

### T-α-1 · Ubicación del corpus fundacional

Sin cambio respecto a C2 de B-bis. El corpus fundacional está en `~/scfv-dsr/` (7 archivos) + `~/Programa-de-Investigacion-SCFV/` (resto).

### T-α-2 · Régimen IA-3

Sin cambio respecto a C2 de B-bis. No existe IA-3.

### T-α-3 · Ruta B-bis → C → D → E → F → G

Sin cambio respecto a C3 de B-bis. La ruta original no es ejecutable.

### T-α-4 · Corpus privado

**Nueva corrección:** el traspaso Ventana 10 declaró *"corpus fundacional raíz = 7 archivos"*. La realidad:
- 7 archivos en `~/scfv-dsr/`.
- ~813 archivos en `~/Programa-de-Investigacion-SCFV/`.
- 21 cánones + 3 consolidados + 4 actas clave + ~25 actas operativas + 126 archivos BIBLIOTECA + 114 logs GIRO_05.

**CORRECCIÓN:** el corpus fundacional del Programa es **mucho mayor** que lo declarado.

---

## §7 · Balance de correcciones

```

RETIRADAS              2 (D-Cα-100 · D-CONV-4 como activa)
REUBICADAS             2 (D-BALDOR-IVA · D-CONV-15)
REFORMULADAS           7 (H-BB3-16 · H-BB3-17 · régimen · Patrón E · nombres · taxonomía · D-CONV-11)
AMPLIADAS              3 (H-Cα-51 · H-Cα-2 · H-Cα-42)
MATIZADAS              2 (H-Cα-52 · H-Cα-73)
CORRECCIONES TRASPASO   1 nueva (T-α-4)

```

---

## §8 · Correcciones que quedan vigentes para futuras ventanas

1. **D-Cα-100** retirada · ACTA_ACTIVACION_HEVNER distingue con precisión.
2. **D-CONV-4** saldada · 23 commits ya pusheados al 28-09.
3. **D-BALDOR-IVA-1/2** reformulada · defecto en M1 `scfv_architect.py`, no en M2.
4. **Régimen** es **tripartito asimétrico con delegación expresa**, no tripartito simple.
5. **Patrón E** tiene **4 detectores** (Merkle + NIST + ProGit + Romney), no 3.
6. **Taxonomía canónica** es de **4 categorías** (aporía · frontera · límite · deuda).
7. **Lakatos** está materializado en `ACTA_ANCLAJE §3` — el Programa lo aplica, no sólo lo audita.
8. **Decisiones tempranas** están en el corpus privado, no en E3 — falta migración.
9. **5 árboles del ecosistema**, no 2.
10. **Ruta metodológica** declarada (Sampieri · Fundacional §26) pero no migrada a E3.

---

**Fin del registro de correcciones.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
