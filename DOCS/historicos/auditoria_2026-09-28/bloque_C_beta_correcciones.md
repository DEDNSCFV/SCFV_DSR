# Bloque C-β · Correcciones a hallazgos previos

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** C-β.0..6 (34 archivos · 5530 L).
**Naturaleza:** registro de correcciones formales. No modifica archivos previos. No modifica el traspaso original.

---

## §0 · Objeto

La auditoría técnica (C-β) descubre hechos que precisan, reformulan o contradicen hallazgos de bloques previos (Ventana 10 · Bloque A/B · Ventana 11 · B-bis). Algunos hallazgos deben retirarse; otros requieren cambio de ubicación; otros deben reformularse.

Este documento registra tres tipos de corrección:

- **RETIRADA** · hallazgo previo que resultó ser artefacto o error de lectura.
- **REUBICACIÓN** · hallazgo previo correcto pero mal ubicado.
- **REFORMULACIÓN** · hallazgo previo correcto pero mal formulada la deuda asociada.

Las correcciones no modifican los archivos originales. Se registran para uso futuro.

---

## §1 · Correcciones al Bloque A (Ventana 10)

### C-B-1 · `fpdf` no declarada

**Hallazgo Bloque A:** `fpdf` importada pero no declarada en `pyproject.toml`.

**Verificación en C-β:**

`reportes_motor.generar_pdf_diario`:
```python
try:
    from fpdf import FPDF
except ImportError:
    raise RuntimeError("fpdf no instalado. Ejecutar: pip install fpdf")
```

Confirmado. La importación es defensiva y explícita. No hay crash silencioso.

Deuda del port confirmada. Sin cambio.

C-B-2 · var/scfv.db sin identificar

Hallazgo Bloque A: var/scfv.db (425 KB) detectada sin identificar.

Verificación en C-β:

cli.py:cmd_init:

```python
DB_DEFAULT = VAR / 'scfv.db'
def cmd_init(args):
    VAR.mkdir(parents=True, exist_ok=True)
    from scfv_dsr.contable.event_store import EventStore
    store = EventStore(str(DB_DEFAULT))
```

Confirmado. Es la DB inicializada por scfv_dsr.cli init.

Hallazgo retirado. No es deuda. Es la DB local declarada en README.

C-B-3 · perfiles/ vacío

Hallazgo Bloque A: perfiles/ vacío en DSR.

Verificación en C-β:

No aparece en el corpus técnico. El directorio no tiene consumidor en código.

Confirmado como patrón. Coherente con GENEALOGIA §9.1 (etapa previa declarada). Sin cambio.

C-B-4 · imports sin prefijo scfv_dsr.

Hallazgo Bloque A: algunos imports sin prefijo scfv_dsr..

Verificación en C-β:

· integrador.py:25: import evaluador (top-level)
· integrador.py:29: from scfv_dsr.profesional.orquestador import ... (correcto)

Confirmado. El integrador usa sys.path.insert para rescatar evaluador. Confirmación material de H-C-78.

Deuda del port confirmada. Sin cambio.

C-B-5 · corpus fundacional no leído

Hallazgo Bloque A: archivos DOCUMENTO_FUNDACIONAL.md, GENEALOGIA.md, HASHES.txt no leídos.

Verificación en C-β: leídos en B-bis.3.

Retirado. Cerrado en B-bis.

---

§2 · Correcciones al Bloque B (Ventana 10)

C-B-6 · D-B-1..15 · métricas H1 duplicadas

Hallazgo Bloque B: métricas H1 duplicadas · doble cómputo · sin consumidor · magnitud hardcoded · s hardcoded.

Verificación en C-β:

generador_propuesta.py:

```python
s = 0.0
t = calcular_t()                # siempre 0.0
v = calcular_v(inflacion_anual) if inflacion_anual is not None else 0.0
```

soporte_C = 0.30*r + 0.25*s + 0.20*o + 0.15*t + 0.10*v

Con defaults: soporte_C = 0.30*r + 0.20*o máximo 0.50.

Confirmado. Las métricas están materializadas en firma pero operativas sólo parcialmente (2 de 5).

Deuda del port confirmada. Se añade D-C-11 para la cuantificación exacta.

C-B-7 · D-B-16..19 · ontología constitucional

Hallazgo Bloque B: tétrada ontología constitucional sin consumidor.

Verificación en C-β:

models.py:Tetrada con 7 campos (H, C, E, M, V, X, K). Dataclass existe. Sin consumidor visible en DSR.

No aparece en motor.py, nucleo_consecuencias.py, orquestador.py, evaluador.py, perceptum.py.

Confirmado. Coherente con HC-4.

Reformulación: D-B-16..19 se refieren a Tetrada dataclass (7 campos). El "3 tétradas coexisten" de B-bis (D-BB-68) se refiere a las 3 cadenas cuaternarias textuales (ADR-001, GENEALOGIA §4.2, Fundacional §17, §21). Son objetos distintos. No contradicción.

C-B-8 · D-B-20..26 · complejidad

Hallazgo Bloque B: motor.generar_asiento F(42) · evaluar_operacion D(29).

Verificación en C-β:

· motor.generar_asiento (líneas 155-221): 7 pasos con múltiples if anidados + 2 loops con for idx, p in enumerate(...). Estructura densa. F(42) plausible.
· evaluador.evaluar_operacion (líneas 115-170): 15+ ramas if op_id == "..." secuenciales, más un dispatch a Baldor para 3 ops. D(29) plausible.

Confirmado. Los valores de radon son coherentes con la estructura.

Deuda del port confirmada. Sin cambio.

C-B-9 · D-BALDOR-VC · verificar_cuadre huérfana

Hallazgo Bloque B: verificar_cuadre huérfana declarada sin patch.

Verificación en C-β:

baldor.verificar_cuadre(total_debe, total_haber) existe.

motor.validar_partida_doble(partidas) reimplementa la misma lógica inline:

```python
if abs(total_debe - total_haber) > 0.001:
    raise ValueError(f"I1_VIOLACION: debe={total_debe}, haber={total_haber}")
```

Reformulación: no es huérfana por ausencia. Es huérfana con duplicado funcional en motor.validar_partida_doble.

Deuda reubicada: D-C-32.

C-B-10 · D-BALDOR-IVA-1/2

Hallazgo Bloque B: deuda IVA en Baldor.

Verificación en C-β:

baldor.calcular_base_e_iva(monto_con_iva, tasa):

```python
base = monto_con_iva / (1.0 + tasa)
iva  = monto_con_iva - base
return base, iva
```

Fórmula correcta. El defecto IVA documentado en _EA_HALLAZGOS (iva = monto * IVA_TASA / 100000000) vive en scfv_architect.py (M1), no en baldor.py (M2).

Reformulación: el defecto IVA está en M1. No fue portado a M2. Deuda de M1, no de M2.

Deuda reubicada.

C-B-11 · suma_montos (diferida)

Hallazgo Bloque B: suma_montos diferida.

Verificación en C-β:

baldor.sumar_montos(montos):

```python
def sumar_montos(montos: List[float]) -> float:
    """Suma algebraica de montos. Raw L874-997 (reducción de términos)."""
    return sum(montos)
```

Función existe. Docstring infla atribución (cita locus de Baldor). Implementación es builtins.sum.

Reformulación: la función existe con implementación correcta pero documentación inflada. Deuda de documentación, no de funcionalidad.

Deuda reubicada: D-C-1.

C-B-12 · MotorContable(None)

Hallazgo Bloque B / H7H / H8P_IMPORTADOR / H9_EVALUACION: MotorContable(None) en exportador.py:66.

Verificación en C-β:

orquestador.py:118:

```python
motor = MotorContable(None, pcu, moneda_funcional="VES")
```

El MotorContable(None) está en orquestador.py, no en exportador.py.

Reformulación: la ubicación declarada por el corpus doctrinal es incorrecta. El defecto real está en orquestador.py.

Corrección: D-BB-14 y D-C-30 deben reformularse para ubicar el defecto en orquestador.py.

C-B-13 · fpdf en pyproject.toml

Hallazgo Bloque A: fpdf no declarada en pyproject.toml.

Verificación en C-β:

pyproject.toml declara lark>=1.0 (per HASHES.txt). No declara fpdf.

Confirmado. La dependencia existe pero no se declara. Import defensivo (try/except) permite que el módulo se importe sin fallar; sólo falla en runtime al llamar generar_pdf_diario.

Deuda del port confirmada. Sin cambio.

---

§3 · Correcciones a hallazgos de B-bis

C-B-14 · D-BB-19 · componentes canónicos no caracterizados

Hallazgo B-bis: ≥5 componentes canónicos no caracterizados (Adquisidor, Perceptum, PropuestaH1, ConsecuenciaAutorizada, NucleoConsecuencias).

Verificación en C-β:

Componente Ubicación Estado
AdquisidorEvidencia No está en corpus técnico DSR Sigue no caracterizado
Perceptum epistemologico/perceptum.py (284 L) ✅ caracterizado
PropuestaH1 epistemologico/models.py ✅ caracterizado
ConsecuenciaAutorizada contable/modelos.py ✅ caracterizado
NucleoConsecuencias contable/nucleo_consecuencias.py ✅ caracterizado
DecisionProvider contable/decision_provider.py ✅ caracterizado
VerificadorAutorizacion contable/verificador_autorizacion.py ✅ caracterizado
PuenteAutorizacion contable/puente_autorizacion.py ✅ caracterizado
PuenteConsecuencias contable/puente_consecuencias.py ✅ caracterizado
MotorContable contable/motor.py ✅ caracterizado

Parcialmente cerrada. 9 de 10 componentes caracterizados. Sólo AdquisidorEvidencia sigue fuera (probablemente en M1).

C-B-15 · D-BB-58 · Intellectus y Dictum

Hallazgo B-bis: Intellectus y Dictum no caracterizados.

Verificación en C-β:

· Intellectus · epistemologico/intellectus.py (105 L) · intérprete hermenéutico.
· Dictum · epistemologico/dictum.py (71 L) · orientador.

Cerrada. Ambos caracterizados.

C-B-16 · H-MIG-02/03 · prefijos vs event-sourced

Hallazgo B-bis: NPL especifica event_store embebido vs migración 002 separada.

Verificación en C-β:

event_store.py crea una sola tabla:

```sql
CREATE TABLE IF NOT EXISTS event_store (
    id INTEGER PRIMARY KEY,
    tipo_evento TEXT NOT NULL,
    payload TEXT NOT NULL,
    correlation_id TEXT NOT NULL,
    idempotency_key TEXT UNIQUE NOT NULL,
    hash_previo TEXT NOT NULL,
    hash_actual TEXT NOT NULL,
    timestamp INTEGER NOT NULL,
    version_contexto TEXT
)
```

Sin prefijos negocio_/auditoria_/epistemic_. Modelo NPL materializado, migración 002 superada.

Resuelto. DSR implementa el NPL. La contradicción era entre M1 (migraciones) y corpus doctrinal (NPL). M2 resuelve siguiendo el NPL.

C-B-17 · D.5 · obtener_por_correlation sin parsear

Hallazgo H7H / H8P_IMPORTADOR §12 / H9_EVALUACION E3: obtener_por_correlation devuelve payload sin parsear.

Verificación en C-β:

event_store.obtener_por_correlation (línea 440):

```python
return {
    "id": row[0],
    "tipo_evento": row[1],
    "payload": json.loads(row[2]),   # ← SÍ parsea
    ...
}
```

No reproducible en HEAD. La inconsistencia declarada no existe.

Reformulación: D.5 debe reformularse como "deuda declarada por H9 §3 E3, no reproducible en HEAD d0433f0".

Deuda reubicada: D-C-23.

C-B-18 · Autonomía declarada de DSR

Hallazgo implícito en README DSR: "El paquete no depende del corpus S0 (scfv_v6). Es portable."

Verificación en C-β:

test_compatibilidad_s0.py:

```python
SCFV_V6 = Path.home() / "scfv_v6"
def test_historico_parsea():
    p = SCFVParser()
    for nombre in ARCHIVOS:
        path = SCFV_V6 / "DOMINIOS" / nombre / "reglas" / f"{nombre}.scfv"
        r = p.parse_file(str(path))
```

Contradice la declaración de autonomía.

Deuda nueva: D-C-82. La autonomía declarada del paquete es correcta en runtime pero falsa en suite de tests.

---

§4 · Retiradas

RET-C-1 · H-C-9 / D-C-9

Hallazgo C-β.2: evidencia.py con ) huérfano · archivo no compila.

Verificación C-β.2-bis: python3 -m py_compile retorna OK.

Retirada. Artefacto de transcripción del pegado. No es defecto.

RET-C-2 · H-C-30 / D-C-22

Hallazgo C-β.3: PersistenciaViolacion declarada en docstring pero no definida.

Verificación C-β.6.1: serializador_canonico.py define la clase. event_store.py la propaga transitivamente vía serializar.

Retirada. Lectura incompleta de mi parte.

---

§5 · Correcciones al traspaso Ventana 10

T-1 · Ubicación de MotorContable(None)

Traspaso declaró (implícito vía H7H): MotorContable(None) en exportador.py:66.

Realidad: MotorContable(None) está en orquestador.py:118.

Corrección registrada. El corpus doctrinal heredó una ubicación errónea de H7H.

T-2 · Ubicación de corpus fundacional

Traspaso declaró: 7 archivos en ~/scfv_v6/ (implícito).

Realidad: 6 en ~/scfv-dsr/, 1 en ~/scfv_v6/. Ya registrado en B-bis C1.

Sin cambio.

T-3 · Régimen IA-3

Traspaso declaró: "IA-2 falsa · IA-3 aplica."

Realidad: régimen tripartito IA-1 + IA-2 + Operador.

Sin cambio respecto a B-bis C2.

---

§6 · Balance de correcciones

```
RETIRADAS                 2 (H-C-9/D-C-9 · H-C-30/D-C-22)
REUBICADAS                4 (D-BALDOR-VC · D-BALDOR-IVA-1/2 · suma_montos · D.5)
REFORMULADAS              3 (D-B-16..19 · MotorContable(None) · D-BB-19)
CONFIRMADAS               ~10 (fpdf · var/scfv.db · perfiles · prefijos sin prefijo · D-B-1..15 · D-B-20..26)
CERRADAS                  3 (corpus fundacional · D-BB-58 · H-MIG-02/03)
CORRECCIONES AL TRASPASO  3 (T-1 · T-2 · T-3 · T-2 y T-3 ya estaban en B-bis)
```

---

§7 · Correcciones que quedan vigentes para futuras ventanas

Las siguientes correcciones deben aplicarse al interpretar el corpus doctrinal:

1. MotorContable(None) está en orquestador.py:118, no en exportador.py:66.
2. D-BALDOR-IVA-1/2 aplica a M1 (scfv_architect.py), no a M2 (baldor.py).
3. D-BALDOR-VC es deuda con duplicado funcional, no ausencia de consumidor.
4. D-B-16..19 se refieren a Tetrada dataclass (7 campos), no a las 3 cadenas cuaternarias textuales.
5. D.5 no es reproducible en HEAD · debe reformularse.
6. test_compatibilidad_s0.py contradice la autonomía declarada por README.
7. PersistenciaViolacion existe en serializador_canonico.py.

---

Fin del registro de correcciones.
Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.
