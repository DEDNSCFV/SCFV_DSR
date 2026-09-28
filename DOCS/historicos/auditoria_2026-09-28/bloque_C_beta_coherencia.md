# Bloque C-β · Coherencia con corpus doctrinal

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** C-β.0..6 (34 archivos · 5530 L).
**Naturaleza:** matriz de correspondencia doctrina ↔ materialización. No juzga. Contrasta.

---

## §0 · Método

Cada correspondencia se contrasta entre:
- una declaración del corpus doctrinal (ADR · NPL · H6/H7/H8P/H9 · Fundacional · GENEALOGIA),
- y su materialización (o ausencia) en el corpus técnico DSR.

Estados posibles:
- **CORRESPONDE** · declaración y código coinciden literalmente
- **PARCIAL** · declaración materializada sólo en parte
- **NO CORRESPONDE** · declaración sin materialización
- **EXCEDE** · código materializa algo no declarado en doctrina
- **CONTRADICE** · declaración y código se contradicen

---

## §1 · ADRs · ADR-000..005

### §1.1 · ADR-000 · Tecnología base

| Declaración | Materialización | Estado |
|---|---|---|
| Python 3.10+ (README DSR) · 3.11+ (ADR-000) | Requisitos en README · sin `python_requires` en pyproject | PARCIAL |
| SQLite | `sqlite3` en `event_store.py`, `cli.py`, `reportes_motor.py` | CORRESPONDE |
| Termux/Android | Termux confirmado | CORRESPONDE |
| Sin red · sin servidores | Sin dependencias de red en código | CORRESPONDE |
| `pypdf` · `pillow` | No declaradas ni usadas | NO CORRESPONDE |
| `fpdf` | Importada en `reportes_motor.generar_pdf_diario` (local, defensivo) | EXCEDE |

### §1.2 · ADR-001 · Separación de poderes

| Autoridad | Componente DSR | Estado |
|---|---|---|
| Epistemológica | `perceptum.py`, `intellectus.py`, `dictum.py`, `generador_propuesta.py` | CORRESPONDE |
| Profesional (Contador) | `h2.py`, `DecisionProfesional` | CORRESPONDE |
| Contable (Motor) | `motor.py`, `nucleo_consecuencias.py` | CORRESPONDE |
| Demostrativa | `event_store.py` (hash chain) · `maquina_estados_asiento.py` (historial) | CORRESPONDE |

Frontera declarada: Núcleo no decide, Motor no orienta, Contador no escribe, Auditoría no modifica. **Respetada en el port.**

### §1.3 · ADR-002 · Prefijos y multi-mandante

| Declaración | Materialización | Estado |
|---|---|---|
| 3 prefijos `negocio_` · `epistemic_` · `auditoria_` | **No materializado** · schema único `event_store` | NO CORRESPONDE |
| `/data/mandante_X/scfv_v6.db` | `~/SCFV_DSR/var/scfv.db` · sin multi-mandante | NO CORRESPONDE |
| Atomicidad multi-prefijo | Atomicidad de ciclo vía `store.transaccion()` (nivel evento, no prefijo) | PARCIAL |

**Interpretación:** DSR implementa el modelo del **NPL** (event-sourced único), no el de ADR-002 (relacional con prefijos). **Corresponde a H-MIG-02/03.** DSR no contradice ADR-002; DSR implementa una arquitectura posterior.

### §1.4 · ADR-003 · Especificación previa

| Declaración | Materialización | Estado |
|---|---|---|
| `README.md` por módulo | Sólo `dsl/README.md` detectado en HASHES.txt | PARCIAL |
| PRE/POST/INVARIANTE por función crítica | Docstrings informales · sin bloques PRE/POST estructurados | PARCIAL |
| "código como consecuencia de especificación" | El corpus doctrinal materializa primero contratos (H8P_*) y luego código | CORRESPONDE |

### §1.5 · ADR-004 · Axiomas epistemológicos

| Axioma | Materialización | Estado |
|---|---|---|
| **E-1** Similitud ≠ Evidencia | `EntidadExtraida` **sin** campo `fuente` · `confianza_por_campo` ausente | NO CORRESPONDE |
| **E-2** Integridad ≠ Veracidad | `event_store` hash chain · `Evidencia.calcular_hash` · no hay campo `veracidad` | CORRESPONDE |
| **E-3** Soporte ≠ Decisión | `h2.py` exige justificación · `modo_auto` bloqueado salvo `SCFV_MODO_PRUEBA=1` | CORRESPONDE |
| `C = f(r,s,o,t,v)` | Firma completa · sólo 2/5 dimensiones operativas | PARCIAL |
| XNOR triple | `xnor.py` con 3 caras equivalentes | CORRESPONDE |

### §1.6 · ADR-005 · Multi-mandante y cifrado

| Declaración | Materialización | Estado |
|---|---|---|
| SQLCipher AES-256 | `sqlite3.connect()` plano · sin cifrado | **NO CORRESPONDE** |
| Passphrase por mandante | Ausente | NO CORRESPONDE |
| Selección de mandante | Ausente | NO CORRESPONDE |
| Bloqueo de sesión | Ausente | NO CORRESPONDE |

**Interpretación:** ADR-005 es de M1 y no fue portado a M2. Confirmado con H-ADR5-01.

---

## §2 · NPL · Invariantes I1..I10

| Invariante | Materialización | Estado |
|---|---|---|
| **I1** ΣDEBE == ΣHABER | `motor.validar_partida_doble` · `motor.generar_asiento` §6 | CORRESPONDE |
| **I2** Cuenta existe | `motor._verificar_cuenta_con_marco` · `motor.generar_asiento` §4 | CORRESPONDE |
| **I3** Hecho CONFIRMADO | No hay verificación explícita en orquestador | NO CORRESPONDE |
| **I4** DECISION_H2_REGISTRADA | `h2.decidir` persiste `DECISION_H2` · `DecisionProvider.obtener_decision` | CORRESPONDE |
| **I5** EVIDENCIA_TRAZABLE | `ObservacionH1.evidencia_id` · `HechoEconomico.evidencia_ids` | CORRESPONDE |
| **I6** REGLA_IDENTIFICADA | `motor.validar_I6` · `motor.generar_asiento` §3-4 | CORRESPONDE |
| **I7** IDEMPOTENCIA | `event_store` UNIQUE `idempotency_key` · `event_store.guardar` | CORRESPONDE |
| **I8** HASH_PREVIO_VALIDO | `event_store.GENESIS_HASH` · `verificar_cadena` | CORRESPONDE |
| **I9** ESTADO_EPISTEMICO | `EstadoEpistemico` en `estados.py` · no verificado en motor | PARCIAL |
| **I10** CONSECUENCIA_REPRODUCIBLE | `event_store.obtener_por_correlation` (I10 declarada) | PARCIAL |

**Balance:** 6/10 correspondencias plenas · 2/10 parciales · 2/10 sin materializar.

---

## §3 · H6_CIERRE · Cadena canónica

### §3.1 · Cadena H1 → EventStore

Cadena declarada:
```

H1 → H2 → DP → VA → PA → NC → PC → MC → ASENTADO → EventStore

```

Materialización en `orquestador.ejecutar_ciclo_v82`:

| Eslabón | Módulo | Estado |
|---|---|---|
| H1 | `generador_propuesta.generar_propuesta_h1` | CORRESPONDE |
| H2 | `h2.H2Decision.decidir` | CORRESPONDE |
| DP | `decision_provider.DecisionProvider.obtener_decision` | CORRESPONDE |
| VA | `verificador_autorizacion.VerificadorAutorizacion.esta_autorizado` | CORRESPONDE |
| PA | `puente_autorizacion.PuenteAutorizacion.autorizar_admitido` | CORRESPONDE |
| NC | `nucleo_consecuencias.NucleoConsecuencias.construir_consecuencia_autorizada` | CORRESPONDE |
| PC | `puente_consecuencias.PuenteConsecuencias.construir_consecuencia_autorizada` | CORRESPONDE |
| MC | `motor.MotorContable.generar_asiento` | CORRESPONDE |
| ASENTADO | `maquina_estados_asiento.MaquinaEstadosAsiento.transicionar` | CORRESPONDE |
| EventStore | `event_store.EventStore.guardar` | CORRESPONDE |

**Cadena canónica completa.**

### §3.2 · H6.9-bis · XNOR fuente única

Declaración: *"`motor.py` y `nucleo_consecuencias.py` delegan en `xnor.py`. Cero tablas duplicadas."*

| Consumidor | Módulo xnor usado | Estado |
|---|---|---|
| `motor._calcular_ubicacion_xnor` | `xnor.ubicacion_booleana` | CORRESPONDE |
| `nucleo_consecuencias._calcular_ubicacion_xnor` | `xnor.ubicacion_booleana` | CORRESPONDE |
| `motor.generar_asiento` §5 | las 3 caras de xnor | CORRESPONDE |
| `examinador.nivel_linea` | módulo xnor completo | CORRESPONDE |
| `evaluador.evaluar_fractal` | `xnor.ubicacion_booleana` | CORRESPONDE |
| `integrador` | `from scfv_dsr.kernel import xnor` | CORRESPONDE |

**Sin tablas duplicadas.** Correspondencia literal.

### §3.3 · H6.10 · Fractalidad

| Declaración | Materialización en DSR | Estado |
|---|---|---|
| V(S) = {cuenta → Σ signo·monto} | No hay implementación directa | NO CORRESPONDE |
| V'(S) = {(cuenta, interno) → Σ signo·monto} | No hay implementación directa | NO CORRESPONDE |
| T_agregación · T_consolidación | No implementados en DSR | NO CORRESPONDE |
| E_refinado morfismo | No implementado en DSR | NO CORRESPONDE |

**Interpretación:** la fractalidad acotada vive en M1 y el corpus doctrinal. No fue portada a DSR. **Corresponde a declaración de autonomía.** No es defecto.

---

## §4 · H7B · Camino 3 · Retículo y examinador

| Declaración | Materialización | Estado |
|---|---|---|
| `reticulo.py` · (P(C), ⊆, ∪, ∩, ¬, △) | `reticulo.py` con métodos `union`, `interseccion`, `complemento`, `diferencia_simetrica` | CORRESPONDE |
| `examinador.py` · panel de consulta | `examinador.py` · no camino crítico | CORRESPONDE |
| `anillo.py` · aparcado por vacuidad | No existe en DSR | CORRESPONDE (aparcamiento) |
| Decisión B · sin default replicado | `reticulo.desde_pcu` usa `meta.get(clave, [])` | CORRESPONDE |

---

## §5 · H8P · Contratos

### §5.1 · H8P_RETICULO_CONTRATO

| Cláusula | Materialización | Estado |
|---|---|---|
| `RetículoCuentas.desde_pcu(pcu, clave="marcos")` | `reticulo.py:desde_pcu` | CORRESPONDE |
| Falsadores F1–F8 | `test_reticulo.py` (14 tests) | CORRESPONDE |
| Sin dependencias de xnor/motor | Sólo stdlib | CORRESPONDE |

### §5.2 · H8P_EXAMINADOR_CONTRATO

| Cláusula | Materialización | Estado |
|---|---|---|
| Rol panel no puerta | `examinador.py` docstring | CORRESPONDE |
| `examinar(Mapping)` → `Reporte` | `ExaminadorEvidencia.examinar` | CORRESPONDE |
| No-Mapping → TypeError | `if not isinstance(evidencia, Mapping): raise TypeError` | CORRESPONDE |
| 16 falsadores E1–E16 | `test_examinador.py` (16 tests · E12 skip) | CORRESPONDE |
| Independencia de motor/event_store | Sólo importa xnor + reticulo | CORRESPONDE |

### §5.3 · H8P_IMPORTADOR_CONTRATO

**Nota:** `importador_s0.py` no está en el corpus técnico DSR. El contrato describe un módulo de M1. **No aplica a M2.**

---

## §6 · H9 · Gate S0

| Criterio | Materialización | Estado |
|---|---|---|
| C1 Materialización | Capas línea/conjunto/integración en DSR | CORRESPONDE parcial (importador no en M2) |
| C2 Falsadores | Tests verdes en DSR (7 DSL + 8 juez) | PARCIAL |
| C3 No-regresión | Suite DSR no corre en 223 tests · M1 y M2 separados | NO CORRESPONDE |
| C4 Frontera importador | No aplica (importador en M1) | — |
| C5-C8 | Delimitación documental en M1 | — |

---

## §7 · GENEALOGIA · Materializaciones

| Declaración | Materialización en DSR | Estado |
|---|---|---|
| DSR = materialización 2 | Confirmado | CORRESPONDE |
| Autónomo respecto a M1 | README declara · **tests lo contradicen** | CONTRADICE |
| Régimen ProGit | Adoptado (commits anotados) | CORRESPONDE |
| GPG pendiente | Deuda declarada | CORRESPONDE |
| 10 fractales | `fractales/*.scfv` (10 archivos) | CORRESPONDE |

**Fricción principal:** la autonomía declarada por README es **desmentida por `test_compatibilidad_s0.py`** (D-C-82).

---

## §8 · DOCUMENTO_FUNDACIONAL · §31

| Nivel de confrontación §31 | Materialización en DSR | Estado |
|---|---|---|
| CONCEPTO | No evaluado explícitamente en tests ni en Gate | NO CORRESPONDE |
| CONTRATO | H8P_RETICULO · H8P_EXAMINADOR · contratos en M1 | CORRESPONDE parcial |
| ARQUITECTURA | Cadena canónica materializada | CORRESPONDE |
| IMPLEMENTACIÓN | 34 archivos · 5530 L | CORRESPONDE |
| PRUEBA | 7 DSL verdes en DSR | PARCIAL |
| EVIDENCIA | Hash chain verificable | CORRESPONDE |

**Conclusión:** el §31 del Fundacional no se cumple **completamente** en DSR. Falta el nivel CONCEPTO explícito.

---

## §9 · Síntesis de coherencia

```

CORRESPONDE          ~35 cláusulas
PARCIAL               ~8 cláusulas
NO CORRESPONDE        ~8 cláusulas
EXCEDE                ~1 cláusula
CONTRADICE            ~1 cláusula

```

**Correspondencias fuertes:**
- Cadena canónica H6 §1 (10/10 eslabones).
- XNOR triple ADR-004 (5/5 consumidores).
- Autoridades ADR-001 (4/4).
- Invariantes NPL I1, I2, I4, I5, I6, I7, I8 (7/10).
- Contratos H8P_RETICULO, H8P_EXAMINADOR.

**No correspondencias:**
- ADR-005 (SQLCipher): arquitectura de M1 no portada.
- ADR-002 (prefijos): arquitectura superada por NPL.
- H6.10 (fractalidad): no portada a M2.
- NPL I3, I9, I10: parciales.
- ADR-004 E-1: no materializado.

**Contradicciones:**
- Autonomía declarada vs `test_compatibilidad_s0.py` (D-C-82).

---

**Fin del análisis de coherencia.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
