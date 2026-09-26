# SCFV_DSR · dsl — Gramática extendida y parser ADL-SCFV

**Módulo:** `~/SCFV_DSR/dsl/`
**Programa:** Investigación SCFV
**Giro:** 04 · Sesión: 4 · Acto: 14
**Fecha:** 2026-09-22
**Autoridad:** Operador (DEDN, C.P.C. Nº 183594)

## 1. Propósito

El módulo implementa la extensión local de la gramática `.scfv` para
ADL-SCFV y su parser correspondiente, conforme a las especificaciones del
Acto 13 (`GIRO_04/13_sintaxis_concreta_adl.md`, hash declarado
`3fc8e7bd…`).

El módulo constituye **infraestructura sintáctica y de parsing**.
No constituye por sí mismo: autoridad normativa, decisión profesional,
motor contable, Diario o Mayor, ni sistema de modificación de datos
contables.

## 2. Autoridad

El parser interpreta sintaxis conforme a la gramática declarada.

Queda expresamente fuera de su autoridad:

- decidir profesionalmente;
- determinar por sí mismo la validez normativa de un hecho;
- contabilizar;
- escribir en Diario o Mayor;
- modificar datos contables;
- sustituir al Motor Contable;
- convertir una declaración sintáctica en una decisión profesional.

## 3. Entradas y salidas

Funciones públicas (heredadas de `parser.py` de S0):

    parse_file(self, filepath: str) -> Dict[str, Any]
    parse_string(self, text: str) -> Dict[str, Any]

La salida conserva las cinco claves históricas de S0:

    fractales, contexto, mandante, tetrada, booleano

y añade tres claves para la extensión:

    contratos, invariantes, asientos_declarados

La salida representa estructura sintáctica procesada.
No constituye decisión profesional ni escritura contable.

## 4. Invariantes del módulo

1. Todo `.scfv` válido bajo S0 deberá continuar siendo aceptado por el
   parser extendido.
2. La extensión será aditiva respecto de la gramática S0.
3. El parser extendido no adquirirá autoridad profesional o contable.
4. S0 permanecerá intacto.

## 5. Dependencias permitidas

- Python 3.11+.
- Lark (versión del entorno actual: 1.3.1).
- Archivos locales del módulo.
- Gramática local derivada de S0 por copia, no por import.

## 6. Dependencias prohibidas

- `%import` de la gramática S0.
- Modificación de archivos bajo `~/SCFV_S0_V1.0.0/`.
- Dependencia de otros árboles de trabajo para resolver producciones.
- Autoridad normativa o contable atribuida al parser.
- Escritura directa a Diario o Mayor.

## 7. Pruebas que validan el módulo

Suite en `tests/`:

- `test_grammar_lalr.py`: construcción LALR sin excepción.
- `test_compatibilidad_s0.py`: los 4 `.scfv` históricos parsean con las
  cinco claves históricas equivalentes a S0.
- `test_contract_def.py`: caso positivo y negativo de `contract_def`.
- `test_invariant_def.py`: caso positivo y negativo de `invariant_def`.
- `test_asiento_declarado_def.py`: caso positivo y negativo de
  `asiento_declarado_def`.

## 8. Bloques PRE/POST/INVARIANTE

### contract_def

- **PRE:** entrada comienza con `CONTRATO`; existe `NAME` identificador;
  los campos obligatorios aparecen en orden.
- **POST:** entrada reconocida; `contratos[NOMBRE]` registra objeto,
  invariantes, elementos y opcionales.
- **INVARIANTE:** no modifica producciones históricas; no redefine tokens
  S0; no convierte la declaración en ejecución.

### invariant_def

- **PRE:** entrada comienza con `INVARIANTE`; existe identificador;
  campos obligatorios en orden.
- **POST:** entrada reconocida; `invariantes[NOMBRE]` registra objeto,
  expresión, dominio, satisfacción, verificación y evidencia.
- **INVARIANTE:** declarar no es demostrar; independiente de
  `contract_def`.

### asiento_declarado_def

- **PRE:** entrada comienza con `ASIENTO_DECLARADO`; existe identificador
  y delimitador `:`.
- **POST:** entrada reconocida; `asientos_declarados[NOMBRE]` registra el
  cuerpo declarado.
- **INVARIANTE:** no se introducen `DEBE`/`HABER` como tokens; no se
  modifica Diario, Mayor ni S0; la declaración no sustituye al Motor
  Contable.
