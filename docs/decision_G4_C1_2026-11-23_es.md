# Entrada del libro de decisiones — el criterio C1 se decide solo con la caída del AUROC (23/11/2026)

Versión en inglés: [`decision_G4_C1_2026-11-23.md`](decision_G4_C1_2026-11-23.md).

**Etapa / puerta:** P4, criterio C1. **Tipo de razón:** metodológica (dependencia del AUPRC frente a la prevalencia).
**Validada por:** Emmanuel Gutiérrez Jiménez (por confirmar con el director de la tesis). **Registrada después** de correr el notebook 05 de este modelo: el cambio surgió de su resultado.

## Contexto

Antes de esta decisión, C1 exigía dos cosas en la población *landmark*: una caída del AUROC de 0,05 o menos **y** conservar al menos dos tercios de la ganancia del AUPRC sobre la prevalencia. En el modelo neonatal (M4), el 55% de las muertes (34.466 de 62.713) ocurre en los días 0 y 1. En el punto de referencia a las 48 horas (decisión M4-D1) el AUROC baja de 0,964 a 0,932 (caída 0,032; IC 95% 0,031–0,033), dentro del límite, pero solo se conserva el 26% (25–27%) de la ganancia del AUPRC. El AUPRC, y por tanto su ganancia sobre la prevalencia, depende de la prevalencia, que cae a menos de la mitad al retirar las muertes de los dos primeros días. La segunda condición penaliza así un desenlace con muchos eventos tempranos aunque el ordenamiento de la población restante siga siendo bueno, que es lo que mide la caída del AUROC.

## Regla (desde el 23/11/2026)

1. **C1 se decide con la caída del AUROC en la población *landmark*: 0,05 o menos.** La proporción conservada de la ganancia del AUPRC se sigue calculando y reportando con su intervalo del 95%, pero no decide.
2. El resto de la puerta P4 y los umbrales de los demás criterios no cambian.

## Efecto sobre los demás modelos del catálogo

Ninguno. No cambia la clasificación de ningún otro modelo:

| Modelo | Caída del AUROC en el *landmark* | Ganancia del AUPRC conservada | C1 con la regla anterior | C1 con esta regla |
|---|---|---|---|---|
| M2, modelo principal (MIMIC-IV, artículo de Cureus) | 0,072 (0,056–0,088) | 40% | no cumple | no cumple |
| M2, retorno R4 | 0,081 (0,066–0,098) | 29% | no cumple | no cumple |
| M2, retorno R2 (escalamiento) | −0,003 | 118% | cumple | cumple |
| M2, retorno R2 reducido | −0,004 | 116% | cumple | cumple |
| M5 y M6 (predicción prenatal) | — | — | cumple por diseño | cumple por diseño |

Los resultados y clasificaciones del artículo de Cureus quedan iguales; el artículo describe C1 con la regla anterior.

## Resultado para M4

Notebook 05 (`data/outputs_05_main_evaluation.txt`, puerta P4): C1 cumple (caída 0,032), C2 cumple, C3 no aplica, C4 cumple. AUROC en el *landmark* 0,932 (≥ 0,75). **Clasificación: predictor.** Con la regla anterior C1 no habría cumplido (26% de la ganancia del AUPRC conservada) y el modelo habría sido identificador temprano; esta entrada es el único lugar donde eso queda registrado.
