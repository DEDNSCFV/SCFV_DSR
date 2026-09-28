# Bloque C-β · Deudas registradas

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** C-β.0..6 (34 archivos · 5530 L).
**Naturaleza:** registro de deudas nuevas. No resuelve. No prioriza. Trazabiliza.

---

## §0 · Método

Cada deuda se registra con: ID · archivo(s) · descripción · estado (ABIERTA).

Sin priorización. Sin asignación de destino. El acto de clasificar destino corresponde a un acto posterior.

---

## §1 · Kernel y Baldor · D-C-1..8

| ID | Archivo | Descripción |
|---|---|---|
| D-C-1 | baldor.py | `sumar_montos` cita `Raw L874-997` pero implementa `sum()` · documentación inflada |
| D-C-2 | baldor.py | `verificar_cuadre` cita Baldor L1676+L874 pero el cuadre es I1 del NPL · locus impropio |
| D-C-3 | baldor.py | Tolerancia de cuadre `0.001` hardcodeada sin decisión documentada |
| D-C-4 | xnor.py | Sin función inversa (`movimiento_desde_ubicacion`) · duplicación latente en consumidores |
| D-C-5 | baldor.py | `raiz_potencia` no valida dominio para exponentes fraccionarios |
| D-C-6 | baldor.py | `mantisa` puede retornar negativo · contrario a convención tabular |
| D-C-7 | baldor.py | Consumidores de `baldor.py` no verificados exhaustivamente |
| D-C-8 | baldor.py | Fecha 2026-09-25 revela ciclo corto de maduración · no hay acta de origen |

---

## §2 · Epistemológico · D-C-10..21

| ID | Archivo | Descripción |
|---|---|---|
| D-C-10 | generador_propuesta.py | `idempotency_key` calculada sobre UUID aleatorio · no determinista · no dispara I7 |
| D-C-11 | generador_propuesta.py | `s`, `t`, `v` inoperativos por defecto · C máximo = 0.50 |
| D-C-12 | models.py | `EntidadExtraida` sin campo `fuente` · E-1 de ADR-004 no materializado |
| D-C-13 | models.py | `Tetrada` con 7 campos · nombre histórico engañoso |
| D-C-14 | perceptum.py | `ALTA_INCERTIDUMBRE` impresa sin nivel ni contexto · ruido estructural |
| D-C-15 | perceptum.py | `confianza_global = min(...)` colapsa a 0 con un solo campo vacío |
| D-C-16 | intellectus.py | 5 defaults silenciosos · `NIIF_Completas` contradice decisión B de H8P_RETICULO |
| D-C-17 | intellectus.py | Detecta conflictos sólo por `tipo` distinto de `valor` |
| D-C-18 | perceptum.py | `extraer_lote` sobre JSON objeto no asigna `referencia_fuente` |
| D-C-19 | generador_propuesta.py | `_generar_propuesta_desde_hecho` privada · no hay API pública para reutilizar hecho |
| D-C-20 | models.py · estados.py | `epistemologico/` depende de `contable/estados.py` · acoplamiento asimétrico |
| D-C-21 | models.py | Comentario `# <-- FASE 1: NUEVO CAMPO` · residuo de proceso |

---

## §3 · Contable parte 1 · D-C-23..33

| ID | Archivo | Descripción |
|---|---|---|
| D-C-23 | event_store.py | D.5 no reproducible en HEAD · requiere reformulación |
| D-C-24 | motor.py | `generar_asiento` recibe `verificador` por parámetro y por `__init__` · redundancia |
| D-C-25 | motor.py | `MotorContable` default `["NIIF_Completas"]` divergente de `reticulo` |
| D-C-26 | event_store.py | `transaccion()` CM cooperativo · caller debe pasar `commit=False` · atomicidad no forzosa |
| D-C-27 | event_store.py | `verificar_cadena` O(N) sin incremental |
| D-C-28 | event_store.py | `tipo_evento` restringido a escalares · puede excluir tipos futuros |
| D-C-29 | motor.py | `_validar_moneda` incompatible con `fractales/HIPERINFLACION.scfv` · multimoneda no soportada |
| D-C-30 | nucleo_consecuencias.py | Normaliza `cuenta → cuenta_codigo` sin contrato explícito |
| D-C-31 | nucleo_consecuencias.py · motor.py | Defaults silenciosos (`"1.0"`, `"VES"`, `["NIIF_Completas"]`) sin decisión documentada |
| D-C-32 | motor.py | `baldor.verificar_cuadre` huérfana con duplicado funcional en `motor.validar_partida_doble` |
| D-C-33 | motor.py | `version_motor: "8.2"` hardcoded · no parametrizable |

---

## §4 · Contable parte 2 · D-C-34..49

| ID | Archivo | Descripción |
|---|---|---|
| D-C-34 | maquina_estados_asiento.py | `es_terminal()` contradice `_TRANSICIONES` para ASENTADO |
| D-C-35 | maquina_estados_asiento.py | Fallback silencioso `propuesta_original_id = correlation_id` · contradice comentario explícito |
| D-C-36 | maquina_estados_asiento.py | `Transicion.hash()` omite `justificacion` y `version_contexto` · hash incompleto |
| D-C-37 | maquina_estados_asiento.py | `MODIFICADO → EVALUADO` sin revalidación H₂ · caller-responsabilidad |
| D-C-38 | maquina_estados_asiento.py | `propuesta_modificada_id` sobreescribible sin warning |
| D-C-39 | maquina_estados_asiento.py | `Transicion` documentada como inmutable pero no `frozen=True` |
| D-C-40 | maquina_estados_asiento.py | `historial` es lista mutable pública · no protegida |
| D-C-41 | puente_consecuencias.py | No revalida `justificacion` no vacía |
| D-C-42 | maquina_estados_asiento.py | `transicionar` no persiste historial · write-back no materializado |
| D-C-43 | reportes_motor.py | Verificación de encabezado pendiente (resuelta en C-β.4-bis) |
| D-C-44 | reportes_motor.py | `_leer_asientos` bypassa `EventStore` · acceso SQL directo sin hash chain |
| D-C-45 | reportes_motor.py | `generar_csv_balance` clasifica cuentas 4/5 como CAPITAL · ignora cuentas 6/7 · balance no cuadra |
| D-C-46 | reportes_motor.py · perceptum.py | Política stdout inconsistente entre módulos |
| D-C-47 | reportes_motor.py | `libros/` en cwd relativo · no configurable |
| D-C-48 | reportes_motor.py | `periodo_id` sin validación de formato |
| D-C-49 | reportes_motor.py | Balance con 0 asientos indistinguible de balance vacío por clasificación |

---

## §5 · Profesional + top-level · D-C-50..61

| ID | Archivo | Descripción |
|---|---|---|
| D-C-50 | orquestador.py | `MotorContable(None)` ubicado en `orquestador.py`, no en `exportador.py` · discrepancia con H7H/H9 |
| D-C-51 | orquestador.py | `version_contexto` reducido a `{version_id}` · pérdida de trazabilidad de versiones |
| D-C-52 | orquestador.py | Máquina arranca en EVALUADO · estado PROPUESTO no operacional |
| D-C-53 | orquestador.py | H2 retorna `decision` y orquestador re-obtiene vía Provider · doble camino |
| D-C-54 | evaluador.py | `evaluar_operacion` sólo despacha 3 ops a Baldor · 15+ duplicadas inline |
| D-C-55 | extractor.py | Reimplementa hash de Evidencia · divergencia silenciosa posible |
| D-C-56 | extractor.py | `dict_desde_observacion` con `except: pass` silencioso |
| D-C-57 | integrador.py | `sys.path.insert` en tiempo de import · rompe encapsulamiento |
| D-C-58 | integrador.py | `_importar_version_contexto` con fallback de 3 ubicaciones |
| D-C-59 | integrador.py | `_construir_observacion` con `timestamp=1756800000` (2025-09-02) · rompe reportes |
| D-C-60 | integrador.py | `_construir_observacion` con `confianza_global=0.95` hardcoded |
| D-C-61 | integrador.py | `_consecuencia_a_candidata` pierde `es_fiscal`/`norma_id` · fractales DSR no pueden producir partidas fiscales |

---

## §6 · Parser DSL · D-C-62..73

| ID | Archivo | Descripción |
|---|---|---|
| D-C-62 | parser.py | "SCFV S0 v7.2" · quinta marca de versión sin mapeo |
| D-C-63 | parser.py | Hash `eebba48b…` de parser previo truncado · no verificable desde M2 |
| D-C-64 | parser.py | `_as_expr_node` código muerto · declarada sin invocación |
| D-C-65 | parser.py | 7 de 8 claves de `_transform_tree` sin consumidor en M2 |
| D-C-66 | parser.py | `_extraer_por_keywords` frágil ante keywords en valores literales |
| D-C-67 | parser.py | `_handle_contract` / `_handle_invariant` dependen de índices posicionales del árbol |
| D-C-68 | parser.py · evaluador.py | Doble parsing de `condition` · parser serializa a string · evaluador re-parsea con regex |
| D-C-69 | parser.py · evaluador.py | Doble parsing de `action` · `GENERAR CONSECUENCIA` serializado a string |
| D-C-70 | parser.py | `Lark(parser="lalr")` sin manejo de conflicto shift/reduce en `__init__` |
| D-C-71 | parser.py | `SCFVParser` reconstruye el LALR en cada instanciación · sin caching |
| D-C-72 | parser.py | `_get_node_value` retorna `None` silencioso para nodos opacos |
| D-C-73 | parser.py | Extensión v7.2 (CONTRATO/INVARIANTE/ASIENTO_DECLARADO) sin consumidor en M2 |

---

## §7 · Serializador canónico · D-C-74..81

| ID | Archivo | Descripción |
|---|---|---|
| D-C-74 | serializador_canonico.py | Chequeo redundante y frágil con `str(campo.default)` |
| D-C-75 | serializador_canonico.py | `_tipo_optional` no cubre `X | None` (PEP 604) · sin `types.UnionType` |
| D-C-76 | serializador_canonico.py | `serializar` no acepta `set`/`frozenset` · `_hacer_inmutable` de `evidencia.py` es código muerto |
| D-C-77 | serializador_canonico.py | `serializar` sin `sort_keys` · determinismo delegado al llamador |
| D-C-78 | serializador_canonico.py | `Union[X, Y]` sin None cae silenciosamente sin tipado |
| D-C-79 | serializador_canonico.py | `serializar` recorre todos los campos de dataclass · sin filtrar `init=False` |
| D-C-80 | serializador_canonico.py | Sin versión del contrato canónico persistida en eventos |
| D-C-81 | serializador_canonico.py | `None` como clave de dict permitido · roundtrip JSON inconsistente |

---

## §8 · Tests DSL · D-C-82..88

| ID | Archivo | Descripción |
|---|---|---|
| D-C-82 | test_compatibilidad_s0.py | Hardcodea `~/scfv_v6/` · dependencia M2 → M1 oculta · contradice README de autonomía |
| D-C-83 | dsl/tests/*.py | `sys.path.insert` replicado en 5 tests · coexistencia con `pyproject.toml` sin resolver |
| D-C-84 | test_contract_def.py | `test_contract_negativo` con `try/except` en lugar de `pytest.raises` |
| D-C-85 | test_grammar_lalr.py | No valida transformación de árbol |
| D-C-86 | test_invariant_def.py | Valida 2 de 7 campos del invariante |
| D-C-87 | dsl/tests/*.py | Ningún test ejercita `_extraer_por_keywords` con valores literales que coincidan con keywords |
| D-C-88 | test_compatibilidad_s0.py | Sólo verifica presencia de claves, no contenido |

---

## §9 · Retiradas

| ID | Motivo |
|---|---|
| D-C-9 | Retirada · la aparente sintaxis rota de `evidencia.py` fue artefacto de transcripción |
| D-C-22 | Retirada · `PersistenciaViolacion` existe en `serializador_canonico.py` |

---

## §10 · Total

```

D-C-1..8            8 deudas   kernel
D-C-10..21         12 deudas   epistemológico  (D-C-9 retirada)
D-C-23..33         11 deudas   contable p1     (D-C-22 retirada)
D-C-34..49         16 deudas   contable p2
D-C-50..61         12 deudas   profesional + top
D-C-62..73         12 deudas   parser DSL
D-C-74..81          8 deudas   serializador
D-C-82..88          7 deudas   tests DSL
─────
86 deudas activas

D-C-9 · D-C-22      2 retiradas

```

---

## §11 · Estados

```

D-C-1..88           ABIERTAS · sin resolución
D-C-9 · D-C-22      RETIRADAS

```

Ninguna deuda se resuelve en este documento. El registro es para trazabilidad futura.

---

**Fin del catálogo de deudas.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
