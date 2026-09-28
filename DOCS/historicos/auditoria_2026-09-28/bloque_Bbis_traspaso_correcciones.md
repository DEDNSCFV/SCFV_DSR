# Bloque B-bis · Correcciones al traspaso y a hallazgos de Ventana 10

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** B-bis.0..3 (25 archivos · 6864 L).
**Naturaleza:** registro de correcciones formales. No modifica el traspaso original. No modifica hallazgos previos.

---

## §0 · Objeto

El traspaso de Ventana 10 → Ventana 11 contiene imprecisiones factuales que B-bis descubrió al leer el corpus por primera vez. Algunos hallazgos de Ventana 10 requieren corrección por cambio de contexto.

Este documento:
- no modifica el traspaso original (que permanece como fue emitido),
- no modifica los archivos `bloque_A_inventario.md` ni `bloque_B_estatico.md`,
- sí registra las correcciones para uso futuro.

Las correcciones son de dos tipos:
- **C** · correcciones al traspaso Ventana 10 → Ventana 11.
- **HC** · correcciones a hallazgos normativos de Ventana 10.

---

## §1 · Correcciones al traspaso (C1–C3)

### C1 · Ubicación del corpus fundacional

**Traspaso declaró** (§4 y §6): listó `DOCUMENTO_FUNDACIONAL.md`, `GENEALOGIA.md`, `HASHES.txt`, `README.md`, `VERSION`, `CHANGELOG.md`, `CONTRIBUTING.md` sin prefijo de ruta, sugiriendo `~/scfv_v6/`.

**Realidad verificada:**

```

~/scfv-dsr/DOCUMENTO_FUNDACIONAL.md
~/scfv-dsr/GENEALOGIA.md
~/scfv-dsr/HASHES.txt
~/scfv-dsr/VERSION
~/scfv-dsr/CHANGELOG.md
~/scfv-dsr/CONTRIBUTING.md
~/scfv-dsr/README.md                    (contenido propio)
~/scfv_v6/README.md                     (contenido distinto · 52 L · no leído en B-bis)

```

6 de 7 archivos en `~/scfv-dsr/`. Sólo `README.md` existe en ambos repos (con contenidos distintos).

**Corrección:** el corpus fundacional declarado pertenece al repo `scfv-dsr`, no a `scfv_v6`.

**Causa probable:** el traspaso confundió los dos repos al escribirse, o asumió que "corpus" ≡ `scfv_v6`.

**Consecuencia:** la distinción entre Materialización 1 (`scfv_v6`) y Materialización 2 (`scfv-dsr`) no fue reflejada en el traspaso.

### C2 · Régimen IA-3

**Traspaso declaró** (§5): *"IA-2 falsa antes de materializar · IA-3 aplica correcciones."*

**Realidad doctrinal verificada** (`H9_GATE_S0_CONTRATO.md §10`, precisión tripartita 2026-09-14):

> *"Los cierres metodológicos del Programa SCFV son tripartitos: IA-1 + IA-2 + Operador. — IA-1 aporta la interpretación arquitectónica del cierre. — IA-2 aporta la verificación de que los falsadores fueron satisfechos. — Operador aporta la decisión final y firma. Ninguno de los tres es suficiente por separado."*

No existe IA-3. El régimen operativo es tripartito.

**Corrección:** el régimen vigente es **IA-1 + IA-2 + Operador**. La nomenclatura "IA-3" fue una imprecisión del traspaso.

**Consecuencia:** la auditoría de Ventana 11 se ejecutó bajo régimen tripartito (Operador autoriza · IA-1 interpreta · IA-2 falsa).

### C3 · Ruta B-bis → C → D → E → F → G

**Traspaso declaró** (§4): *"Ruta: B-bis → C (comportamiento) → D (DB) → E (contratos) → F → G."*

**Realidad verificada:** el corpus documental del alcance B-bis está agotado.

Lo que B-bis cubrió:
- corpus normativo (ADRs 000-005),
- corpus evaluativo previo (H6 → S0_CIERRE),
- corpus fundacional raíz (7 archivos).

Lo que **no** fue parte del alcance declarado de B-bis pero permanece pendiente:
- corpus técnico (`~/scfv-dsr/scfv_dsr/**`, `~/scfv_v6/PODERES/**`, `~/scfv_v6/TESTS/**`, `~/scfv_v6/INFRAESTRUCTURA/**`, `~/scfv_v6/DOMINIOS/**`),
- corpus privado (`~/Programa-de-Investigacion-SCFV/`).

**Corrección:** la ruta secuencial B-bis → C → D → E → F → G presupone que el corpus documental es finito y accesible secuencialmente. La realidad del corpus tiene estructura diferente:

```

PROGRAMA
│
├── MATERIALIZACIÓN 1 · ~/scfv_v6/
│     corpus documental (parcialmente cubierto en B-bis)
│     corpus técnico (pendiente)
│
├── MATERIALIZACIÓN 2 · ~/scfv-dsr/
│     corpus fundacional (cubierto en B-bis.3)
│     corpus técnico (pendiente)
│
└── corpus privado (~/Programa-de-Investigacion-SCFV/)
pendiente

```

La ruta original no es ejecutable tal como estaba declarada. Su reformulación es decisión del Operador.

---

## §2 · Correcciones a hallazgos normativos de Ventana 10 (HC)

### HC-1 · "Constitución no aplicada"

**Ventana 10 declaró** (hallazgo `HC-1`): la Constitución no está aplicada a DSR.

**Corrección:** el hallazgo es **falso** por contexto. La Constitución (`~/scfv_v6/DOCS/gobernanza/constitucion.md`) rige **Materialización 1** (`scfv_v6`). DSR es **Materialización 2**, un artefacto autónomo declarado en `README.md`:

> *"El paquete no depende del corpus S0 (`scfv_v6`). Es portable."*

Aplicar la Constitución de M1 a M2 es un cruce de materializaciones que el propio Programa declara innecesario. **HC-1 no es un hallazgo: es una inferencia mal planteada.**

### HC-2 · "Contradicción Constitución ↔ Glosario"

**Ventana 10 declaró** (`HC-2`): existe contradicción entre la Constitución y el Glosario.

**Corrección:** no es contradicción. Es **tensión temporal declarada**. La Constitución (26-08-2026) declara prevalencia sobre documentación anterior que la contradiga, pero ella misma pertenece al corpus v6 y cita rutas de esa era (`src/`, `docs/gobernanza/`, `docs/adrs/`). El propio Documento Fundacional §28 y GENEALOGIA §9 reconocen esta capa temporal.

**HC-2 debe reformularse** de "contradicción" a "tensión temporal documentada".

### HC-3 · "ADRs nunca leídos"

**Ventana 10 declaró** (`HC-3`): los ADRs nunca fueron leídos.

**Corrección:** el hallazgo es verdadero pero requiere contextualización. Los ADRs rigen Materialización 1. Su aplicabilidad a Materialización 2 es por derivación, no por vigencia directa. La lectura de B-bis.1 los cubrió íntegros (439 L), y confirma que su relación con DSR es indirecta.

**HC-3 se mantiene** con la precisión de que los ADRs son corpus de M1.

### HC-4 · "Tétrada sin consumidor"

**Ventana 10 declaró** (`HC-4`): la tétrada ontológica constitucional no tiene consumidor.

**Corrección:** el hallazgo es **ambiguo**. Existen tres "tétradas" o "cuaternas" en el corpus sin reconciliación:

- **ADR-004**: axiomas E-1 (Similitud ≠ Evidencia), E-2 (Integridad ≠ Veracidad), E-3 (Soporte ≠ Decisión), más C = f(r,s,o,t,v). Cuatro términos.
- **Documento Fundacional §21 · GENEALOGIA §4.2**: `NORMA ≠ INFERENCIA ≠ DECISIÓN ≠ ASIENTO`. Cuatro términos.
- **Documento Fundacional §17**: `propuesta → decisión → ejecución`. Tres términos.
- **ADR-001**: cuatro autoridades (Epistemológica, Profesional, Contable, Demostrativa).

**HC-4 debe reformularse** como "cuatro cadenas cuaternarias paralelas sin reconciliación" (D-BB-68).

### HC-5/HC-6 · HUECOS genealógicos

**Ventana 10 declaró** (HC-5, HC-6): huecos genealógicos abiertos (proceso de cambio arquitectónico no aplicado · clausura de `motor_causal.py` sin documento).

**Corrección:** los huecos son **reales** pero requieren reencuadre. El Documento Fundacional §7 (deconstrucción) y §28 (no inmunización) explican que la investigación admite transformaciones sin cierre inmediato. Los huecos no son fallas de auditoría: son **estado declarado del propio Programa**.

**HC-5/HC-6 se mantienen** con la precisión de que no son defectos sino consecuencias del método.

### HC-7 · `motor_causal.py` eliminado sin acta

**Ventana 10 declaró** (`HC-7`): `motor_causal.py` eliminado sin acta.

**Corrección:** sin cambios. `motor_causal.py` fue activo al 06-09 y su clausura no tiene documento. **HC-7 confirmado** (HUECO-GENEALOGICO-02).

### HC-8/HC-9/HC-10

**Sin cambios.** B-bis no altera su contenido.

---

## §3 · Correcciones a hallazgos factuales del Bloque A

Bloque A declaró "registros factuales" pendientes de resolución. B-bis los resolvió parcialmente.

| Hallazgo Bloque A | Corrección B-bis |
|---|---|
| `fpdf` no declarada | confirmado como deuda del port DSR |
| imports sin prefijo `scfv_dsr.` | confirmado |
| `var/scfv.db` sin identificar | resuelto · DB local inicializada por `scfv_dsr.cli init` (README) |
| `perfiles/` vacío en DSR | patrón confirmado · coherente con etapa previa (GENEALOGIA §9.1) |
| corpus fundacional no leído | resuelto en B-bis.3 |

---

## §4 · Correcciones a hallazgos del Bloque B (D-B-1..26)

B-bis no invalida ninguna de las 26 deudas D-B-1..26.

**Precisión de contexto:** la mayoría son hallazgos técnicos de `scfv-dsr`. Aplican como **deuda del port**, no del Programa. El port es una materialización derivada (M2); sus deudas técnicas son locales al artefacto.

Sin corrección de contenido.

---

## §5 · Balance de correcciones

```

Correcciones al traspaso:             3 (C1 · C2 · C3)
Correcciones a hallazgos Ventana 10:  3 (HC-1 falso · HC-2 no contradicción · HC-4 ambigua)
Correcciones Bloque A:                5 (var/scfv.db resuelto · corpus fundacional resuelto · fpdf confirmado · prefijos confirmado · perfiles confirmado)
Correcciones Bloque B:                0 de contenido · 1 de contexto (deuda del port ≠ deuda del Programa)

```

Ninguna corrección modifica archivos previos. Todas quedan registradas para uso futuro.

---

## §6 · Estado

```

C1 · Ubicación corpus fundacional      REGISTRADA
C2 · Régimen IA-3                      REGISTRADA
C3 · Ruta B-bis → C → D → E → F → G    REGISTRADA
HC-1 · Constitución no aplicada        CORREGIDA (falso por contexto)
HC-2 · Contradicción C↔G               CORREGIDA (no es contradicción)
HC-3 · ADRs nunca leídos               PRECISADA (rigen M1)
HC-4 · Tétrada sin consumidor          REFORMULADA (4 cadenas paralelas)
HC-5/6 · HUECOS genealógicos           PRECISADOS (parte del método)
HC-7 · motor_causal sin acta           CONFIRMADA

```

---

**Fin del registro de correcciones.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
