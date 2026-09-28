# Bloque C-β · Hallazgos consolidados

**Estado:** CERRADO.
**Fecha:** 2026-09-28.
**Fundamento:** C-β.0..6 (34 archivos · 5530 L).
**Naturaleza:** catálogo de fichas de hallazgo. No es matriz. No es cuaderno. Es consolidación.

---

## §0 · Método

Cada hallazgo se registra con: ID · archivo(s) · categoría · descripción · deuda asociada.

Vocabulario de categoría: CONTRACT · IMPLEMENTATION · EVIDENCE · HYPOTHESIS · FALSATION · VALIDATION · DESIGN DECISION · VERDICT.

Categorías especiales de C-β:
- `COHERENCIA-INTERNA` · contradicción interna del propio módulo
- `FRONTERA` · respeto o violación de separación de autoridades
- `DEFECTO-PORT` · defecto introducido durante el port M1→M2
- `CORRECCION-PREVIA` · hallazgo previo precisado o corregido
- `RETIRADO` · hallazgo declarado y luego retirado tras verificación

---

## §1 · Capa kernel (H-C-1..12)

| ID | Archivo | Cat. | Descripción | Deuda |
|---|---|---|---|---|
| H-C-1 | xnor.py | CONTRACT | Materializa ADR-004 §4.3 sin desviación · tres caras equivalentes | — |
| H-C-2 | baldor.py | EVIDENCE | `calcular_base_e_iva` con fórmula correcta · defecto IVA de M1 no replicado | — |
| H-C-3 | baldor.py | DEFECTO-PORT | `sumar_montos` cita `Raw L874-997` pero implementa `sum()` | D-C-1 |
| H-C-4 | baldor.py | DEFECTO-PORT | `verificar_cuadre` cita Baldor L1676+L874 pero el cuadre es I1 del NPL | D-C-2 |
| H-C-5 | baldor.py | DESIGN DECISION | Tolerancia de cuadre `0.001` hardcodeada sin decisión documentada | D-C-3 |
| H-C-6 | xnor.py | DEFECTO-PORT | Sin función inversa (`movimiento_desde_ubicacion`) · duplicación latente | D-C-4 |
| H-C-7 | baldor.py | IMPLEMENTATION | 623 L · archivo individual más grande del corpus técnico | — |
| H-C-8 | baldor.py | EVIDENCE | Fecha 2026-09-25 · día previo al release DSR (26-09) | D-C-8 |
| H-C-9 | baldor.py | RETIRADO | Artefacto de transcripción · no es defecto real | — (retirada D-C-9) |
| H-C-10 | baldor.py | DEFECTO-PORT | `raiz_potencia` no valida dominio para exponentes fraccionarios | D-C-5 |
| H-C-11 | baldor.py | DEFECTO-PORT | `mantisa` puede retornar negativo · contrario a convención tabular | D-C-6 |
| H-C-12 | baldor.py | EVIDENCE | Imports locales `from math import ...` dentro de funciones · estilo inconsistente | — |

---

## §2 · Capa epistemológico (H-C-13..29)

| ID | Archivo | Cat. | Descripción | Deuda |
|---|---|---|---|---|
| H-C-13 | models.py | CONTRACT | `EntidadExtraida` sin campo `fuente` · ADR-004 E-1 no materializado | D-C-12 |
| H-C-14 | models.py | EVIDENCE | `Tetrada` con 7 campos (H,C,E,M,V,X,K) · nombre histórico engañoso | D-C-13 |
| H-C-15 | generador_propuesta.py | DEFECTO-PORT | `idempotency_key` calculada sobre UUID aleatorio · no determinista | D-C-10 |
| H-C-16 | generador_propuesta.py | CONTRACT | `s=0.0`, `t=0.0`, `v=0.0` por defecto · C máximo = 0.50 | D-C-11 |
| H-C-17 | perceptum.py | DEFECTO-PORT | `ALTA_INCERTIDUMBRE` impresa en 2 lugares · ruido estructural | D-C-14 |
| H-C-18 | perceptum.py | DEFECTO-PORT | `confianza_global = min(...)` colapsa a 0 con un solo campo vacío | D-C-15 |
| H-C-19 | intellectus.py · dictum.py | CORRECCION-PREVIA | Caracterizados · D-BB-58 cerrada | — (cerrada) |
| H-C-20 | intellectus.py | DEFECTO-PORT | Comparación por `str().lower()` · coerción forzada a string | — |
| H-C-21 | intellectus.py | CONTRACT | 5 defaults silenciosos · `NIIF_Completas` contradice decisión B de H8P_RETICULO | D-C-16 |
| H-C-22 | intellectus.py | DEFECTO-PORT | Conflicto normativo sólo por `tipo` distinto de `valor` | D-C-17 |
| H-C-23 | dictum.py | IMPLEMENTATION | Emojis en salida de texto de consola · coherente con TUI Curses | — |
| H-C-24 | perceptum.py | CONTRACT | `_extraer_entidades` sólo soporta JSON objeto · resto retorna lista vacía | — |
| H-C-25 | perceptum.py | DEFECTO-PORT | `extraer_lote` sobre JSON objeto no asigna `referencia_fuente` | D-C-18 |
| H-C-26 | generador_propuesta.py | DEFECTO-PORT | `_generar_propuesta_desde_hecho` privada · sin API pública de reuso | D-C-19 |
| H-C-27 | models.py | FRONTERA | `PropuestaH1` depende de `contable/estados.py` · acoplamiento asimétrico | D-C-20 |
| H-C-28 | models.py | CONTRACT | `DecisionProfesional.autor: str` (no Optional) · divergencia con NPL | — |
| H-C-29 | models.py | EVIDENCE | Comentario `# <-- FASE 1: NUEVO CAMPO` · residuo de proceso | D-C-21 |

---

## §3 · Capa contable parte 1 (H-C-30..43)

| ID | Archivo | Cat. | Descripción | Deuda |
|---|---|---|---|---|
| H-C-30 | event_store.py | CORRECCION-PREVIA | `PersistenciaViolacion` existe · import transitivo vía serializador | — (retirada D-C-22) |
| H-C-31 | event_store.py | CORRECCION-PREVIA | D.5 no reproducible en HEAD · `obtener_por_correlation` parsea correctamente | D-C-23 |
| H-C-32 | motor.py | DEFECTO-PORT | `generar_asiento` recibe `verificador` por parámetro y por `__init__` · redundancia | D-C-24 |
| H-C-33 | motor.py | CONTRACT | Default `["NIIF_Completas"]` divergente de `reticulo` | D-C-25 |
| H-C-34 | event_store.py | DEFECTO-PORT | `transaccion()` CM cooperativo · caller debe pasar `commit=False` | D-C-26 |
| H-C-35 | event_store.py | IMPLEMENTATION | `verificar_cadena` O(N) sin incremental | D-C-27 |
| H-C-36 | event_store.py | DEFECTO-PORT | `tipo_evento` restringido a escalares · excluye tipos futuros | D-C-28 |
| H-C-37 | motor.py | CONTRACT | `_validar_moneda` incompatible con `fractales/HIPERINFLACION.scfv` | D-C-29 |
| H-C-38 | nucleo_consecuencias.py | FRONTERA | Normaliza `cuenta → cuenta_codigo` sin contrato explícito | D-C-30 |
| H-C-39 | nucleo_consecuencias.py · motor.py | DEFECTO-PORT | Defaults silenciosos sistemáticos (`"1.0"`, `"VES"`, `["NIIF_Completas"]`) | D-C-31 |
| H-C-40 | motor.py | CORRECCION-PREVIA | `baldor.verificar_cuadre` huérfana con duplicado funcional en `validar_partida_doble` | D-C-32 |
| H-C-41 | motor.py | EVIDENCE | `version_motor: "8.2"` hardcoded en dict de asiento | D-C-33 |
| H-C-42 | motor.py | CONTRACT | Verificación XNOR triple + ubicación declarada · defensa en profundidad | — |
| H-C-43 | nucleo_consecuencias.py | EVIDENCE | Firma duplicada fiscal con Motor · NC valida presencia, Motor valida catálogo | — |

---

## §4 · Capa contable parte 2 (H-C-44..70)

| ID | Archivo | Cat. | Descripción | Deuda |
|---|---|---|---|---|
| H-C-44 | reportes_motor.py | FRONTERA | `_leer_asientos` bypassa `EventStore` · SQL crudo sin hash chain | D-C-44 |
| H-C-45 | reportes_motor.py | DEFECTO-PORT | `generar_csv_balance` clasifica cuentas 4/5 como CAPITAL · ignora 6/7 | D-C-45 |
| H-C-46 | reportes_motor.py · perceptum.py | COHERENCIA-INTERNA | Política stdout inconsistente entre módulos | D-C-46 |
| H-C-47 | reportes_motor.py | DESIGN DECISION | `libros/` en cwd relativo · no configurable | D-C-47 |
| H-C-48 | reportes_motor.py | DEFECTO-PORT | `periodo_id` sin validación de formato | D-C-48 |
| H-C-49 | reportes_motor.py | EVIDENCE | Balance con 0 asientos indistinguible de balance vacío | D-C-49 |
| H-C-50 | reportes_motor.py | EVIDENCE | Marca "SCFV Motor 9.0.0" en docstring · primera aparición en código | — |
| H-C-51 | maquina_estados_asiento.py | COHERENCIA-INTERNA | `es_terminal()` contradice `_TRANSICIONES` para ASENTADO | D-C-34 |
| H-C-52 | maquina_estados_asiento.py | COHERENCIA-INTERNA | Fallback `propuesta_original_id = correlation_id` contradice puente_autorizacion | D-C-35 |
| H-C-53 | maquina_estados_asiento.py | DEFECTO-PORT | `Transicion.hash()` omite `justificacion` y `version_contexto` | D-C-36 |
| H-C-54 | maquina_estados_asiento.py | CONTRACT | `MODIFICADO → EVALUADO` sin revalidación H₂ | D-C-37 |
| H-C-55 | maquina_estados_asiento.py | CONTRACT | Sin transición `ADMITIDO → RECHAZADO` · diseño | — |
| H-C-56 | maquina_estados_asiento.py | DEFECTO-PORT | `propuesta_modificada_id` sobreescribible sin warning | D-C-38 |
| H-C-57 | maquina_estados_asiento.py | COHERENCIA-INTERNA | `Transicion` documentada como inmutable pero no `frozen=True` | D-C-39 |
| H-C-58 | puente_autorizacion.py | FRONTERA | Verificador sin `estado_actual` · coherente con contrato | — |
| H-C-59 | puente_consecuencias.py | IMPLEMENTATION | Validación fuerte de historial · no confía en estado_actual | — |
| H-C-60 | puente_consecuencias.py | DEFECTO-PORT | No revalida `justificacion` no vacía | D-C-41 |
| H-C-61 | maquina_estados_asiento.py | FRONTERA | `transicionar` no persiste historial · write-back no materializado | D-C-42 |
| H-C-62 | maquina_estados_asiento.py | COHERENCIA-INTERNA | `historial` es lista mutable pública | D-C-40 |
| H-C-63 | reportes_motor.py | CONTRACT | Docstring `SCFV Motor 9.0.0` · confirma H-NOM-01 | — |
| H-C-64 | reportes_motor.py | FRONTERA | Acceso paralelo al almacén · no verifica hash chain | D-C-44 |
| H-C-65 | reportes_motor.py | DESIGN DECISION | `libros/` cwd relativo | D-C-47 |
| H-C-66 | perceptum.py · reportes_motor.py | COHERENCIA-INTERNA | Contradicción de política stdout | D-C-46 |
| H-C-67 | reportes_motor.py | DEFECTO-PORT | Clasificación histórica incorrecta de cuentas 4/5 | D-C-45 |
| H-C-68 | reportes_motor.py | CONTRACT | `_leer_asientos` sin verificar período declarado | — |
| H-C-69 | reportes_motor.py | DEFECTO-PORT | `periodo_id` sin validación formato | D-C-48 |
| H-C-70 | reportes_motor.py | EVIDENCE | Balance vacío silencioso | D-C-49 |

---

## §5 · Capa profesional + top-level (H-C-71..84)

| ID | Archivo | Cat. | Descripción | Deuda |
|---|---|---|---|---|
| H-C-71 | orquestador.py | CORRECCION-PREVIA | `MotorContable(None)` en `orquestador.py`, no en `exportador.py` | D-C-50 |
| H-C-72 | orquestador.py | DEFECTO-PORT | `version_contexto` reducido a `{version_id}` · pérdida de trazabilidad | D-C-51 |
| H-C-73 | orquestador.py | CONTRACT | Máquina arranca en EVALUADO · PROPUESTO no operacional | D-C-52 |
| H-C-74 | orquestador.py | DEFECTO-PORT | H2 retorna decision y orquestador re-obtiene vía Provider | D-C-53 |
| H-C-75 | evaluador.py | DEFECTO-PORT | Sólo 3 ops a Baldor · 15+ duplicadas inline | D-C-54 |
| H-C-76 | extractor.py | DEFECTO-PORT | Reimplementa hash de Evidencia · divergencia silenciosa | D-C-55 |
| H-C-77 | extractor.py | DEFECTO-PORT | `dict_desde_observacion` con `except: pass` silencioso | D-C-56 |
| H-C-78 | integrador.py | FRONTERA | `sys.path.insert` en tiempo de import · rompe encapsulamiento | D-C-57 |
| H-C-79 | integrador.py | DEFECTO-PORT | `_importar_version_contexto` con fallback de 3 ubicaciones | D-C-58 |
| H-C-80 | integrador.py | DEFECTO-PORT | `timestamp=1756800000` (2025-09-02) hardcoded · rompe reportes | D-C-59 |
| H-C-81 | integrador.py | DEFECTO-PORT | `confianza_global=0.95` hardcoded · no usa Perceptum | D-C-60 |
| H-C-82 | integrador.py | DEFECTO-PORT | `_consecuencia_a_candidata` pierde `es_fiscal`/`norma_id` | D-C-61 |
| H-C-83 | integrador.py | EVIDENCE | Único punto que invoca `verificar_cadena()` tras ciclo | — |
| H-C-84 | integrador.py | IMPLEMENTATION | Contrato de retorno expone 4 claves (consecuencias, candidata, resultado, cadena) | — |

---

## §6 · Capa infra + dsl (H-C-85..113)

| ID | Archivo | Cat. | Descripción | Deuda |
|---|---|---|---|---|
| H-C-85 | parser.py | EVIDENCE | "SCFV S0 v7.2" · quinta marca de versión | D-C-62 |
| H-C-86 | parser.py | EVIDENCE | Hash `eebba48b…` truncado · no verificable desde M2 | D-C-63 |
| H-C-87 | parser.py | DEFECTO-PORT | `_as_expr_node` código muerto | D-C-64 |
| H-C-88 | parser.py | DEFECTO-PORT | 7 de 8 claves de `_transform_tree` sin consumidor en M2 | D-C-65 |
| H-C-89 | parser.py | DEFECTO-PORT | `_extraer_por_keywords` frágil ante keywords en valores | D-C-66 |
| H-C-90 | parser.py | DEFECTO-PORT | `_handle_contract` / `_handle_invariant` con índices posicionales | D-C-67 |
| H-C-91 | parser.py · evaluador.py | COHERENCIA-INTERNA | Doble parsing de `condition` · parser serializa a string | D-C-68 |
| H-C-92 | parser.py · evaluador.py | COHERENCIA-INTERNA | Doble parsing de `action` | D-C-69 |
| H-C-93 | parser.py | CONTRACT | `Lark(parser="lalr")` sin manejo de conflicto shift/reduce | D-C-70 |
| H-C-94 | parser.py | DEFECTO-PORT | Sin caching del LALR · reconstrucción por instancia | D-C-71 |
| H-C-95 | parser.py | DEFECTO-PORT | `_get_node_value` retorna `None` silencioso | D-C-72 |
| H-C-96 | parser.py | DEFECTO-PORT | Extensión v7.2 sin consumidor en M2 | D-C-73 |
| H-C-97 | serializador_canonico.py | CORRECCION-PREVIA | `PersistenciaViolacion` definida en este módulo | — (retirada D-C-22) |
| H-C-98 | serializador_canonico.py | DEFECTO-PORT | Chequeo redundante con `str(campo.default)` | D-C-74 |
| H-C-99 | serializador_canonico.py | DEFECTO-PORT | `_tipo_optional` no cubre `X | None` (PEP 604) | D-C-75 |
| H-C-100 | serializador_canonico.py | DEFECTO-PORT | Sin soporte `set`/`frozenset` · `_hacer_inmutable` muerto | D-C-76 |
| H-C-101 | serializador_canonico.py | DEFECTO-PORT | `serializar` sin `sort_keys` · determinismo delegado | D-C-77 |
| H-C-102 | serializador_canonico.py | DEFECTO-PORT | `Union[X, Y]` sin None cae silenciosamente | D-C-78 |
| H-C-103 | serializador_canonico.py | DEFECTO-PORT | Recorre todos los campos de dataclass sin filtrar `init=False` | D-C-79 |
| H-C-104 | serializador_canonico.py | DEFECTO-PORT | Sin versión del contrato canónico persistida | D-C-80 |
| H-C-105 | serializador_canonico.py | EVIDENCE | `List[Any]` se maneja por accidente, no por diseño | — |
| H-C-106 | serializador_canonico.py | DEFECTO-PORT | `None` como clave de dict permitido · roundtrip inconsistente | D-C-81 |
| H-C-107 | test_compatibilidad_s0.py | FRONTERA | Hardcodea `~/scfv_v6/` · dependencia M2 → M1 oculta | D-C-82 |
| H-C-108 | dsl/tests/*.py | DEFECTO-PORT | `sys.path.insert` replicado en 5 tests | D-C-83 |
| H-C-109 | test_contract_def.py | EVIDENCE | `try/except` en lugar de `pytest.raises` | D-C-84 |
| H-C-110 | test_grammar_lalr.py | DEFECTO-PORT | No valida transformación de árbol | D-C-85 |
| H-C-111 | test_invariant_def.py | DEFECTO-PORT | Valida 2 de 7 campos | D-C-86 |
| H-C-112 | dsl/tests/*.py | DEFECTO-PORT | Ningún test ejercita `_extraer_por_keywords` con valores literales | D-C-87 |
| H-C-113 | test_compatibilidad_s0.py | DEFECTO-PORT | Sólo verifica presencia de claves, no contenido | D-C-88 |

---

## §7 · Retirados y corregidos

| ID | Estado | Causa |
|---|---|---|
| H-C-9 | RETIRADO | Artefacto de transcripción · no es defecto real |
| H-C-30 | REFORMULADO | `PersistenciaViolacion` existe · no es deuda |
| H-C-97 | REFORMULADO | Cierra la reserva de H-C-30 |
| H-C-107 | CORRECCION-PREVIA | Afecta declaración de autonomía del README |

---

## §8 · Balance

```

Total hallazgos activos:    110 (retirado H-C-9)
Distribución por categoría:
CONTRACT                      ~20
DEFECTO-PORT                  ~40
COHERENCIA-INTERNA             ~8
FRONTERA                       ~7
EVIDENCE                      ~15
IMPLEMENTATION                 ~5
DESIGN DECISION                ~4
CORRECCION-PREVIA              ~6
RETIRADO                        1

```

Familias estructurales:

- **F-1 · Determinismo y hashing** (H-C-10, 15, 51, 53, 72, 77, 80, 101, 104)
- **F-2 · Coherencia interna de módulos** (H-C-34, 51, 52, 57, 62, 91, 92)
- **F-3 · Defaults silenciosos** (H-C-16, 21, 31, 39, 47, 48, 59, 60)
- **F-4 · Frontera y separación de autoridades** (H-C-27, 32, 44, 57, 64, 78, 107)
- **F-5 · Duplicación de código** (H-C-40, 54, 75, 76, 79, 88, 96)
- **F-6 · Documentación inflada o desalineada** (H-C-3, 4, 5, 7, 41, 63, 85, 86)
- **F-7 · Tests débiles** (H-C-84, 85, 86, 87, 88, 109, 110, 111, 113)

---

**Fin del catálogo de hallazgos.**
**Este documento no tiene autoridad normativa. Es constancia de un bloque de auditoría.**
