# Auditoría técnica SCFV_DSR · 2026-09-26

**Commits auditados**: e0923e4 (fundación) → abb2bac (FASE 1)
**Acto posterior, no auditado**: 4eca9d5 (autoflake, cierre de ventana)
**Artefacto**: SCFV_DSR v0.1.0
**Régimen**: solo lectura durante auditoría · escritura autorizada por archivo

> **Ubicación provisoria.** Este documento vive en `DOCS/` del port porque
> el árbol canónico del Programa (ACTAS/) no fue verificado en esta
> ventana. Migrar cuando corresponda.

---

## Estado verificado del artefacto

| Hecho | Método | Valor |
|---|---|---|
| Módulos Python | `find` + `wc -l` | 43 · 5 445 LOC |
| Tests DSL | `pytest` | 7 passed |
| Eventos en DB | `SELECT COUNT(*)` | 285 |
| `correlation_id` únicos | `SELECT COUNT(DISTINCT)` | 149 |
| Ciclos completos (2 eventos) | `GROUP BY HAVING COUNT(*)=2` | 136 |
| Ciclos huérfanos (1 evento) | `GROUP BY HAVING COUNT(*)=1` | 13 |
| Tipo de huérfanos | `SELECT tipo_evento` | 100% `DECISION_H2` |
| Eslabones rotos en cadena de hashes | `verificar_cadena()` | 0 |
| Duplicados por `idempotency_key` | constraint UNIQUE | 0 |

---

## Hallazgo 1 · Ciclos huérfanos por falta de atomicidad transaccional

**Evidencia**: 13 `correlation_id` con `DECISION_H2` sin `ASIENTO_REGISTRADO`. Todos con `tipo_decision=ACEPTAR`. Los timestamps, según el informe original, se concentran en una sola sesión de desarrollo (2026-09-25). No re-verificado en esta ventana.

**Mecanismo causal identificado y reproducido** (H1): con evidencia incompleta para el fractal INVENTARIOS (`{"tipo":"compra_inventario","activo_es_inventario":true,"monto":100.0}`), el pipeline produce `monto=0` en la primera partida. `nucleo_consecuencias.py:197` dispara `NC_VIOLACION: partida 0 con monto inválido`. La decisión H2 ya estaba persistida. Sin rollback envolvente, queda huérfana.

**Mecanismo**: `orquestador.py` persistía `DECISION_H2` (paso 2) y `ASIENTO_REGISTRADO` (paso 9) en dos `commit()` separados. Cualquier excepción entre ambos deja la decisión huérfana.

La reproducción demuestra que este mecanismo puede producir un huérfano; no establece que haya sido la causa individual de cada uno de los 13 huérfanos históricos.

**Estado**: resuelto en FASE 1 (commit `abb2bac`).

---

## Hallazgo 2 · Dos arquitecturas paralelas no coordinadas

**Evidencia**:

- `maquina_estados_asiento.py`: historial de transiciones vive en RAM (`self.historial: List[Transicion]`). Lectura parcial del módulo, no verificada la totalidad.
- `event_store.py`: fuente de verdad persistente en SQLite con cadena de hashes.

**Consecuencia**: la máquina de estados no puede reconstruir su historial desde la DB. El ciclo ADMITIDO → ASENTADO no queda registrado como evento.

**Estado**: trabajo futuro (FASE 3).

---

## Hallazgo 3 · Módulos formales huérfanos de llamada

| Módulo | Funciones públicas | Consumidores externos | Evidencia |
|---|---|---|---|
| `kernel/baldor.py` | 52 (`grep -c "^def "`) | 0 | `grep -rn "baldor\."` = 0 |
| `epistemologico/intellectus.py` | 3 | 0 | nadie lo importa |
| `epistemologico/dictum.py` | 1 | 0 | nadie lo importa |

**Cadena declarada**: `perceptum → intellectus → dictum → evidencia` (Documento Fundacional).

**Cadena ejecutada**: `perceptum → evidencia` (intellectus y dictum omitidos).

**Consecuencia**: H2 decide sin pasar por análisis normativo. Las 52 funciones formales de Baldor están implementadas con locus declarado por línea, pero ninguna se invoca. Las 6 operaciones con `funcion_baldor` declarado en `operaciones.json` no despachan a Baldor.

**Estado**: FASE 2 (Baldor) y FASE 4 (intellectus/dictum) pendientes.

---

## Hallazgo 4 · El adaptador no propaga campos de fiscalidad

**Evidencia** (`integrador.py:89-99`):

```python
def _consecuencia_a_candidata(consecuencias):
    return [
        {
            "cuenta": c["cuenta"],
            "monto": float(c["monto"]),
            "naturaleza": c["naturaleza"],
            "movimiento": c["movimiento"],
        }
        for c in consecuencias
    ]

```

El adaptador reduce cada consecuencia a 4 campos. No propaga es_fiscal ni norma_id.

Consecuencia: las ramas de validación que dependen de es_fiscal y norma_id no reciben esos campos a través de este camino de producción. Esto incluye la validación I6 del Motor (motor.py:160-161) y de NC (nucleo_consecuencias.py:243-249).

Estado: hallazgo documental. Corregir requeriría extender el DSL del fractal para declarar fiscalidad.

---

Hallazgo 5 · Tipos de evento no emitidos

Tres planos distintos:

· Enum declarado (contable/estados.py): 18 miembros en TipoEvento.
· Emisión como miembro del Enum: solo TipoEvento.DECISION_H2 se emite como miembro. ASIENTO_REGISTRADO se persiste como string directo, no como TipoEvento.ASIENTO_REGISTRADO. Los otros 17 miembros no se emiten.
· Persistencia en DB (event_store.tipo_evento): solo 2 valores presentes.

```
DECISION_H2        149
ASIENTO_REGISTRADO 136
```

Consecuencia: el enum documenta intenciones que el pipeline no ejecuta. 16 tipos declarados no aparecen en la DB.

Estado: hallazgo documental.

---

Hallazgo 6 · Autor sin CPC profesional identificado

Evidencia: los 149 eventos DECISION_H2 tienen autor = "PROFESIONAL_NO_IDENTIFICADO".

Causa: no determinada en esta ventana. Podría ser variable de entorno no seteada, default de código, o constante. Requiere verificación adicional.

Consecuencia: las decisiones H2 no están firmadas por un profesional identificado. La trazabilidad profesional está vacía.

Estado: hallazgo documental.

---

Hallazgo 7 · Concatenación ambigua en la cadena de hashes

Evidencia (event_store.py, cálculo de hash_actual):

```python
datos = (
    payload_json
    + version_json
    + correlation_id
    + idempotency_key
    + hash_previo
)
hash_actual = hashlib.sha256(datos.encode("utf-8")).hexdigest()
```

Los 5 campos se concatenan sin separador. Esto introduce una ambigüedad estructural de serialización: representaciones distintas de los campos pueden producir la misma cadena de entrada al hash.

Ejemplo: con los demás campos fijos,

· (payload="a", campo="bc")
· (payload="ab", campo="c")

producen la misma concatenación abc.

No es una colisión criptográfica de SHA-256. Es una ambigüedad de serialización previa al hash.

Estado: hallazgo declarado. Corregir requiere versionado de algoritmo (los 285 hashes existentes quedarían inválidos con cualquier cambio). Decisión arquitectónica mayor, fuera del alcance de FASE 1.

---

Hallazgo 8 · Régimen de falsación sin criterio de parada

Evidencia: durante la ventana se registraron 20 falsaciones (F1–F20) sobre el diff de FASE 1 (3 archivos). Las rondas posteriores no produjeron un defecto funcional adicional en el mecanismo bajo prueba.

Patrón:

· Ronda 1 · diff 15 líneas → 8 falsaciones
· Ronda 2 · diff +30% → 6 falsaciones
· Ronda 3 · diff +30% → 6 falsaciones

Sin un criterio de parada declarado a priori, la revisión continuó ampliando la superficie de casos límite.

Corrección adoptada: el test es el juez. Si el test pasa, la intervención se cierra. La falsación posterior verifica el test, no el ideal de perfección.

Estado: hallazgo metodológico · régimen corregido para esta ventana.

---

Hallazgos metodológicos · retirados del informe original

Los siguientes fueron introducidos en versiones tempranas del informe y retirados tras falsación:

Elemento Motivo de retiro
Título "Deuda epistémica en artefactos DSR" Generalización no demostrada a partir de un artefacto
Puntuación "Hevner: 3.7/5" Hevner no define escala 0–5. Era rúbrica propia
"Veredicto Lakatos: progresivo" Requiere trayectoria histórica con predicciones corroboradas
"40% de módulos formales huérfanos" Sin denominador canónico
"Cadena epistémica incompleta" Concepto ≠ módulo Python. Falta canon que ligue ambos
"H2 no recibe normas" No se trazó la ruta de llamada

Nota: retirada del informe ≠ falsación del concepto. "Deuda epistémica" permanece como hipótesis conceptual no operacionalizada.

---

Trabajo futuro

Fase Objetivo Estado
FASE 2 Cableado de Baldor · 6 operaciones despachan por funcion_baldor Contratos verificados · implementación aún no iniciada
FASE 3 Persistencia del historial de máquina Decisión arquitectónica pendiente
FASE 4 Cableado intellectus → dictum Canon no identificado
— Migración de 13 huérfanos históricos Decisión: dejar como registro pre-FASE-1
— Redefinir "huérfano" en tests y docs DECISION_H2 sin ASIENTO_REGISTRADO

---

Referencias internas

· Commit FASE 1: abb2bac
· Commit autoflake (posterior, no auditado): 4eca9d5
· DB auditada: var/scfv.db (285 eventos, CADENA_INTEGRA)
· Test FASE 1: ~/test_fase1_atomicidad.py (PASS)
· Backup FASE 1: ~/scfv_backup_fase1_*/
