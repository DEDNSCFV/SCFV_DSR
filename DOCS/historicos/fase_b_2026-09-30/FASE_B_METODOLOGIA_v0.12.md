═══════════════════════════════════════════════════════════════════
FASE B · METODOLOGÍA v0.12
═══════════════════════════════════════════════════════════════════

ESTATUTO:   documento metodológico de Fase B
            NO es acta de cierre · NO es v1.0
            NO cierra deudas · NO autoriza intervención
            NO modifica SCFV_DSR · NO modifica M · NO firma §20

FECHA:      2026-09-30
VENTANA:    B
ORIGEN:     traspaso VENTANA_2026-09-30_CONSOLIDADO (A→B)
FALSACIÓN:  3 rondas IA-2 · PASS
BLOQUES:    B1–B13 · B11.V

NOTA DE ESTATUTO POR SECCIÓN
  [DATO]      verificable contra fuente primaria
  [DATO-2]    verificable contra fuente secundaria · declarado
  [DECISIÓN]  asignación de ventana · no verificable
  [PEND]      declarado como hueco

═══════════════════════════════════════════════════════════════════
TOMO I · DATO
═══════════════════════════════════════════════════════════════════

§D1 · METADATOS

  Ventana:                 B
  Fecha:                   2026-09-30
  Origen:                  A→B · VENTANA_2026-09-30_CONSOLIDADO
  Falsación:               3 rondas IA-2
  Bloques ejecutados:      B1–B13 · B11.V
  Estado:                  congelado · apto para materializar

§D2 · INSUMOS RECIBIDOS

  [DATO-2] Archivos fuente leídos durante B · verificable por ls.

  I1   VENTANA_2026-09-30_CONSOLIDADO.md
  I2   bloque_M_deudas_catalogo_consolidado.md
  I3   bloque_B_estatico.md
  I4   bloque_Bbis_{deudas,acta,hallazgos,falsacion_matriz,traspaso_correcciones}.md
  I5   bloque_C_beta_{deudas,acta,hallazgos,correcciones,coherencia}.md
  I6   bloque_C_alpha_{deudas,acta,hallazgos,correcciones,referencias_cruzadas,matriz_21_canones}.md
  I7   bloque_M1_{alpha,beta,gamma,delta}_*.md
  I8   bloque_C_gamma_sintesis_metodologica.md · bloque_V11_cierre_traspaso.md
  I9   arqueologia_B{1,2}_inventario.md
  I10  AUDITORIA_2026-09-26.md
  I11  INFORME_FASE_4_RECONOCIMIENTO_2026-09-28.md
  I12  H8P_IMPORTADOR_CONTRATO.md §22.4
  I13  git log scfv-dsr
  I14  ~/Programa-de-Investigacion-SCFV/ACTAS/ (listado · acceso parcial)

  No recibidos:
  N1   Lista de Cierre v1.0 §5 y §7
  N2   FASE 4 (documento citado por arqueologia_B2)
  N3   Traspaso Ventana 7 (citado por INFORME_FASE_4)
  N4   scfv_v6/DOCS completo

§D3 · REGLAS DE VENTANA RB-0..RB-9

  RB-0   Ninguna conclusión se publica sin verificación previa contra
         locus. Cinco retiradas del mismo patrón obligan a parar.

  RB-1   Una deuda no se asigna a repositorio por mención del nombre.
         Requiere locus material o relación documental explícita.

  RB-2   Duplicado cuenta una vez · segundo ID queda como marca cruzada.

  RB-3   Duplicado solo si comparten archivo:línea o módulo:objeto.

  RB-4   Duplicación intra-M solo si (a) locus idéntico o (b) fuente
         primaria declara "mismo objeto".

  RB-5   Estado asignado por B solo si M o fuente primaria lo declara.

  RB-6   Ninguna cifra se emite desde narración. Toda cifra desde
         comando. Todo residuo se declara antes de cerrar.

  RB-7   En casos mixtos (código + doctrina), C-INTERV toma TEC como
         categoría primaria. Estatuto: regla de ventana · no ontológica.

  RB-8   Una D-META cerrada no entra en el universo de intervención.

  RB-9   C-INTERV activo ≠ 350 categorizadas. C-INTERV activo = TEC
         + DOC · sin cierres históricos · sin decisiones pendientes
         · sin discrepancias.

  RB-0..RB-9 son reglas de ventana. No modifican M. No modifican
  CC1–CC3-bis ni RT1–RT4.

§D4 · SUBSTRATO · CIFRAS DE M

  [DATO-2] Cifras de M §10 · no verificadas por grep individual:

    D-B 26 · D-BB 73 · D-IMP 2 · D-C 88 · D-Cα 126 · M1 29 · DM 6
    ──────────────────────────────────────────────────────────────
    350

  [DATO] Verificaciones por grep · familia por familia:

    bloque_Bbis_deudas.md       75 filas (73 D-BB + 2 D-IMP)   OK
    bloque_C_beta_deudas.md     88 filas                        OK
    bloque_C_alpha_deudas.md   127 filas (126 + 1 doble)        OK
    bloque_M1_alpha              5 filas                        OK
    bloque_M1_beta               8 filas                        OK
    bloque_M1_gamma              0 filas (prefijo D-gamma-X-N)  --
    bloque_M1_delta              9 filas                        OK
    bloque_B_estatico            0 filas (sin tabla "| ID |")   --

  [PEND] 350 no se reconstruye por grep. Depende de M §2 y §5.

  [DATO] Partición M §10:
    341 pendientes + 5 reformuladas + 3 retiradas + 1 cerrada doc = 350

  [DATO] Retiradas · confirmadas en fuente primaria:
    D-C-9     bloque_C_beta_deudas.md:164
    D-C-22    bloque_C_beta_deudas.md:165
    D-Calpha-100  bloque_C_alpha_deudas.md:163

  [PEND] Reformuladas · tres cifras distintas coexisten:
    M §10        5   (4 D-B-16..19 + 1 D-BB-19)
    C-beta corr:397 3   (D-B-16..19 + MotorContable(None) + D-BB-19)
    C-alpha corr:263 7  (H-BB3-16/17 · régimen · Patrón E · nombres
                         · taxonomía · D-CONV-11)
    M prevalece bajo RT1 → 5. Reconciliación pendiente.

  [PEND] CERRADA VERIFICADA · triple estatuto:
    [M]      M no declara CERRADA VERIFICADA. Bajo RT1 · D-C-26 ABIERTA.
    [FUENTE] AUDITORIA_2026-09-26.md · Hallazgo 1 · commit abb2bac.
    [B]      B no decide aún qué estatuto dar a D-C-26 en el cómputo.

  [DATO] Duplicados por locus (RB-3 + RB-4):
    D-B-4   = D-C-54    evaluador.py:89 · evaluar_operacion
    D-BB-14 = D-C-50    orquestador.py:118 · MotorContable(None)

  [PEND] Duplicado cross-cuerpo:
    D-Calpha-69 <-> D-CONV-4 · hipótesis de correspondencia · no verificado
    D-CONV-4 está en anexo §11 · fuera del cuerpo 350.

§D5 · DISTRIBUCIÓN REPO/CAPA

  Leyenda obligatoria:
    Las columnas Alta · R1–R6 · META · MIX · ?a · ?r son dimensiones
    de clasificación, NO categorías mutuamente excluyentes.
    La suma horizontal no particiona el cuerpo.
    La única columna cuya suma totaliza 350 es "Total".

  Convenciones:
    R1  scfv_v6
    R2  SCFV_S0_V1.0.0
    R3  scfv-dsr
    R4  Programa-de-Investigacion-SCFV
    R5  scfv_github
    R6  corpus/documentos externos
    META  sin repo material (meta-proceso)
    MIX   dos repos simultáneos declarados
    ?a    activa sin repo/locus clasificado
    ?r    retirada fuera de clasificación por repo

  Familia     Total  Alta   R1  R2   R3  R4  R5  R6  META  MIX  ?a  ?r
  M1+IMP+DM     37    37   31   0    0   0   0   0     6    0   0   0
  D-B           26    26    2   0   19   0   0   0     0    5   0   0
  D-BB          73    49   22   0    3  16   0   1     3    4  24   0
  D-C           88    88    0   0   84   0   0   0     0    1   1   2
  D-Calpha     126    78    1   1   42  29   2   0     0    4  47   0
  ─────────────────────────────────────────────────────────────────────
  Total        350   278   56   1  148  45   2   1     9   14  72   2

  [PEND] Residuo aritmético: 348 vs 349 vs 350 declarado. No cerrado.

  [PEND] 348 no es cifra operativa hasta cerrar matriz de duplicaciones
  (RB-4). Fue cálculo provisional sobre 2 duplicaciones confirmadas.

§D6 · RETIRADAS RB-0

  [DATO] Siete retiradas propias de B:
    F-B9-1   F-AD = §7.3 CONV              retirada
    F-B9-2   INFORME_FASE_4 cita bien      retirada
    F-B9-3   F-AD = §7.3 G05               retirada
    F-B10-1  D-C-13 duplicado              retirada (RB-4)
    F-B10-2  D-C-32 reformulada            retirada (RB-5)
    F-B10-3  D-C 84 contables              retirada (RB-6)
    F-B11-1  D-META-9 = hipótesis          retirada (v0.11)

  Patrón F-AH confirmado: las retiradas de B reproducen el vicio que
  A ya había advertido (publicar antes de verificar).

  Las retiradas afectan afirmaciones/lecturas producidas durante B.
  NO son retiradas de deudas del catálogo M. NO modifican M.


═══════════════════════════════════════════════════════════════════
TOMO II · DECISIÓN
═══════════════════════════════════════════════════════════════════

§X1 · CRITERIO C-INTERV PUBLICADO

  [DECISIÓN] Criterio de asignación TEC/DOC/NO-INT/META/DISCREP:

    C-INTERV-TEC
      La reparación requiere modificar código, tests, o configuración
      ejecutable. La fuente del defecto está en un archivo material
      del corpus (no en un documento).

    C-INTERV-DOC
      La reparación requiere modificar un documento normativo o
      declarativo (M · ADR · README · acta). La fuente del defecto
      está en prosa, no en código.

    NO-INTERV
      Solo cuando el estatuto de no intervención está respaldado por:
        (a) M declara explícitamente CERRADA · RETIRADA · o equivalente, o
        (b) decisión documental previa con autoridad reconocida en la
            ventana (acta con autoridad, ADR, protocolo).
      NO se admite "no es deuda del corpus" como vía de salida.
      Si una entrada no parece deuda, se registra como META-RECON o
      DISCREP-ABIERTA, no como NO-INTERV.

    META-{POL,ESTAT,RECON}
      Requiere decisión posterior:
        META-POL     política del Operador
        META-ESTAT   estatuto de fuente
        META-RECON   reconciliación entre fuentes

    DISCREP-ABIERTA
      Discrepancia entre fuentes · dato no reconciliable sin fuente
      no disponible.

  [DECISIÓN] RB-7 · Límite del criterio:
    En casos mixtos (defecto en código + doctrina), prevalece TEC.
    Estatuto: regla de ventana B · no ontológica.
    No implica que el defecto doctrinal desaparezca.

§X2 · ASIGNACIÓN C-INTERV

  [DECISIÓN] Esta sección es asignación de B, no dato.

  Distribución revisada (post-falsación v0.11):

    Familia     IDs    TEC   DOC   NO-INT   META   DISCREP
    M1+IMP+DM    37     20     6      1       9        1
    D-B          26     20     0      2       4        0
    D-BB         73     13    35      1      19        5
    D-C          88     69     5      0       3        2
    D-Calpha    126      8    91      1      19        5
    ─────────────────────────────────────────────────────
                350    130   137      5      54       13

    Fuera de C-INTERV:
      CERRADA DOC.     1
      RETIRADA         3
      REFORMULADA      5
      DUPLICADA        2
      ─────────────────
                     350

  [DECISIÓN] Aviso obligatorio:
    La suma de categorías de B reproduce 350 únicamente porque la
    asignación fue construida sobre el universo nominal declarado
    por M. No constituye verificación independiente.
    No debe invocarse como prueba de integridad del documento.

  [DECISIÓN] D-C-21 · reasignada a C-INTERV-TEC (antes NO-INTERV).
    M la declara ABIERTA · RT1 prevalece.

§X3 · META-PEND DESDOBLADO

  [DECISIÓN] META-PEND deja de ser categoría única:
    META-POL     requiere política del Operador         (~12)
    META-ESTAT   requiere decidir estatuto de fuente    (~8)
    META-RECON   requiere reconciliación entre fuentes  (~34)

  Cambio de granularidad · no de cifra.

§X4 · DEUDAS META · TRES ESTATUTOS

  [DECISIÓN]

    [HISTÓRICAS]  producidas durante B
                  D-META-1 .. D-META-11     = 11

    [CERRADAS]    resueltas documentalmente durante B
                  D-META-9 (B9)             =  1

    [ACTIVAS]     requieren acción posterior
                  D-META-1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 10 · 11
                  = 10

  Listado activas:

    D-META-1    ~330 vs 348 · requiere Lista de Cierre v1.0    META-RECON
    D-META-2    "resuelta" C-beta §0 sin estatuto              META-ESTAT
    D-META-3    H8P §22.4 · 5 deudas · M registra 2            META-ESTAT
    D-META-4    D-BB-14 = D-C-50 · deduplicación               META-POL
    D-META-5    D-EPIST-1..7 · FASE 4 ausente                  META-RECON
    D-META-6    "SIN ESTADO" no existe en M                    META-RECON
    D-META-7    FASE 2.a.1/2.a.2 · reparaciones sin deuda      META-POL
    D-META-8    M §0 subdeclara DC (1 vs 5)                    META-RECON
    D-META-10   CERRADA VERIFICADA del consolidado             META-ESTAT
    D-META-11   reformuladas 3/5/7 · tres cifras coexisten     META-RECON

  D-META-9 · cerrada en B9:
    F-AD = INFORME_FASE_4 §1 · C-1..C-4.
    · C-1 (cadena inferida)      · no está en M
    · C-2 (perceptum huérfano)   · no está en M
    · C-3 (7 archivos ep.)       · no está en M
    · C-4 (push ya hecho)        · = D-CONV-4
    Locus verificado en INFORME_FASE_4_RECONOCIMIENTO_2026-09-28.md §1.
    Cerrada. No pertenece al universo META activo.

§X5 · RB vs M · ZONA GRIS DECLARADA

  [DECISIÓN] Declarado · no resuelto:

    RB-0..RB-9 son reglas de ventana B.
    No modifican M en sentido formal.
    Alteran la lectura derivada de M (duplicados, cierre, etc.).
    La distinción es semántica, no material.

    Decisión del Operador pendiente:
      (a) Aceptar la distinción formal · RB no modifica M.
      (b) Declarar que RB modifica el cómputo autorizado de M.
      (c) Abrir deuda meta específica.

═══════════════════════════════════════════════════════════════════
TOMO III · FALSACIÓN
═══════════════════════════════════════════════════════════════════

§F1 · AFIRMACIONES FALSABLES

  FD1 · 350 depende de M §2, no de grep             [DATO-2 · declarado]
  FD2 · 348 es cálculo provisional de B, no cifra
        de M · pendiente matriz duplicaciones        [PEND]
  FD3 · CERRADA VERIFICADA · triple estatuto
        declarado · no resuelto                      [PEND]
  FD4 · Reformuladas 3/5/7 · M prevalece            [PEND]
  FD5 · D-Calpha-69 <-> D-CONV-4 · hipótesis
        de correspondencia · no equivalencia         [PEND]
  FD6 · C-INTERV criterio publicado en §X1          [DECISIÓN]
  FD7 · META-PEND desdoblado en §X3                 [DECISIÓN]
  FD8 · F-AD = INFORME_FASE_4 §1 · resultado B9     [DATO]
  FD9 · NO-INTERV revisado · D-C-21 vuelve a TEC    [DECISIÓN]
  FD10· D-C · 1 activa ?a + 2 retiradas ?r          [PEND]
  FD11· RB vs M · zona gris declarada               [PEND]
  FD12· 72 ?a · 24 D-BB + 47 D-Calpha + 1 D-C       [PEND]

§F2 · LO QUE v0.12 NO AFIRMA

  · No afirma que 350 sea cifra verificada ID x ID.
  · No afirma que CERRADA VERIFICADA = 0 sea estatuto final.
  · No afirma que reformuladas = 5 sin reservas.
  · No afirma que F-AD = INFORME_FASE_4 §1 sin reserva
    (B9 sí lo estableció · v0.12 lo restaura).
  · No afirma que C-INTERV cierre por construcción.
  · No afirma que RB no modifiquen M (zona gris declarada).
  · No afirma que 348 sea cifra oficial del cuerpo.
  · No afirma que NO-INTERV sean las únicas no-deudas.

═══════════════════════════════════════════════════════════════════
TOMO IV · PENDIENTES
═══════════════════════════════════════════════════════════════════

§P1 · ANTES DE MATERIALIZAR v1.0

  1. Resolver FD1 · 350 ID x ID
  2. Resolver FD3 · CERRADA VERIFICADA
  3. Resolver FD4 · reformuladas 3/5/7
  4. Resolver FD5 · D-Calpha-69 <-> D-CONV-4
  5. Decidir FD11 · RB vs M
  6. Resolver FD10 · D-C residuo
  7. Cerrar matriz de duplicaciones
  8. Decidir criterio D-Calpha doctrinal (47 sin clasificar)
  9. Decidir MIX (14 casos)

§P2 · LO QUE v0.12 ENTREGA

  [Hecho verificado]        §D5 · distribución repo/capa
  [Hecho verificado]        §D6 · retiradas RB-0
  [Criterio publicado]      §X1 · TEC/DOC/NO-INT/META/DISCREP
  [Reasignación revisada]   §X2 · D-C-21 a TEC · RT1 respetado
  [Desdoblamiento]          §X3 · META-PEND -> POL/ESTAT/RECON
  [Deudas meta]             §X4 · 11 históricas · 1 cerrada · 10 activas
  [Zona gris declarada]     §X5 · RB vs M
  [Todos los residuos]      declarados · no ocultos

§P3 · ESTATUTO DE v0.12

  v0.12 es un borrador metodológico honesto.
  No pretende ser completo.
  No pretende que sus cifras sean definitivas.

  Declara:
    · qué es dato
    · qué es decisión
    · qué es fuente secundaria
    · qué queda pendiente

  Pasa a fase de verificaciones primarias.
  No pasa a v1.0.
  No cierra Fase B.

═══════════════════════════════════════════════════════════════════
FIN DE FASE_B_METODOLOGIA_v0.12
═══════════════════════════════════════════════════════════════════
