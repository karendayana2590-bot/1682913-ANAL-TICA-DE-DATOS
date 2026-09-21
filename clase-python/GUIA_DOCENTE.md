# Guía docente · Introducción a Python y analítica industrial

## Preparación
La secuencia está diseñada para principiantes en tres encuentros de cuatro horas. No se recomienda comprimir todos los ejercicios en una sola sesión corta. La agenda detallada está al inicio del notebook. Disponga parejas con un computador; reserve un equipo con el notebook y los paquetes instalados para contingencias de conexión.

Antes de clase, abra el notebook en el entorno que usará el grupo, pruebe una celda y los controles del simulador. En Colab guarde una copia; en Jupyter confirme que el kernel tiene NumPy, pandas y Matplotlib. Los controles son opcionales: si ipywidgets no está disponible, se puede modificar y ejecutar `simular(...)`.

## Dinámica transversal
1. Proyecte la pregunta de cada bloque antes del código.
2. Pida una predicción individual y luego consenso en pareja.
3. Ejecute el ejemplo; solicite explicar la salida con unidades.
4. Cambie un dato y pida anticipar la consecuencia.
5. Resuelva el reto sin abrir la solución desplegable hasta terminar el intento.

Cambie los roles de quien programa y quien revisa después de cada reto. La persona revisora debe señalar una suposición o una validación, no limitarse a observar.

## Sesión 1 · Entorno y lógica
**Apertura:** compare «1000 unidades» con «100 unidades/hora». Pregunte qué información falta para evaluar desempeño.

**Entornos:** cada estudiante crea texto y código, guarda, reinicia y ejecuta nuevamente. Muestre un NameError al ejecutar una celda dependiente antes de definir la variable, y recupere el flujo ejecutando en orden.

**Variables y colecciones:** use tarjetas de producción, rechazo, horas y personas. Pida clasificar tipo y unidad antes de programar. Contraste texto numérico con número.

**Condicionales:** haga que el grupo represente las fronteras 95 y 98. Pregunte a qué rama pertenece exactamente cada frontera.

**Ciclos:** represente cinco turnos con cinco estudiantes. Cada uno entrega un dato al acumulador. Diferencie cantidad de registros de suma de unidades.

**Salida:** una variable, una condición y un ciclo explicados con palabras propias. Si más de un tercio del grupo confunde asignación y comparación, retome el ejemplo antes de la siguiente sesión.

## Sesión 2 · Funciones, NumPy y pandas
**Repaso:** reconstruya la fórmula de calidad sin mostrar código.

**Funciones:** compare imprimir un resultado con devolverlo para calcular otro indicador. Pruebe el caso cero producción y el caso horas cero. Explique por qué uno permite un resultado parcial y el otro se rechaza.

**Errores:** entregue tres fallos deliberados: nombre incorrecto, texto en una suma y división por cero. El estudiante debe identificar tipo, causa y corrección; no basta con copiar la solución.

**NumPy:** compare lista y arreglo multiplicados por dos. Dibuje una matriz días × líneas y señale la dirección de cada reducción por eje.

**pandas:** solicite seleccionar, filtrar y agrupar la tabla pequeña. Demuestre que una unión con claves repetidas puede duplicar observaciones.

**Salida:** cada pareja formula una pregunta que pueda responder con un filtro y otra que requiera agrupación.

## Sesión 3 · Decisiones industriales
**Contrato de datos:** lea el diccionario y acuerde qué significa defectuosa y hora-persona. Aclare que se compara el mismo producto y que los datos son sintéticos.

**Detectives:** cambie un dato por equipo: negativo, ausente, duplicado, infinito o defecto mayor que producción. Deben explicar por qué la validación lo rechaza y cómo consultarían la fuente.

**Indicadores:** pida calcular manualmente la primera fila: 980 buenas, 98 % calidad, 100 % cumplimiento y 30.625 buenas/hora-persona. Contraste con Python.

**Simulador:** pruebe los cuatro escenarios del notebook. Pregunte por qué una mejora aritmética de productividad al reducir personas no basta para recomendar esa medida.

**Comité:** distribuya roles de análisis, operaciones y auditoría. Cada equipo defiende una recomendación; otro equipo señala un supuesto que debería verificarse. Use la rúbrica del notebook.

## Resultados de referencia del conjunto original
| Medida | Línea A | Línea B |
|---|---:|---:|
| Producción | 6230 | 5710 |
| Defectuosas | 186 | 203 |
| Buenas | 6044 | 5507 |
| Horas-persona | 192 | 144 |
| Calidad | 97.01 % | 96.44 % |
| Cumplimiento | 103.83 % | 100.18 % |
| Productividad (buenas/hora-persona) | 31.48 | 38.24 |

Global: 11940 producidas, 389 defectuosas, 11551 buenas, 96.74 % de calidad y 34.38 buenas/hora-persona. A lidera producción y calidad; B lidera productividad laboral. No hay evidencia para atribuir causalidad a dotación, operadores o máquinas.

## Apoyos y profundización
- Si alguien se atasca: reduzca el problema a una fila, escriba la fórmula en papel y nombre cada unidad.
- Si termina pronto: solicite días adicionales, análisis de sensibilidad y pruebas de datos inválidos.
- Sin conexión: use Jupyter ya instalado; el notebook contiene sus datos.
- Sin controles gráficos: modifique los argumentos de `simular` y ejecute la celda.
- Para accesibilidad: lea los estados de calidad por nombre; no dependa solo del color, y permita explicaciones orales junto con el código.

## Lista de revisión de entrega
- Notebook ejecutable desde cero y con interpretación en texto.
- Fórmulas con unidades y denominadores definidos.
- Datos inválidos detectados, sin correcciones inventadas.
- Totales y razones globales coherentes.
- Archivos de salida y gráfico legible.
- Recomendación vinculada con evidencia y una limitación explícita.
