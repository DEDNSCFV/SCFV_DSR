# ACTA · FASE 2.c · DESGLOSE_IVA

**Programa:** SCFV_DSR
**Fase:** 2 · Cableado Baldor
**Subfase:** 2.c · desglose_iva
**Fecha:** 2026-09-27
**Rol constructor:** IA-1
**Rol falsador:** IA-2
**Operador:** DEDN
**Estatuto:** ACTA INTERNA · NO ES ACTO DEL PROGRAMA
**Ubicación:** ~/scfv-dsr/DOCS/ACTA_FASE_2C_DESGLOSE_IVA_2026-09-27.md
**Estado:** CERRADA · SIN PATCH

---

## §1 · OBJETO

Determinar si corresponde cablear desglose_iva en evaluar_operacion()
durante la FASE 2.c, dado que su primitiva Baldor calcular_base_e_iva
retorna tuple (base, iva) y el contrato actual del pipeline está
cableado para "1 acción DSL = 1 partida = 1 monto float".

---

## §2 · EVIDENCIA MATERIAL

### 2.1 · Declaración en operaciones.json (líneas 190-197)

    "desglose_iva": {
      "descripcion": "Desglose base + IVA",
      "normas": ["LIVA_Art4"],
      "funcion_baldor": "calcular_base_e_iva",
      "parametros": ["monto_con_iva", "tasa"]
    }

### 2.2 · Primitiva Baldor (baldor.py:174-180)

    def calcular_base_e_iva(monto_con_iva: float, tasa: float) -> tuple:
        """Desglosa monto con IVA incluido en (base, iva).
        Raw L1693 (distributiva) + L1699 (inverso)."""
        base = monto_con_iva / (1.0 + tasa)
        iva = monto_con_iva - base
        return base, iva

Dentro de la frontera D-BALDOR-2 (cálculo aritmético).

### 2.3 · DSL · gramática (grammar.lark)

    action: assignment | generate
    generate: "GENERAR" "CONSECUENCIA" "(" param_list ")"
    param_list: param ("," param)*
    param: NAME "=" arith

Una acción GENERAR CONSECUENCIA produce una única consecuencia.
Confirmado en 42 invocaciones en fractales/*.scfv: cada partida es
una línea GENERAR separada.

### 2.4 · Modelo downstream (modelos.py)

    @dataclass
    class ConsecuenciaAutorizada:
        ...
        partidas: List[Dict]

    @dataclass
    class PartidaAutorizada:
        cuenta_codigo: str
        cuenta_version: str
        monto: float
        ubicacion: str
        movimiento: str
        moneda: Optional[str] = "VES"
        es_fiscal: bool = False
        norma_id: Optional[str] = None

PartidaAutorizada.monto: float. No hay campos base ni iva.

### 2.5 · Reducción en integrador.py

    def _consecuencia_a_candidata(consecuencias: List[Dict]) -> List[Dict]:
        return [
            {
                "cuenta": c["cuenta"],
                "monto": float(c["monto"]),
                "naturaleza": c["naturaleza"],
                "movimiento": c["movimiento"],
            }
            for c in consecuencias
        ]

float(c["monto"]) revienta con un tuple.

### 2.6 · Contrato motor.py

    if not isinstance(p["monto"], (int, float)):
        raise ValueError(f"MOTOR_VIOLACION: partida {idx} con monto no numérico")
    if p["monto"] < 0:
        raise ValueError(...)

Un tuple no pasa el contrato del motor.

### 2.7 · Convergencia con ciclo 6.0

ACTO_6_0_CONV_CONVERGENCIA.md §7.2.8:

    desglose_iva · operación en operaciones.json:190 · sin invocación

Y §7.4:

    desglose_iva = operación sin invocación (1)

La clasificación "operación sin invocación" fue declarada por el
Programa antes de esta ventana. No es hallazgo nuevo de esta sesión.

### 2.8 · Ancla normativa no cargable

GIRO_04/07_materializacion_scfv_dsr.md §4:

    Con `version_norma=True`: `LIVA_ART_62`, `LIVA_ART_62_COMPLETA`.
    Sin `version_norma`, descartadas por el loader actual: `NIC_29`,
    `BA_VEN_NIF_01`, `LIVA_Art4`, `LIVA_Art4.v81.bak`.
    Estado inicial: 2 normas utilizables de 6 JSON presentes.

desglose_iva cita LIVA_Art4. LIVA_Art4 no pasa el loader actual.

### 2.9 · Evento real sin desglose

AUDITORIA_B98_EXTRACTOR_2026-09-25.log registra un evento
ASIENTO_REGISTRADO real (id 372bed8b-...):

    partidas: [
      {"cuenta": "110101", "monto": 1000.0, ...},
      {"cuenta": "410101", "monto": 1000.0, ...}
    ],
    total_debe: 1000.0, total_haber: 1000.0,
    evidencia: {"factura": "FAC-001", "monto": 1000.0, "tipo": "venta", ...},
    normas_aplicadas: ["LIVA_Art4", "NIC_29"]

Asiento con LIVA_Art4 en normas_aplicadas, sin desglose base/cuota.
No contiene campos base_iva, iva, tasa, monto_con_iva, ni invocación
de desglose_iva.

### 2.10 · Grep de consumidores

    $ grep -rn "calcular_base_e_iva\|desglose_iva" --include="*.py" --include="*.json" --include="*.scfv" .
    ./scfv_dsr/kernel/operaciones.json:190:    "desglose_iva": {
    ./scfv_dsr/kernel/operaciones.json:195:      "funcion_baldor": "calcular_base_e_iva",
    ./scfv_dsr/kernel/baldor.py:174:def calcular_base_e_iva(monto_con_iva: float, tasa: float) -> tuple:

Tres coincidencias textuales: dos declaraciones JSON + una definición
Python. Ninguna constituye invocación ejecutable. Cero consumidores
en .scfv, evaluador.py, motor.py, orquestador.py, dsl/ ni tests.

---

## §3 · OBJETO BAJO FALSACIÓN

Extender el contrato de evaluar_operacion() para aceptar retornos
múltiples (tuple), desempaquetar y producir monto, con el fin de
cablear desglose_iva.

---

## §4 · FALSACIÓN DEL CABLEADO

### 4.1 · Sin consumidor ejecutable

Ver §2.10. Cero invocaciones.

### 4.2 · Sin consumidor DSL

42 reglas GENERAR CONSECUENCIA en fractales/*.scfv. Ninguna invoca
operacion="desglose_iva" ni variante. El DSL no puede emitir dos
partidas desde una acción.

### 4.3 · Sin modelo de dos salidas

PartidaAutorizada.monto: float es un único campo. No hay base ni iva.
Elegir cuál del tuple va a monto sería decisión inventada sin canon.

### 4.4 · Sin correspondencia causal LIVA_Art4 → desglose_iva

El evento B98 (§2.9) demuestra que LIVA_Art4 puede estar presente en
una consecuencia sin que desglose_iva la haya producido. La presencia
retrospectiva de una norma no implica la operación.

### 4.5 · Solapamiento con ciclo 6.0

El Programa ya clasificó desglose_iva como "operación sin invocación"
(§2.7). Este acta confirma la clasificación con evidencia
independiente, no la descubre.

---

## §5 · DECISIÓN

desglose_iva NO SE CABLEA durante la FASE 2.c.

Su estatuto:

    PRIMITIVA DECLARADA · SIN CONSUMIDOR CANONIZADO · SIN CABLEADO

No se modifica baldor.py, operaciones.json, evaluador.py,
integrador.py ni motor.py.

---

## §6 · DEUDAS ARQUITECTÓNICAS

- D-BALDOR-IVA-1 · ¿Debe existir un consumidor de desglose fiscal
  dentro del DSR?
- D-BALDOR-IVA-2 · Si debe existir, ¿qué contrato representa
  simultáneamente base e IVA?
- D-LIVA-LOADER · LIVA_Art4 no pasa el loader actual. O se arregla
  el loader, o se cambia la norma citada, o se retira la declaración.
- D-IVA-PIPELINE · Evento B98 registra venta con LIVA_Art4 sin
  desglose base/cuota. Hallazgo del pipeline real, independiente
  de desglose_iva.

Ninguna de las cuatro se resuelve en esta acta.

---

## §7 · RELACIÓN CON FASE 2.b · CONTRASTE

    2.b · verificar_cuadre  → bloqueo por ESTATUTO
                               (retorno bool queda fuera del canon
                                de cálculo de monto; motor ya tiene
                                I1 con validar_partida_doble)

    2.c · desglose_iva      → bloqueo por FORMA
                               (retorno tuple cae dentro del canon
                                de cálculo aritmético, pero el DSL
                                y el modelo downstream están
                                cableados para "1 acción = 1 partida
                                = 1 monto float")

2.c no es análoga a 2.b. Es un bloqueo de forma, no de estatuto.
Si el DSL pudiera emitir múltiples partidas por acción, desglose_iva
sería cableable sin tocar Baldor. Hoy no puede.

---

## §8 · ESTADO DE FASE

    FASE 2.a · CERRADA                          (commit abd746e)
    FASE 2.b · MATERIALIZADA SIN PATCH          (commit 78eda31)
    FASE 2.c · MATERIALIZADA SIN PATCH          (este acta)
    FASE 3   · DESTINO DE D-BALDOR-VC / D-BALDOR-IVA-1/2

---

## §9 · INVARIANTE METODOLÓGICO

    presencia declarativa         ≠ obligación de cableado
    coincidencia textual          ≠ invocación ejecutable
    norma citada                  ≠ operación ejecutada
    pertenencia a Baldor          ≠ obligación de cableado
    capacidad del lenguaje        ≠ demanda arquitectónica real

---

## §10 · CIERRE

FASE 2.c queda cerrada por falsación del cableado propuesto.
calcular_base_e_iva permanece intacta. Sin patch de código. Sin nuevo
consumidor. Sin modificación del contrato de evaluar_operacion.

**ESTADO:** CERRADA · SIN PATCH
