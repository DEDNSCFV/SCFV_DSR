# M-deudas · Catálogo consolidado de deudas registradas y su estado actual

**Estado:** MATERIALIZACIÓN CERRADA · catálogo provisional · DC-1 abierta.
**Fecha:** 2026-09-28.
**Ventana:** 12.
**Bloque:** M-deudas.
**Naturaleza:** reconciliación ID por ID de las deudas registradas en la auditoría externa V10–V12.

---

## §0 · Metadatos

```

Ventana:               12
Fecha:                 2026-09-28
Bloque:                M-deudas
Base:                  actas V10 + V11 + M1.α + M1.β + M1.γ + M1.δ + C-γ + canon D-CONV
HEAD scfv-dsr previo:  c7057c7
Método:                reconciliación ID por ID · no suma de rangos
Estatuto:              materialización cerrada · catálogo provisional
Deuda interna abierta: DC-1

```

---

## §1 · Regla de construcción

```

ID único
↓
familia
↓
documento origen
↓
estado actual
ABIERTA · CONFIRMADA · REFORMULADA · RETIRADA
CERRADA DOCUMENTALMENTE · CERRADA VERIFICADA
REFERENCIA CORRECTIVA
↓
sucesora o nota

```

Reglas operativas:

```

R1  IDs encontrados ≠ deudas de la familia
R2  ID registrado   ≠ deuda vigente
R3  Cuando una misma acta contiene una anotación descriptiva
contradicha por una sección formal de estados, prevalece
la sección formal, salvo que una sección posterior del
mismo documento la modifique expresamente.
R4  El catálogo consolida documentalmente. No verifica unicidad
inter-familias. DC-1 declarada abierta.
R5  Un cierre declarado por acta externa se registra como
CERRADA DOCUMENTALMENTE cuando no cita fundamento material.
No se registra como CERRADA VERIFICADA.
R6  Los rangos de familia no heredan estado homogéneo. Cada
rango se declara "registradas · estado individual según
detalle siguiente".

```

---

## §2 · Familia D-B · 26 registradas

Origen: bloque_B_estatico.md §7.

```

D-B-1..15    CONFIRMADAS   (C-β §6)
D-B-16..19   REFORMULADAS  (C-β correcciones:133)
· objeto: Tetrada dataclass (7 campos) ≠ 3 cadenas cuaternarias textuales
· identidad histórica conservada · ID vigente
· no hay sucesión a otro ID
D-B-20..26   CONFIRMADAS   (C-β §6)

```

Total: 26 registradas · 22 confirmadas · 4 reformuladas · 0 retiradas · 0 cerradas.

---

## §3 · Familia D-BB · 73 registradas · estado individual según detalle

Origen: bloque_Bbis_deudas.md §1-§17.

```

D-BB-1..14    ABIERTAS
D-BB-15       anotación "(resuelta)" en fila · §17 no lo ratifica
· ABIERTA por R3
D-BB-16..18   ABIERTAS
D-BB-19       REFORMULADA (C-β)
D-BB-20..57   ABIERTAS
D-BB-58       CERRADA DOCUMENTALMENTE (C-β §6)
· fundamento material no citado · verificación pendiente · DC-10
D-BB-59..73   ABIERTAS

```

Total: 73 registradas · 71 abiertas · 1 reformulada · 0 retiradas · 1 cerrada documentalmente.

---

## §4 · Familia D-IMP · 2 registradas

Origen: bloque_Bbis_deudas.md §15 · H8P_IMPORTADOR §22.4.

```

D-IMP-01    ABIERTA
D-IMP-02    ABIERTA

```

Familia separada de D-BB · 2 IDs.

---

## §5 · Familia D-C · 88 registradas · estado individual según detalle

Origen: bloque_C_beta_deudas.md.

```

D-C-1..8      ABIERTAS
D-C-9         RETIRADA · artefacto de transcripción
D-C-10..21    ABIERTAS
D-C-22        RETIRADA · PersistenciaViolacion existe en serializador_canonico.py
D-C-23..42    ABIERTAS
D-C-43        anotación "(resuelta en C-β.4-bis)" en fila
· §11 la declara ABIERTA por R3
D-C-44..88    ABIERTAS

```

Total: 88 registradas · 86 abiertas · 2 retiradas.

---

## §6 · Familia D-Cα · 126 registradas · estado individual según detalle

Origen: bloque_C_alpha_deudas.md.

```

D-Cα-1..99     ABIERTAS
D-Cα-100       RETIRADA · ACTA_ACTIVACION_HEVNER distingue con precisión
D-Cα-101..126  ABIERTAS

```

Total: 126 registradas · 125 abiertas · 1 retirada.

Referencia correctiva adicional · no computa como deuda del cuerpo:

```

D-Cα-127       REFERENCIA CORRECTIVA
· no es fila de bloque_C_alpha_deudas.md
· asignada en bloque_C_alpha_correcciones.md:117
· descripción: "Patrón E tiene 4 detectores verificables, no 3"

```

Nota: la tabla de bloque_C_alpha_deudas.md tiene 127 filas físicas por doble aparición de D-Cα-100 (§5 y §7). Los IDs únicos son 126.

---

## §7 · M1 · 29 deudas técnicas + 6 metodológicas

### M1.α · PODERES · 5

```

D-M1α-1   9 archivos .bak.py en raíz de PODERES
D-M1α-2   Tres invariantes .md vacíos en FORMAL/
D-M1α-3   Candidatos a no-consumidos por import textual
D-M1α-4   Módulos aislados puros
D-M1α-5   Discrepancia 82 vs 72+9 en *.py

```

### M1.β · TESTS · 8

```

D-M1β-1   19 módulos PODERES sin test directo
D-M1β-2   Cuatro tests monolíticos · NATURALEZA CUESTIONADA · revisar antes de intervenir
D-M1β-3   test_integracion.py vacío
D-M1β-4   Subdirectorios sin contenido
D-M1β-5   resultados.txt sistema paralelo · NATURALEZA CUESTIONADA · revisar antes de intervenir
D-M1β-6   Un test skipped sin identificar
D-M1β-7   Cero conftest.py · NATURALEZA CUESTIONADA · revisar antes de intervenir
D-M1β-8   test_f3b4_infra_f.py nombre no convencional · NATURALEZA CUESTIONADA · revisar antes de intervenir

```

### M1.γ · INFRAESTRUCTURA · 7

```

D-γ-DB-1      Multi-persistencia SQLite sin canónica
D-γ-DB-2      scfv_diario.db · séptima DB
D-γ-DB-3      Ruta por defecto 'scfv.db' relativa
D-γ-SQL-1     Cadena migratoria sin aplicador
D-γ-SQL-2     negocio_pcu declarado 4 veces
D-γ-SQL-3     event_store divergente
D-γ-CORPUS-1  proyecciones/sql/ no catalogado

```

### M1.δ · DOMINIOS · 9

```

D-M1δ-1   DOMINIOS desconectado del runtime
D-M1δ-2   BaseFractal.init incompatible
D-M1δ-3   Docstring huérfano + import duplicado
D-M1δ-4   fiscal.py accede a tablas no materializadas
D-M1δ-5   READMEs documentan 6-15x lo implementado
D-M1δ-6   .scfv declaran reglas no implementadas · NATURALEZA CUESTIONADA · revisar antes de intervenir
D-M1δ-7   base_fractal.py huérfano
D-M1δ-8   inventario.py stub vacío
D-M1δ-9   Dominio fiscal sin test

```

### DM · metodológicas · 6

```

DM-1  Comandos grep con sintaxis incorrecta
DM-2  Saltos en la secuencia declarada
DM-3  IA-1 e IA-2 sin separación de turnos
DM-4  Numeración O1..O43 sin índice
DM-5  Deudas fragmentadas por bloque
DM-6  Correcciones retroactivas no versionadas

```

---

## §8 · Anomalías y errores documentales · reclasificados

### ERROR DEL CORPUS

```

A1   C-β §6 "3" cuenta categorías, no IDs
A7   V11 §3 declara D-Cα-1..129 · catálogo dice 1..126
A10  C-γ §1 declara "21 archivos" · el directorio tiene 26

```

### AMBIGÜEDAD DOCUMENTAL INTERNA · resuelta por R3

```

A2   D-BB-15 anotación / §17 → §17 prevalece
A3   D-C-43 anotación / §11 → §11 prevalece

```

### CORRECCIÓN DE CATALOGACIÓN · ya resuelta

```

A4   D-Cα-127 fuera de bloque_C_alpha_deudas.md

```

### ARTEFACTO ARITMÉTICO · ya explicado

```

A5   127 filas por doble aparición de D-Cα-100

```

### CUESTIÓN DE ALCANCE · genealogía de DC-8

```

A6   D-CONV en Programa privado · alcance externo
A8   D-CONV-4 aparece reformulada en acta C-α:176
A9   D-CONV-4 aparece retirada "como activa" en correcciones C-α:261
→ A8 y A9 originan DC-8

```

---

## §9 · Errores propios declarados de la auditoría

**Categoría separada de las deudas del corpus.**

```

E1    Filtro de backups incompleto '.bak_*' no captura '.bak.py'
E2    Patrón grep '[A-Za-z_.]+' trunca nombres con dígitos
E3    A3 generó falsos positivos por no excluir entrypoints
E4    A2 pudo inflar por doble for other in ...
E5    H3 de M1.β con patrón 'from $m( |$)' no captura 'import X as Y'
E6    H3 mal leído: intellectus.intellectus
E7    Sintaxis '! -path' incorrecta en grep de M1.γ.3
E8    auditoria_normativa confundido con tabla
E9    Clasificar estado por palabra clave del defecto
E10   Leer "127 filas" como anomalía sin verificar duplicado
E11   "Sucesora D-C-13" para D-B-16..19 · es coexistencia, no sucesión
E12   Suma mecánica de rangos sin aplicar retiradas
E13   Suma global de dos corpus propuesta en versión previa del catálogo

```

---

## §10 · Balance consolidado · cuerpo SCFV-DSR

### Universo documental

```

313  =  D-B 26 + D-BB 73 + D-C 88 + D-Cα 126      (V10-V11)
37  =  D-IMP 2 + M1α-δ 29 + DM 6                 (V12)
───
350  registros del cuerpo SCFV-DSR
· 344 técnicas    (26+73+2+88+126+29)
· 6 metodológicas (DM)

```

### Partición por estado consolidado

```

341   restantes según partición consolidada
· no reformuladas · no retiradas · no cerradas
· no homogéneo como estado individual
5   reformuladas
· 4 en D-B  → D-B-16..19
· 1 en D-BB → D-BB-19
3   retiradas
· 2 en D-C  → D-C-9 · D-C-22
· 1 en D-Cα → D-Cα-100
1   cerrada documentalmente
· 1 en D-BB → D-BB-58 · DC-10
───
350

```

Nota: D-CONV-4 y D-CONV-11 no participan del cómputo 350. Son anexo.

Nota: la cifra 341 es un residuo aritmético. No es una categoría de estado homogénea.

### Registros por familia

```

Familia    Registradas   Abiertas   Reform.   Retir.   Cerr.doc.   Ref.corr.
D-B        26            22         4         0        0           0
D-BB       73            71         1         0        1           0
D-IMP       2             2         0         0        0           0
D-C        88            86         0         2        0           0
D-Cα      126           125         0         1        0           1
M1 téc.    29            29         0         0        0           0
DM          6             6         0         0        0           0
──────────────────────────────────────────────────────────────────────
Cuerpo    350           341         5         3        1           1

```

Nota: la columna Ref.corr. es documental adicional. D-Cα-127 no computa dentro de los 126 registros de la familia.

---

## §11 · Anexo · D-CONV · deudas administrativas del Programa privado

**No pertenece al cuerpo SCFV-DSR. No se suma al total 350.**

Origen: ~/Programa-de-Investigacion-SCFV/ACTAS/ACTO_6_0_CONV_CONVERGENCIA.md §9.1.
Naturaleza: administrativa/metodológica del ciclo 6.0.
Referencia cruzada en scfv-dsr: D-Cα-8.

```

D-CONV-1   6.0.06 nombrada Díaz Navarro pero canon Fernández Otero/Navarro · media
D-CONV-2   21 actas untracked en git · alta
D-CONV-3   BIBLIOTECA/INVENTARIO.md + REGISTRO_ENTRADAS.log sin commitear · media
D-CONV-4   23 commits ahead de origin · media · REFORMULADA · DC-8 abierta
D-CONV-5   0 tags en 31 commits · alta
D-CONV-6   Sin firma GPG · baja
D-CONV-7   H-A5j · MONEDA/B101 sin reproducir · media
D-CONV-8   Prompt Giro 05 sin firmar · media
D-CONV-9   Sin CHANGELOG ni VERSION · media
D-CONV-10  Sin plan de V&V declarado · media
D-CONV-11  Sin declaración de ruta metodológica · alta · REFORMULADA (declarada, no migrada)
D-CONV-12  Sin LICENSE ni §contribución · media
D-CONV-13  L4 idempotencia · Decimal · nan/inf · ISO 8601 · baja
D-CONV-14  L5 cuentas PCU · TipoEvento · baja
D-CONV-15  L6 · 9 deudas genealógicas · alta

```

Total: 15 registradas · 13 abiertas · 2 reformuladas · 0 retiradas.

Estatuto: externas · no integradas a la auditoría externa 6.1 · no intervenibles como deuda técnica DSR.

---

## §12 · Deudas del propio catálogo

### DC ABIERTAS

```

DC-1    Deduplicación inter-familias NO verificada
· no afirma ausencia de duplicación
· afirma que el cruce todavía no fue ejecutado
· se resuelve en bloque posterior M-deudas.9

DC-8    D-CONV-4 contradicción reformulada/retirada PENDIENTE
· acta C-α:176 declara reformulada
· correcciones C-α:261 declara retirada "como activa"
· fuentes con distinto estatuto · no resoluble por decisión editorial
· queda en corpus privado

DC-9    5 deudas M1 con naturaleza cuestionada
· D-M1β-2 · D-M1β-5 · D-M1β-7 · D-M1β-8 · D-M1δ-6
· acción: revisión de naturaleza antes de intervenir

DC-10   D-BB-58 cierre documental sin fundamento material citado
· registrada como CERRADA DOCUMENTALMENTE (R5)
· no como CERRADA VERIFICADA

DC-14   D-Cα-127 "referencia correctiva"
· estatuto "externa" sin fuente explícita de procedencia
· el registro de la referencia sí consta en
bloque_C_alpha_correcciones.md:117
· lo pendiente es el fundamento para calificarla como "externa"

```

### DC INCORPORADAS EN ESTA VERSIÓN

```

DC-2    composición del "5 reformuladas" declarada en §10
DC-3    regla R3 declarada en §1
DC-4    errores propios separados en §9
DC-5    A1-A10 reclasificados en §8
DC-6    D-CONV en anexo separado §11
DC-7    particiones 313 + 37 = 350 y 341 + 5 + 3 + 1 = 350 declaradas
DC-11   rangos de familia con desglose individual
DC-12   341 rotulado como residuo aritmético
DC-13   estatuto global del documento declarado en §0 y §14

```

---

## §13 · Fuera de scope del catálogo

```

HL-1..412       numeración interna corpus privado · no deudas
5 D-* sin materialización individual

```

---

## §14 · Firma

El catálogo consolida 350 registros del cuerpo SCFV-DSR: 344 técnicas + 6 metodológicas. Particiones explícitas:

```

313 + 37 = 350
341 + 5 + 3 + 1 = 350
344 + 6  = 350

```

Anexo separado: 15 deudas administrativas del Programa privado, no sumables.

Cinco deudas del propio catálogo quedan abiertas: DC-1 · DC-8 · DC-9 · DC-10 · DC-14.
Nueve quedan incorporadas en esta versión: DC-2 · DC-3 · DC-4 · DC-5 · DC-6 · DC-7 · DC-11 · DC-12 · DC-13.

La resolución de DC-1 precede a cualquier intervención que dependa de la unicidad inter-familias. Las demás DC abiertas conservan sus propios actos de resolución y sus condiciones de intervención.

El catálogo no autoriza intervención por sí mismo. Es la base para priorizar.

---

**Fin del catálogo consolidado.**
**Materialización cerrada · catálogo provisional · DC-1 abierta.**
