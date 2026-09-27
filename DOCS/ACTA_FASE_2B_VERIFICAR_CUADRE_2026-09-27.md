# ACTA · FASE 2.b · VERIFICAR_CUADRE

**Programa:** SCFV_DSR
**Fase:** 2 · Cableado Baldor
**Subfase:** 2.b · verificar_cuadre
**Fecha:** 2026-09-27
**Rol constructor:** IA-1
**Rol falsador:** IA-2
**Operador:** DEDN
**Estatuto:** ACTA INTERNA · NO ES ACTO DEL PROGRAMA
**Ubicación:** ~/scfv-dsr/DOCS/ACTA_FASE_2B_VERIFICAR_CUADRE_2026-09-27.md
**Estado:** CERRADA · SIN PATCH

---

## §1 · OBJETO

Determinar el estatuto de verificar_cuadre dentro de
scfv_dsr/kernel/baldor.py y decidir si corresponde cablearlo en
evaluar_operacion() durante la FASE 2.b.

---

## §2 · EVIDENCIA MATERIAL

### 2.1 · Fuente primaria · scfv_dsr/kernel/baldor.py:1-20

Lectura directa en esta ventana. Fragmento literal:

    "Baldor contable — operador algebraico elemental.
     Fuente · ~/.baldor_algebra_raw.txt (Álgebra de A. Baldor, 287 pp.)
     SHA256 raw · 63fe32a1ece2e183c43a5d040003c1efc6f6745e0afa976c7aed052c77f5fbaf

     Cada función implementa una ley o regla del raw con locus declarado.
     No inventa operaciones. No confunde aritmética con álgebra.

     Autoridad:
         - NO decide DEBE/HABER (eso es XNOR).
         - NO decide profesionalmente (eso es H2).
         - NO escribe en el motor.

     Frontera declarada (D-BALDOR-2):
         Cubre las 287 pp. del Álgebra de Baldor.
         NO cubre: redondeo administrativo, conversión con spread cambiario,
         cálculo de mora legal, operaciones específicas de industria."

Frontera D-BALDOR-2 verificada en primario, sin mediación de
auditorías secundarias.

### 2.2 · Fuente arquitectónica · ACTA_ENMIENDA_FRACTALIDAD_ACOTADA_MD_2026-09-24.md

§2-ter propone la articulación:

    Dogma       ↔ XNOR
    Disciplina  ↔ Baldor
    Economía    ↔ Motor epistémico

y especifica: "Disciplina · Baldor · calcula el monto aritmético."

La misma acta declara esta articulación como propuesta del Giro 05
y sin canon directo en el corpus.

### 2.3 · Estado histórico

PROMPT_AVANZADO_GIRO_05_AI1_AI2.md registraba
"Baldor · implementación pendiente (D-NUC-1)".
Estado superado parcialmente por FASE 2.a.

### 2.4 · FASE 2.a · commit abd746e

Despacho materializado para:

    interes_compuesto → capital_final
    valor_presente    → capital_inicial
    tasa_efectiva     → tasa_ic

---

## §3 · OBJETO BAJO FALSACIÓN

    verificar_cuadre(total_debe, total_haber) -> bool
        return abs(total_debe - total_haber) < 0.001

Pertenece técnicamente al operador aritmético Baldor.
Produce booleano. No produce monto. No decide DEBE/HABER.
No escribe en Motor.

---

## §4 · FALSACIÓN DEL CABLEADO

### 4.1 · Ausencia de consumidor ejecutable

Evidencia reproducible — grep global en ~/scfv-dsr:

    $ grep -rn "verificar_cuadre" --include="*.py" --include="*.scfv" --include="*.json" .
    ./scfv_dsr/kernel/operaciones.json:179:    "verificar_cuadre": {
    ./scfv_dsr/kernel/operaciones.json:184:      "funcion_baldor": "verificar_cuadre",
    ./scfv_dsr/kernel/baldor.py:169:def verificar_cuadre(total_debe: float, total_haber: float) -> bool:

El grep produce tres coincidencias textuales: dos declaraciones en
operaciones.json (entrada del diccionario en línea 179 + campo
funcion_baldor en línea 184) y una definición Python en baldor.py:169.

Ninguna constituye invocación ejecutable. Cero consumidores en
.scfv, evaluador.py, motor.py, orquestador.py, dsl/ ni tests.

### 4.2 · Solapamiento con Motor

motor.py:56-64 define validar_partida_doble(), que calcula ΣDEBE,
ΣHABER y rechaza abs(debe-haber) > 0.001. Mismo umbral, misma
relación. No invocado desde generar_asiento (hallazgo colateral,
fuera de 2.b).

### 4.3 · Contrato no declarado

Cablear verificar_cuadre como operación ordinaria de
evaluar_operacion() exigiría:

    Baldor → bool → evaluador → consecuencia

Contrato no declarado. evaluar_operacion retorna valor numérico;
_consecuencia_a_candidata hace float(c["monto"]); motor.py:141 exige
int|float.

---

## §5 · DECISIÓN

verificar_cuadre NO SE CABLEA durante FASE 2.b.

No se declara inválida la función. Su estatuto:

    PRIMITIVA BALDOR VÁLIDA
    SIN CONSUMIDOR CANONIZADO EN SCFV_DSR
    DESTINO ARQUITECTÓNICO PENDIENTE

No se modifica baldor.py, operaciones.json, evaluador.py,
integrador.py ni motor.py.

---

## §6 · DEUDA ARQUITECTÓNICA · D-BALDOR-VC

Determinar en fase arquitectónica correspondiente cuál es el lugar
de una primitiva Baldor cuyo resultado es validación booleana y no
monto. Alternativas sin adoptar:

1. conservar como primitiva disponible;
2. reubicar como validador;
3. integrar mediante contrato arquitectónico explícito;
4. eliminar su declaración si se demuestra ausencia de función.

---

## §7 · RELACIÓN CON FASE 2.c · desglose_iva

FASE 2.c no es análoga a 2.b. calcular_base_e_iva(monto_con_iva,
tasa) produce valores aritméticos, pero su retorno tuple (base, iva)
no satisface el contrato numérico actual de evaluar_operacion.
El bloqueo de 2.c es de forma del contrato de retorno, no de
pertenencia a Baldor.

La frontera de 2.b (pertenencia a Baldor sin consumidor) no aplica
a 2.c (pertenencia a Baldor con consumidor bloqueado por forma).

---

## §8 · ESTADO DE FASE

    FASE 2.a · CERRADA                          (commit abd746e)
    FASE 2.b · MATERIALIZADA SIN PATCH          (este acta)
    FASE 2.c · NO RESUELTA · bloqueo de forma
    FASE 3   · DESTINO DE D-BALDOR-VC

---

## §9 · INVARIANTE METODOLÓGICO

    función existente            ≠ función consumida
    coincidencia textual         ≠ invocación ejecutable
    pertenencia a Baldor         ≠ obligación de cableado
    propuesta arquitectónica     ≠ canon externo directo
    canon interno del Giro 05    ≠ canon externo verificado

---

## §10 · CIERRE

FASE 2.b queda cerrada por falsación del cableado propuesto.
verificar_cuadre permanece intacta. Sin patch de código. Sin nuevo
consumidor. Sin modificación del contrato de evaluar_operacion.

**ESTADO:** CERRADA · SIN PATCH
