# Clase · Introducción a Python para analítica industrial

**1682913 · Analítica de Datos · Nivel inicial · 12 horas sugeridas**

[![Abrir en Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/karendayana2590-bot/1682913-ANAL-TICA-DE-DATOS/blob/main/clases/introduccion-python/Introduccion_Python_Analitica_Industrial.ipynb)

## Comienza aquí
1. Abre el notebook en Colab con el botón anterior y guarda una copia, o descarga esta carpeta y ábrelo en Jupyter.
2. Ejecuta las celdas en orden. Lee, predice, modifica y explica los resultados.
3. Resuelve los ocho retos antes de desplegar las soluciones.
4. Prueba el simulador y termina el proyecto del comité de producción.

GitHub muestra el contenido; la ejecución del código y los controles ocurre en Colab o Jupyter.

## Materiales
- [Notebook de la clase](Introduccion_Python_Analitica_Industrial.ipynb): 68 celdas, explicaciones, ejercicios, soluciones y simulador.
- [Clase completa para lectura](CLASE_COMPLETA.md): todo el contenido en una página.
- [Guía docente](GUIA_DOCENTE.md): secuencia, dinámicas, respuestas y criterios de revisión.
- [Datos de producción](produccion.csv): doce registros sintéticos con dos líneas y seis días.
- [Programa de análisis](analizar_produccion.py): valida datos, calcula indicadores y exporta resultados.
- [Dependencias](requirements.txt).

## Temas cubiertos
Python; Jupyter Notebook/JupyterLab; Google Colab; celdas y kernel; variables; tipos; conversiones; operadores; listas, tuplas, diccionarios y conjuntos; condicionales; ciclos; funciones; validación y errores; librerías; NumPy; pandas; CSV; limpieza; filtros; agrupaciones; uniones; gráficos; producción, calidad, cumplimiento y productividad; simulación; interpretación y comunicación.

## Ejecución local
Desde esta carpeta y dentro de tu entorno de Python:
```text
python -m pip install -r requirements.txt
python -m jupyterlab
```
Para ejecutar solamente el programa industrial:
```text
python analizar_produccion.py
```
También admite una ruta: `python analizar_produccion.py otro_archivo.csv`. El archivo debe respetar el diccionario y el catálogo A/B del ejemplo. Los CSV resultantes se guardan en `resultados/` dentro de la carpeta de ejecución. Las instrucciones de instalación y activación completas están en el notebook.

Los datos son educativos y los umbrales de calidad son supuestos de práctica. La clase incluye rúbrica de 100 puntos, doce preguntas de autoevaluación y un reto final en equipo.
