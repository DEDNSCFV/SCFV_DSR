# M1.γ · INFRAESTRUCTURA · auditoría del corpus técnico

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Ventana:** 12.
**Bloque:** M1.γ (sub-bloque de M1 · corpus técnico).
**Naturaleza:** inventario SQL + mapa de persistencia + reconciliación runtime/declarativo + trazabilidad de inicialización.

---

## §0 · Metadatos

```

Ventana:               12
Fecha:                 2026-09-28
Bloque:                M1.γ
Subpasos:              M1.γ.0 ... M1.γ.4
Base medida:           ~/scfv_v6/INFRAESTRUCTURA + ~/scfv_v6/scfv*.db
HEAD scfv-dsr previo:  a1e12db

```

---

## §1 · Magnitud

### Volumen bruto

```

40 archivos       130.189 B   ~130 KB

```

### Desglose por tipo

```

SQL      18 archivos   1.326 L
Shell     3 archivos     191 L
Markdown  5 archivos     214 L
CSV       4 archivos      36 L
Python    4 archivos       0 L  (solo init.py vacíos)
TXT       1 archivo        0 L  (requirements.txt)
DB        1 binario   49.152 B  (INFRAESTRUCTURA/db/scfv.db)

```

No hay backups `.bak*` en este árbol.

---

## §2 · Subpasos ejecutados

```

M1.γ.0  INVENTARIO INFRAESTRUCTURA   ✓ estructura + fuente
M1.γ.1  MAPA SQL                     ✓ tablas declaradas + scfv.db
M1.γ.2  RECONCILIACION SQL/DB        ✓ divergencia declarado vs runtime
M1.γ.3  INICIALIZACION DB            ✓ (con bug de sintaxis grep declarado)
M1.γ.4  RE-EJECUCION                 ✓ corrección + hallazgos adicionales

```

---

## §3 · Hallazgos estructurales

### Corpus SQL declarativo

```

schema_final.sql          663 L · 26 CREATE TABLE
migrations/               17 archivos SQL · 001 ... 017
schemas/                  5 archivos .md por concepto

```

`schema_final.sql` declara 26 tablas, agrupadas en:

```

negocio_*       (17 tablas)  contabilidad, ventas, compras, inventario, fiscal, PCU, periodos
auditoria_*     (5 tablas)   hash_chain, event_store, event_processing, sagas, bitacora
epistemic_*     (3 tablas)   observacion, proposicion, orientacion
contexto_*      (2 tablas)   negocio_contextos, contexto_version
trabajos_*      (2 tablas)   solicitados, realizados
checkpoints     (1 tabla)

```

### Divergencia SQL declarativo ↔ runtime SQLite

```

Declarado en schema_final.sql:     26 tablas
Materializado en scfv.db runtime:   2 tablas
event_store         20 filas
negocio_diario       4 filas

```

No hay paridad. La DB runtime es un mínimo esqueleto operativo, no materialización del esquema declarado.

### Seis SQLite en el árbol

```

~/scfv_v6/scfv.db                      110.592 B  ·  11-Sep  ·  7 tablas (event_store + negocio_diario + 3 proyecciones + 2 trabajos)
~/scfv_v6/scfv.db.baseline_v81          81.920 B  ·  01-Sep  ·  6 tablas
~/scfv_v6/scfv.db.g24e_test             90.112 B  ·  03-Sep  ·  7 tablas (con schema_migrations)
~/scfv_v6/scfv_h6_5.db                  12.288 B  ·  11-Sep  ·  1 tabla
~/scfv_v6/scfv_tui.db                   12.288 B  ·  12-Sep  ·  1 tabla
~/scfv_v6/INFRAESTRUCTURA/db/scfv.db    49.152 B  ·  31-Ago  ·  2 tablas

```

`g24e_test` es la única con `schema_migrations` — pista de una línea migratoria histórica.

La DB raíz contiene tres proyecciones y un trigger:

```

proyeccion_decisiones_h2        10 filas
proyeccion_integridad_hash       1 fila
proyeccion_resumen_eventos       1 fila
trigger actualizar_decisiones_h2 se dispara en INSERT de ASIENTO_REGISTRADO

```

### Persistencia distribuida en PODERES

```

~30 puntos sqlite3.connect activos en PODERES
~12 CREATE TABLE desde Python

```

Módulos que crean tablas directamente:
```

event_store.py               → event_store
proyeccion_diario.py         → negocio_diario
integrador.py                → proyeccion_integridad_hash · proyeccion_cambios_dsl · proyeccion_resumen_eventos
reportes.py                  → negocio_productos

```

Ruta por defecto `sqlite3.connect("scfv.db")` es **relativa**. La DB concreta depende del `cwd`. Eso explica la multiplicación de `scfv*.db`.

### Divergencia de esquema `event_store`

`event_store.py` crea:
```sql
id INTEGER PRIMARY KEY
tipo_evento TEXT NOT NULL
payload TEXT NOT NULL
correlation_id TEXT NOT NULL
idempotency_key TEXT UNIQUE NOT NULL
hash_previo TEXT NOT NULL
hash_actual TEXT NOT NULL
timestamp INTEGER NOT NULL
version_contexto TEXT
```

INFRAESTRUCTURA/db/scfv.db tiene:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
event_id TEXT UNIQUE NOT NULL        ← columna extra ausente en runtime
tipo_evento TEXT NOT NULL
timestamp INTEGER NOT NULL           ← orden distinto
payload TEXT NOT NULL
version_contexto TEXT NOT NULL       ← NOT NULL, en runtime es nullable
...
```

Si el código operara contra esa DB, INSERT fallaría por constraint event_id NOT NULL.

Migraciones sin aplicador

Ningún módulo Python ni shell referencia migrations/ como mecanismo de aplicación. Las referencias textuales a "migracion" son a DOCS/migracion_v82.md.

Las 17 migraciones son corpus declarativo histórico, no cadena operativa verificada.

Cuarto corpus declarativo no catalogado

```
~/scfv_v6/proyecciones/sql/proyeccion_decisiones_h2.sql
```

Árbol fuera de INFRAESTRUCTURA. Tercera fuente declarativa paralela (INFRAESTRUCTURA + proyecciones + SQL embebido en Python).

---

§4 · Observaciones

```
O24  migrations/ va de 001 a 017 sin huecos
O25  schema_final.sql (663 L) vs 17 migraciones (636 L): ¿coincide?
O26  requirements.txt = 0 L (canónico del ecosistema Python, vacío)
O27  backups/ contiene scripts, no backups
     ejecutar_pruebas.sh · backup.sh · backup_local.sh
O28  examples/ con 4 CSV: datasets de demostración
O29  Seis scfv.db distintas · DB canónica no declarada
O30  schemas/ 5 .md para 17 migraciones: desproporción
O31  negocio_pcu duplicado en schema_final.sql (líneas 15 y 546)
     Segundo bloque incluye migración 013 con constraints relajados
O32  Migración 013 recrea negocio_pcu standalone (tercera declaración)
O33  auditoria_normativa: tipo de trabajo, no tabla
O34  checkpoints declarada pero no referenciada por PODERES
O35  4 tablas referenciadas en PODERES sin materializar en runtime
     negocio_inflacion · negocio_tasas_cambio · negocio_monedas · negocio_productos
O36  3 proyecciones en DB raíz sin código consumidor identificado
     (definidas por trigger, no por código)
```

---

§5 · Errores propios declarados

```
E7  Sintaxis incorrecta en M1-M4 de M1.γ.3
    '! -path *__pycache__*' es sintaxis de find, no de grep
    Grep tomó ! · -path · *__pycache__* como argumentos posicionales
    Los vacíos de M1-M4 eran falsos negativos por bug

E8  Error de lectura en L2 de M1.γ.2
    auditoria_normativa contado como nombre de tabla
    Es literal de argparse choices=["...auditoria_normativa..."]
```

---

§6 · Deudas

```
D-γ-DB-1       Multi-persistencia SQLite (6-7 DBs) sin DB canónica declarada
D-γ-DB-2       scfv_diario.db (exportador.py) · séptima DB no catalogada
D-γ-SQL-1      Cadena migratoria sin aplicador activo
D-γ-SQL-2      negocio_pcu declarado 4 veces con divergencia de constraints
D-γ-SQL-3      event_store divergente entre DB declarada y runtime
D-γ-CORPUS-1   proyecciones/sql/ no catalogado en M1.0
D-γ-DB-3       Ruta por defecto 'scfv.db' relativa · dependencia de cwd
```

---

§7 · Cierre

INFRAESTRUCTURA/: corpus SQL declarativo (schema_final + 17 migraciones) sin aplicador activo, sin paridad con la DB runtime. Persistencia efectiva distribuida en ~30 puntos SQLite con ruta relativa. Seis DB en el árbol con esquemas divergentes. Proyecciones creadas por trigger y por código Python, ambas coexistiendo. Cuarto corpus declarativo en ~/scfv_v6/proyecciones/sql/ no inventariado en M1.0.

El subsistema INFRAESTRUCTURA declara una arquitectura objetivo (26 tablas) que el runtime nunca materializa. La divergencia entre capa declarativa y capa operativa es estructural, no accidental.

---

Fin del acta M1.γ.
