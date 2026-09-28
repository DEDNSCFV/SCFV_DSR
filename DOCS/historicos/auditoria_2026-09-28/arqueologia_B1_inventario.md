# ARQUEOLOGÍA DIACRÓNICA · B.1 · INVENTARIO
### Auditoría 2026-09-28 · ~/scfv-dsr

---

## 0 · Alcance

Primer bloque de arqueología diacrónica. Sólo lectura. Objetivo: determinar
si el repo DSR tiene historia de código que explique el estado actual de
los huérfanos detectados por vulture_60 y por el informe FASE 4.

Hallazgo sometido a falsación IA-2 en esta misma fecha. Dos correcciones
de alcance aplicadas: (a) distinción de mecanismos en §3, (b) sustitución
de "historia sustantiva" por formulación operacional en §7.

---

## 1 · Historia de commits con código

Desde `e0923e4` (c0 · Fundación) hasta HEAD, cuatro commits tocaron `.py`:

```

abb2bac  FASE 1 · Atomicidad transaccional
event_store.py +39 · h2.py +2 · orquestador.py +206/-83

4eca9d5  chore: autoflake
9 archivos · imports cosméticos · 5+/14-

015d6d4  FASE 2.a.1 · dedup suma_montos
evaluador.py -4

abd746e  FASE 2.a.2 · despacho Baldor
evaluador.py +17

```

Los cinco commits restantes (`e6f6d06`, `78eda31`, `1db6c90`, `7872fd4`,
`8404d01`) son documentales — sólo `.md` y `.txt`.

---

## 2 · Rastreo de símbolos huérfanos · git log -S

27 símbolos del vulture_60 verificados:

    validar_partida · validar_partida_doble · validar_I6
    generar_csv_diario · generar_csv_mayor · generar_csv_balance
    generar_pdf_diario
    obtener_hash_final · obtener_por_id · obtener_por_correlation
    union · interseccion · complemento · diferencia_simetrica
    es_subconjunto · es_particion · cuentas_huerfanas · complemento_set
    es_terminal · puede_asentar · puede_anular
    PartidaAutorizada · cuenta_version · ubicacion · es_fiscal
    ExaminadorEvidencia · examinar

Los 27 devuelven **sólo e0923e4**. Ningún commit posterior.

---

## 3 · Falsos negativos · dos mecanismos distintos, no uno

Tres símbolos devolvieron `git log -S` vacío:

    intellectus · dictum · reportes_motor

La investigación con `grep` sobre el contenido de cada archivo revela
que NO comparten un mecanismo único. Son dos mecanismos agrupando tres
casos.

### Grupo A · case-sensitivity · intellectus + dictum

Verificación:

    intellectus.py
      grep "intellectus"    → 0 matches
      grep "Intellectus"    → 6 matches (líneas 2, 7, 20, 25, 70, 105)

    dictum.py
      grep "dictum"         → 0 matches
      grep "Dictum"         → 2 matches (líneas 2, 7)

Mecanismo: `git log -S` es case-sensitive. El patrón buscado era en
minúscula (`intellectus`, `dictum`); el código usa CamelCase
(`Intellectus`, `Dictum`) en docstrings y nombres de clase. Cero
coincidencias en líneas del diff.

Corrección metodológica: usar `-i` en el patrón, o buscar la forma
exacta (CamelCase) que aparece en el código.

### Grupo B · string ausente del contenido · reportes_motor

Verificación:

    reportes_motor.py
      grep "reportes_motor" → 0 matches
      docstring: "SCFV Motor 9.0.0 — Reportes desde EventStore"
      "Reportes desde EventStore" sí aparece, "reportes_motor" no.

Mecanismo: `git log -S "símbolo"` busca el string en líneas del diff,
no en nombres de archivo. El nombre del archivo no cuenta como
ocurrencia. `reportes_motor` es el nombre del archivo, no un string
del contenido.

Corrección metodológica: para verificar historia de un archivo, usar
`git log --follow -- <path>`, no `git log -S` sobre el nombre.

### Verificación cruzada de los tres

`git log --follow` sobre cada archivo confirma: los tres existen en c0.
`git blame` sobre líneas clave confirma autoría `^e0923e4`. Ninguno
tiene commits posteriores que los hayan tocado (excepto autoflake
cosmético en intellectus y dictum, sólo imports de typing).

---

## 4 · Verificación por archivo · git log --follow

    motor.py           · c0, autoflake
    reportes_motor.py  · c0
    reticulo.py        · c0
    examinador.py      · c0
    intellectus.py     · c0, autoflake
    dictum.py          · c0, autoflake

Autoflake pasa por 3 de los 6 archivos huérfanos. Sólo elimina imports de
`typing`. Cero lógica tocada.

---

## 5 · Verificación por línea · git blame

`motor.py:61 validar_partida_doble` · `reportes_motor.py:80 generar_csv_diario`
· `intellectus.py:1` — todos `^e0923e4`.

Autoría: cada línea huérfana nace en c0.

---

## 6 · Diff semántico c0..HEAD

Imports eliminados por autoflake: 13 líneas de `import os`, `import sqlite3`,
`from typing import ...`, etc. Cero huérfanos pierde su último import.

Llamadas eliminadas: todas en `orquestador.py` y `event_store.py`,
resultado de FASE 1 (transaccionalidad) y FASE 2.a.1 (dedup). Ninguna
eliminación afecta a un huérfano — los huérfanos no tenían llamadas que
eliminar; nacieron sin consumidor.

---

## 7 · Hallazgo reformulado tras falsación

**Formulación original (falsada):**

    "El repo DSR no tiene historia de código post-c0."

**Formulación sostenida (operacional):**

    Los commits post-c0 que modificaron .py no explican el origen ni la
    pérdida de consumidores de los símbolos huérfanos identificados en
    vulture_60.

**Formulación complementaria (B.1.b):**

    Los 27 símbolos huérfanos verificados por git log -S -- '*.py' tienen
    su primer y único commit en e0923e4.

Ambas quedan falsables por separado. La primera es sobre los commits
post-c0. La segunda es sobre los símbolos huérfanos.

---

## 8 · Consecuencia para FASE 3

La decisión sobre huérfanos no puede apoyarse en historia del repo DSR:
los huérfanos nacen huérfanos en c0, y ningún commit posterior los
desconectó. Debe apoyarse en:

(a) historia de S0 (~/scfv_v6/), o
(b) canon doctrinal (npl, c3, H8P, H9), o
(c) decisión explícita nueva.

Pendiente para B.2: abrir los ~15 documentos de S0 que pueden contener
la intención original.

---

## 9 · Correcciones metodológicas registradas

Dos artefactos del instrumental detectados y documentados para futuros
bloques:

1. `git log -S "símbolo"` con patrón en minúscula sobre código que usa
   CamelCase produce falsos negativos silenciosos. Usar `-i` o la forma
   exacta.

2. `git log -S "nombre_de_archivo"` no rastrea el nombre del archivo,
   sólo su contenido. Para historia de archivos usar `--follow`.

---

*Bloque B.1 · sólo lectura · sin patch · sin modificación de código.*
*Falsado por IA-2 · dos correcciones de alcance aplicadas.*
