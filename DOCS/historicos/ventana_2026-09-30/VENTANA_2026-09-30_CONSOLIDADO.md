═══════════════════════════════════════════════════════════════
VENTANA 2026-09-30 · CONSOLIDADO DE TRABAJO
═══════════════════════════════════════════════════════════════

ESTATUTO:        HISTÓRICO / DOCUMENTO DE TRABAJO
NO ES ARTEFACTO SCFV_DSR
NO MODIFICA CÓDIGO
NO MODIFICA TESTS
NO MODIFICA ADRs
NO MODIFICA README
NO RESUELVE DEUDAS
NO RECLASIFICA
NO ES ACTO
NO SE FIRMA §20

FECHA:           2026-09-30
VENTANA:         privada
RÉGIMEN:         documento histórico · no materializado

NOTA DE ALCANCE
Este consolidado es un ANCLA DE TRANSFERENCIA a Fase B.
NO es expediente íntegro del chat.
Las falsaciones se registran como índice (§3), no como texto completo.

═══════════════════════════════════════════════════════════════
§0 · METADATOS
═══════════════════════════════════════════════════════════════

Objeto de la ventana
  Análisis de las deudas registradas en la auditoría externa
  del artefacto SCFV_DSR · corpus DOCS/historicos/auditoria_2026-09-28/

Fuente primaria
  bloque_M_deudas_catalogo_consolidado.md · 504 L

Frontera ampliada durante la ventana
  · 13 archivos de auditoría en ~/scfv-dsr/DOCS/historicos/
  · ~/scfv_v6/DOCS/H8P_IMPORTADOR_CONTRATO.md §22.4
  · ~/scfv_v6/PODERES/CONTABLE/importador_s0.py L125–194
  · ~/scfv_v6/TESTS/test_importador_s0.py (cabeceras)
  · ~/scfv_v6/DOCS/adrs/ (ADR-000..005 cabeceras)
  · git log · git show · git diff del repo ~/scfv-dsr

STOP materialización del artefacto
  vigente durante toda la ventana · no levantado

═══════════════════════════════════════════════════════════════
§1 · SÍNTESIS EJECUTIVA
═══════════════════════════════════════════════════════════════

Cobertura del cuerpo M: 350 / 350 deudas examinadas
Cierres verificados:    1  (D-C-26)
Cierres documentales:   1  (D-BB-58)
Retiradas:              3  (D-C-9 · D-C-22 · D-Cα-100)
Candidatas:             3  (D-CONV-4 · D-Cα-69 · D-BB-57)
Abiertas / material:    ~330  (discrepancia declarada: ver §5)
Sin estado:             ~30
Universo mínimo:        > 368  (350 M + externos + fuera de M)

Documentos de trabajo producidos: 6
  v0.1.3 · v0.2.2 · v0.3.1 · v0.4.2 · v0.5.1 · v1.0

Falsaciones registradas: ~50  (F1–FZ · varias retiradas)

Hallazgos estructurales:
  F-H   deuda sin trazabilidad a M
  F-Z   reparación sin deuda correspondiente en M
  F-AB  familia D-EPIST-1..7 fuera de M
  F-X   git es la única capa del corpus con reparaciones materiales
  F-AH  la propia sesión reprodujo el patrón que M ya había advertido

═══════════════════════════════════════════════════════════════
§2 · DOCUMENTOS DE TRABAJO
═══════════════════════════════════════════════════════════════

§2.1 · v0.1.3 · TAXONOMÍA OBSERVADA DE M-DEUDAS

Método
  Descripción de estructuras observables en M-deudas.
  Cada estrato lleva locus · criterio de inclusión · frontera.

9 estratos (original) → 8 vigentes (E8 retirado tras falsación IA-1)

E1  FAMILIA / REGISTRO
    Locus: M §2–§7
    Criterio: encabezado §X con rango declarado · granularidad variable
    Familias: D-B · D-BB · D-IMP · D-C · D-Cα · M1α · M1β · M1γ · M1δ · DM
    Total cuerpo: 350

E2  ESTADO
    Locus: M §1 · L39
    7 valores: ABIERTA · CONFIRMADA · REFORMULADA · RETIRADA
               CERRADA DOCUMENTALMENTE · CERRADA VERIFICADA
               REFERENCIA CORRECTIVA
    CERRADA VERIFICADA no aparece en ningún registro · columna huérfana en L372

E3  ANOMALÍA INTERFUENTE
    Locus: M §8 · A1..A10
    Heterogéneo · 5 subclases:
      ERROR DEL CORPUS          A1 · A7 · A10
      AMBIGÜEDAD RESUELTA R3    A2 · A3
      CORRECCIÓN DE CATALOGACIÓN A4
      ARTEFACTO ARITMÉTICO      A5
      ALCANCE DC-8              A6 · A8 · A9

E4  ERROR PROPIO
    Locus: M §9 · E1..E13
    13 errores de la auditoría · no del corpus

E5  DEUDA META
    DC-1 (§0) · DC-8 (A8/A9) · DC-10 (§3)
    §0 declara solo DC-1 · subdeclaración registrada

E6  NUMERACIÓN
    13 conjuntos de identificadores detectados
    Solo O1..O43 es nombrado como problema por M (DM-4)

E7  FUENTE / CADENA
    §0 · L18 · 8 bases declaradas por M
    §2–§7 · atribuciones de origen por familia
    Dos funciones distintas agrupadas

E8  (RETIRADO)
    D-Cα-127 no es estrato independiente
    M lo declara explícitamente REFERENCIA CORRECTIVA
    Absorbido por E2

E9  ALCANCE EXTERNO
    D-CONV-1..15 · A6 · alcance declarado por M
    No es propiedad intrínseca

─────────────────────────────────────────────────────────────

§2.2 · v0.2.2 · SEPARACIÓN POR ESTATUTO

Método
  Asignación de objetos de M a los estratos observados.
  Sin interpretar · sin resolver · sin construir inventario.

Reglas aplicadas
  RA1  un objeto puede pertenecer a más de un estrato
  RA2  no se fusiona C-1 / C-2
  RA3  no se interpreta estado
  RA4  NO-ASIGNADO solo para objetos sin ningún estrato
  RA5  identidad de conjunto ≠ notación
  RA6  asignación estructural ≠ pertenencia al cuerpo
  RA7  solo lo que M declara · sin verificación externa

Asignaciones múltiples registradas: 5
  D-Cα-127 → E2 (referencia correctiva)
  M1γ / D-γ → E1 (una entrada · dos notaciones)
  DC-*      → E5 + E6
  A*        → E3 + E6
  E*        → E4 + E6

NO-ASIGNADOS estrictos: vacío
Observaciones meta fuera de estratos: 5 (nota al margen · no objetos)

─────────────────────────────────────────────────────────────

§2.3 · v0.3.1 · DETERMINACIÓN DE VIGENTE

Método
  Registro del estado que M declara · sin inferir.

Cuerpo SCFV-DSR: 350

Desglose:
  293 con estado declarado y determinación ordinaria
   22 D-B en doble columna C-1/C-2 (CONFIRMADA declarada)
   35 NO-DETERMINADOS (M1α-δ + DM · M §7 no asigna estado)

Externo:
  D-CONV-15 · separado del cómputo del cuerpo

Reglas RD1–RD7 aplicadas · verificación aritmética obligatoria

─────────────────────────────────────────────────────────────

§2.4 · v0.4.2 · RESOLUCIÓN · RÉGIMEN R-B

Hallazgo estructural
  M declara ESTADOS · no CONDICIONES DE CIERRE.

Regímenes posibles:
  R-a  M-estricto · solo lo que M declara
  R-b  M + fuentes trazables (adoptado por el Operador)

Bajo R-a (referencia):
  Partición: 350 = 3 retiradas + 347 bloqueadas
  Resolubles estrictos: 0

Bajo R-b (adoptado):
  Lista cerrada de 13 archivos
  RT1–RT4 · regla de traducción
  CC1–CC3-bis · criterio de cierre

─────────────────────────────────────────────────────────────

§2.5 · v0.5.1 · RESULTADO LOCAL RESOLUCIÓN

Pilotos ejecutados:
  D-IMP (2 deudas) · verificado contra contrato + código + tests
  M1β   (8 deudas) · verificado solo contra acta
  M1α   (5 deudas) · idem
  M1δ   (9 deudas) · idem

Objetos examinados: 24
Cierres:             0 bajo CC1–CC3-bis

Hipótesis §4 (sostenida en 3–4 casos · no universalizada)
  Las fuentes del corpus examinado declaran deudas sin proporcionar
  evidencia material de reparación.

F-T · dos tipos de deuda
  Tipo A  el código hace algo a corregir
  Tipo B  falta algo en el corpus

F-R/F-U
  Los tests verdes NO equivalen a cierre de deudas

─────────────────────────────────────────────────────────────

§2.6 · v1.0 · LISTA DE CIERRE CONSOLIDADA

CERRADA VERIFICADA (1)
  D-C-26
    Material: commit abb2bac · event_store.py +39 L
    Verificación: AUDITORIA_26-09 Hallazgo 1 · "resuelto en FASE 1"

CERRADA DOCUMENTAL (1)
  D-BB-58
    Fuente: C-β acta §7 · "cerrada · caracterizados"

RETIRADA (3)
  D-C-9   · artefacto de transcripción
  D-C-22  · PersistenciaViolacion existe en serializador_canonico.py
  D-Cα-100 · ACTA_ACTIVACION_HEVNER distingue con precisión

CANDIDATA (3)
  D-CONV-4 · FASE 4 §1 C-4 · "push ya hecho · Everything up-to-date"
  D-Cα-69  · misma deuda que D-CONV-4
  D-BB-57  · H-BB3-19 · "paradoja del acta resuelta" · release 26-09

ABIERTA / REQUIERE MATERIAL (~330 · discrepancia declarada · ver §5)
  Por familia (aproximado):
    D-BB   72
    D-C    84
    D-Cα  125
    D-B    26
    D-IMP   2
    M1α     5
    M1β     8
    M1γ     7
    M1δ     9
    DM      6

SIN ESTADO (~30)
  D-BB-15 · D-BB-14 · D-BB-19 · D-C-25 · D-C-30
  D-C-43 · D-IMP-01 · D-IMP-02 · D-M1α-3/4/5
  D-EPIST-1..7 · DESC-01 · H-PER-CONF
  Ops inertes (3) · 12 items §15 B-bis
  Hallazgos 4-7 AUDITORIA_26-09

Regla de frontera
  CANDIDATA = soporte externo identificable · falta acto del Operador
  NO se eleva a CANDIDATA una anotación ambigua

═══════════════════════════════════════════════════════════════
§3 · FALSACIONES REGISTRADAS (ÍNDICE)
═══════════════════════════════════════════════════════════════

Notación: F-N · contenido · veredicto

RETIRADAS (por error propio de IA-2)
  F1    M1γ sin locus            → retirada (grep único)
  F4    espantapájaros IA-1      → retirada (sin verificar)
  F11   M no cierra suma global  → retirada (M sí cierra 350)
  F-A   C-β §6 no resuelve       → retirada (headers vs contenido)
  F-AO  anomalía aritmética D-Cα → retirada (paste parcial)

SOSTENIDAS (principales)
  F5    M es nodo · no raíz
  F8    Naming collision M1γ
  F9    M porta 13 errores propios (E1–E13)
  F12   V10 · V12 ausentes en repo
  F14   bloque_B_estatico fuera de §0
  F17   D-CONV-4 doble estado · DC-8 existe
  F18   E11 coexistencia ≠ sucesión
  F20   Refundacional §10 sin locus en M
  F21   M §0 subdeclara DC (1 vs ≥3)
  F22   DM-3 describe esta sesión
  F23   O1..O43 sin índice
  F24   DM-5/DM-6 no resueltas
  F25   D-Cα-128/129 sin locus
  F26   D-Cα-100 doble fila
  F-H   deuda sin trazabilidad M
  F-Z   reparación sin deuda en M
  F-AB  familia D-EPIST-1..7 fuera de M
  F-X   git única capa con reparaciones materiales
  F-AH  sesión reproduce patrón que M ya había advertido

DISTINCIONES DERIVADAS
  CANDIDATA ≠ SIN ESTADO
  CERRADA DOCUMENTAL ≠ CERRADA VERIFICADA
  RETIRADA ≠ CERRADA
  registrado ≠ verificado ≠ convalidado ≠ materializado

═══════════════════════════════════════════════════════════════
§4 · REGLAS VIGENTES
═══════════════════════════════════════════════════════════════

CC1  Una deuda no se cierra por declaración documental
CC2  Cierre requiere: ID único + evidencia material de reparación
     + verificación independiente
CC3  La evidencia debe citar material (diff · commit · test)
CC3-bis  Independencia funcional · no meramente documental
CC4  Sin material ni declaración → bloqueada por material

RT1  Precedencia consolidatoria de M · no autoridad ontológica
RT2  Fuente puede aportar dato faltante (marcado ORIGEN-FUENTE)
RT3  Discrepancias entre M y fuente → observación meta
RT4  Cita como archivo:sección o archivo:línea

═══════════════════════════════════════════════════════════════
§5 · DISCREPANCIA ~330 / ~344
═══════════════════════════════════════════════════════════════

§5 y §7 declaran ~330 abiertas.
La suma por familia en §6 da 344.

Diferencia: ~14.

NO se corrige por inferencia.
Causa probable (no verificada): solapamientos entre familias
que §5 no resta.

Se traslada a Fase B como asunto explícito de reconciliación.

═══════════════════════════════════════════════════════════════
§6 · RIESGO OPERATIVO
═══════════════════════════════════════════════════════════════

Patrón observado en IA-2
  Cinco veces publicó un resultado antes de verificar.
  Cinco veces lo retiró.

Casos:
  F1       grep único sin codificación alternativa
  F4       acusación sin verificar afirmación previa
  F-A      grep de headers sin verificar contenido
  F-AO     paste parcial
  F-BB-14  diff parcial

Advertencia metodológica para Fase B
  Conclusión no verificada NO adquiere estatuto de hecho
  por haber aparecido en un grep, un paste parcial o una
  lectura incompleta.

Se traslada como RIESGO OPERATIVO · no como regla formal.

═══════════════════════════════════════════════════════════════
§7 · PENDIENTES PARA FASE B
═══════════════════════════════════════════════════════════════

1. Reconciliación ~330 / ~344
2. Política P1/P2/P3 sobre "resueltas" del acta C-β
3. D-BB-14 · D-C-50 · dos loci para el mismo bug (MotorContable(None))
4. D-EPIST-1..7 · familia fuera de M
5. F-H · DESC-01 · H-PER-CONF · sin trazabilidad M
6. F-Z · ops inertes · reparación sin deuda en M
7. F-AB · familia D-EPIST fuera de M
8. F-AD · 4 correcciones retroactivas Ventana 7
9. DC-9 · DC-14 · deudas meta declaradas por git no registradas en M §0
10. Confirmar estatuto de H8P_IMPORTADOR_CONTRATO.md (§22.4) como
    fuente incorporada a la frontera permanente

═══════════════════════════════════════════════════════════════
§8 · CIERRE DE VENTANA
═══════════════════════════════════════════════════════════════

Estado al cierre:
  A2 real              CERRADO
  T13                  CERRADO
  Lista v1.0           CONSOLIDADA · congelada
  Discrepancia         ~330 / ~344 · PENDIENTE
  CANDIDATAS           3 · no convalidadas
  SIN ESTADO           preservado como déficit de determinación
  Materialización      STOP
  Fase B               nueva ventana

Insumos congelados transferidos:
  · Lista de Cierre v1.0 (6 estatutos)
  · Documentos de trabajo v0.1.3 → v1.0
  · Falsaciones F1–FZ (índice · ver §3)
  · Reglas CC1–CC3-bis · RT1–RT4
  · Frontera de 13 archivos + H8P §22.4 + código/tests D-IMP
  · Riesgo operativo (cinco retiradas del mismo patrón)
  · Pendientes enumerados (§7)

═══════════════════════════════════════════════════════════════
FIN DEL CONSOLIDADO
═══════════════════════════════════════════════════════════════
