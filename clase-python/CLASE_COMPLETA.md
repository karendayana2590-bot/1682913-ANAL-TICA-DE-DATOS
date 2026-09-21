# Python para analizar datos de producción
**1682913 · Analítica de Datos · Cuaderno del estudiante · Edición guiada 2**

Este es el archivo **Introduccion_Python_Analitica_Industrial.ipynb** de la clase. Contiene las explicaciones, veinte ejecuciones guiadas y ocho retos. Los datos de la fábrica son sintéticos; el código sí se ejecuta y genera resultados.

**Empieza aquí:** guarda una copia en Drive, conéctate al entorno y ejecuta de arriba abajo. Antes de cada celda encontrarás qué hacer y qué debería aparecer. Los títulos «Ejecución 01…20» son referencias de la clase; los números entre corchetes que muestra Colab cambian con el orden en que ejecutes.

En los retos, escribe tu solución en la celda señalada. No es necesario completar los retos para que los ejemplos siguientes funcionen. Cuando quieras volver al ejemplo original, restaura sus valores y ejecuta nuevamente desde arriba.


## 1. Python y los entornos de trabajo
Python es un lenguaje: expresamos instrucciones para que un intérprete las ejecute. Un **algoritmo** es una secuencia de pasos; un **programa** es su implementación. Un **editor** permite escribir; el **intérprete** ejecuta; el **kernel** conserva el estado del notebook; una **librería** aporta funciones reutilizables.

Un notebook `.ipynb` combina celdas de texto Markdown, código y resultados. Un archivo `.py` contiene código y resulta útil para ejecutar tareas completas. GitHub permite consultar el notebook, pero para ejecutar sus celdas debes abrirlo en Jupyter o Colab.

| Aspecto | Jupyter en tu equipo | Google Colab |
|---|---|---|
| Inicio | Requiere Python y paquetes locales | Se abre en el navegador |
| Archivos | Permanecen en la carpeta donde los guardas | Los archivos del entorno de ejecución son temporales |
| Ejecución | Usa los recursos de tu computador | Usa un entorno remoto con disponibilidad variable |
| Guardado | Guarda el `.ipynb` localmente | Guarda una copia en Drive o descarga el `.ipynb` |
| Uso propuesto | Trabajo local y control del entorno | Comenzar con poca instalación |

### Opción A · Colab paso a paso
El archivo de esta clase se llama **Introduccion_Python_Analitica_Industrial.ipynb**. Un `.ipynb` es un cuaderno que contiene explicaciones, código y espacios para resolver los ejercicios; no debes buscar un archivo desconocido ni crearlo desde cero.

1. Pulsa [Abrir el cuaderno de esta clase en Colab](https://colab.research.google.com/github/karendayana2590-bot/1682913-ANAL-TICA-DE-DATOS/blob/main/clase-python/Introduccion_Python_Analitica_Industrial.ipynb) e inicia sesión con Google si se solicita. Este enlace abre directamente el archivo de la clase.
2. Selecciona **Archivo → Guardar una copia en Drive** y trabaja en esa copia. Si prefieres subir el archivo manualmente, primero [descarga el cuaderno de la clase](https://raw.githubusercontent.com/karendayana2590-bot/1682913-ANAL-TICA-DE-DATOS/main/clase-python/Introduccion_Python_Analitica_Industrial.ipynb). Luego abre Colab, usa **Archivo → Subir notebook** y selecciona **Introduccion_Python_Analitica_Industrial.ipynb** desde la carpeta donde lo descargaste, normalmente **Descargas**. Los nombres de menú pueden variar con el idioma.
3. Conecta el entorno y ejecuta la primera celda con **Shift+Enter**.
4. Prueba una celda de texto y otra de código. El botón `+ Código` agrega instrucciones; `+ Texto` agrega explicaciones.
5. Guarda una copia en Drive o descarga el notebook. Descargar el notebook no descarga automáticamente los CSV generados.
6. El caso industrial ya incluye los datos dentro del cuaderno: **no necesitas subir un CSV para empezar**. Para practicar además la lectura de archivos, descarga **produccion.csv** desde **Materiales → Descargar datos CSV** en la página de la clase y súbelo desde el panel de archivos de Colab. Después podrás leerlo con `pd.read_csv("produccion.csv")`. Vuelve a subirlo si el entorno se reinicia o desaparece.

### Qué vas a ejecutar
Los ocho retos y el programa industrial son ejercicios ejecutables en Python. Los ejemplos iniciales usan números definidos en sus celdas; el proyecto final trabaja con doce registros sintéticos de dos líneas durante seis días. Los datos son hipotéticos para aprender, pero los cálculos, las validaciones y los archivos que genera el programa son reales. La página web permite usar el laboratorio y la autoevaluación; el código Python se ejecuta en el cuaderno de Colab o Jupyter.

### Opción B · Jupyter paso a paso
Con Python 3 instalado, abre una terminal en la carpeta de la clase. En Windows puedes usar `py` en lugar de `python` si ese es el lanzador disponible.
```text
python -m venv .venv
```
Activa el entorno con `.venv\Scripts\Activate.ps1` en PowerShell o `source .venv/bin/activate` en macOS/Linux. Si PowerShell bloquea la activación, puedes usar directamente `.venv\Scripts\python.exe` en lugar de `python`, sin cambiar políticas del sistema.
```text
python -m pip install jupyterlab numpy pandas matplotlib ipywidgets
python -m jupyterlab
```
Descarga **Introduccion_Python_Analitica_Industrial.ipynb**, guárdalo en la carpeta de la clase y ábrelo desde el explorador de archivos de Jupyter. Si prefieres la interfaz clásica Jupyter Notebook, instala `notebook` y ejecuta `python -m notebook`.

### Cómo trabajar sin perderte
- Ejecuta de arriba abajo; una celda puede necesitar variables de celdas anteriores.
- `[*]` indica ejecución; el número entre corchetes registra el orden de ejecución, no la posición de la celda.
- Guarda con frecuencia. Reiniciar el kernel borra variables, pero no el texto guardado.
- Antes de entregar: **reinicia y ejecuta todas las celdas**. Esto descubre dependencias ocultas.
- Markdown admite `# Título`, `**negrita**`, listas y tablas. El código usa sangría de cuatro espacios para delimitar bloques.

**Actividad:** escribe tu nombre en una celda de texto, ejecuta un saludo, cambia el mensaje y reinicia el kernel. Explica qué desapareció y qué permaneció.

Referencias de instalación: [Jupyter](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) y [preguntas frecuentes de Colab](https://research.google.com/colaboratory/faq.html).


### Ejecución 01 · Comprobar que Python funciona

**Haz esto:** Ejecuta la celda completa con el botón triangular de su izquierda o Shift+Enter.

**Debes ver:** Aparecen un saludo, la versión de Python y 95.0 % de calidad.

**Comprende:** Python ejecuta instrucciones. print muestra valores; 950 / 1000 * 100 transforma una razón en porcentaje.

**Prueba y explica:** Cambia solo el mensaje del saludo y vuelve a ejecutar.


```python
import sys
print("¡Hola, equipo de analítica industrial!")
print("Versión de Python:", sys.version.split()[0])
print("Mi primer indicador:", 950 / 1000 * 100, "% de calidad")
```

## 2. Variables, tipos y operadores
Una variable es un nombre asociado a un valor. `=` asigna; `==` compara. Usa nombres como `unidades_buenas`: indican qué mide el dato. Python distingue mayúsculas y minúsculas; no uses espacios ni empieces con un número. Los comentarios comienzan con `#`.

| Tipo | Ejemplo | Aplicación |
|---|---|---|
| `int` | `1000` | Unidades enteras |
| `float` | `7.5` | Horas o mediciones decimales |
| `str` | `"Línea A"` | Texto entre comillas |
| `bool` | `True`, `False` | Cumple o no cumple |
| `None` | `None` | Ausencia de valor, diferente de cero |

Operadores: `+`, `-`, `*`, `/` (división), `//` (cociente entero), `%` (residuo), `**` (potencia). Usa paréntesis para hacer explícito el orden. Los decimales se escriben con punto en el código. Una tasa `0.95` corresponde a `95 %`; no multipliques dos veces por 100.


### Ejecución 02 · Guardar datos en variables

**Haz esto:** Ejecuta sin cambiar los valores iniciales; identifica producidas, defectuosas y horas.

**Debes ver:** 950 unidades buenas, calidad 95.00 %, 39 cajas completas y 14 unidades restantes.

**Comprende:** Cada nombre representa un dato. Primero se calculan buenas; después se usan para calcular calidad y cajas.

**Prueba y explica:** Cambia defectuosas de 50 a 20 y predice las buenas antes de ejecutar.


```python
linea = "A"
producidas = 1000
defectuosas = 50
horas = 7.5
buenas = producidas - defectuosas
calidad_pct = buenas / producidas * 100
cumple = calidad_pct >= 97
print(type(producidas), type(horas), type(linea), type(cumple))
print(f"Línea {linea}: {buenas} unidades buenas; calidad {calidad_pct:.2f}%")
print("Cajas completas de 24:", buenas // 24, "Unidades restantes:", buenas % 24)
```

### Conversión y entrada de datos
`input()` devuelve texto, aunque escribas números. Convierte con `int()` para enteros o `float()` para decimales. `float("7,5")` produce un error: acuerda el separador decimal. En el notebook usamos datos ya definidos para que **Ejecutar todo** no se quede esperando una respuesta.
```python
horas = float(input("Horas trabajadas (usa punto decimal): "))
```
Los valores decimales pueden tener pequeñas aproximaciones binarias. Redondea para mostrar; conserva precisión durante los cálculos.


### Ejecución 03 · Convertir texto a números

**Haz esto:** Compara las dos líneas que usan 100 y 20: una trabaja con texto y otra con enteros.

**Debes ver:** 8.0; 10020; 120; tasa de rechazo 5.0 % con los valores iniciales.

**Comprende:** Sumar textos concatena. int y float convierten valores. El porcentaje depende de las variables de la celda anterior.

**Prueba y explica:** Vuelve a los datos iniciales si quieres comparar con estas respuestas de referencia.


```python
texto_horas = "7.5"
horas_convertidas = float(texto_horas)
print(horas_convertidas + 0.5)
print("100" + "20")  # concatenación: 10020
print(int("100") + int("20"))  # suma: 120
print(f"Tasa de rechazo: {defectuosas / producidas:.1%}")
```

### 🧩 Reto 1 · Un turno en números

Un turno produce 840 unidades, 21 defectuosas, durante 7 horas con 3 operarios. Calcula buenas, calidad porcentual, unidades buenas/hora y unidades buenas/hora-persona. ¿Por qué los dos últimos resultados son diferentes?

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
buenas = 840 - 21
print(buenas)  # 819
print(buenas / 840 * 100)  # 97.5 %
print(buenas / 7)  # 117 unidades buenas/hora
print(buenas / (7 * 3))  # 39 unidades buenas/hora-persona
```

</details>


## 3. Colecciones: organizar varios datos
Una **lista** almacena una secuencia modificable; una **tupla** agrupa elementos que no se reasignan individualmente; un **diccionario** relaciona claves con valores; un **conjunto** conserva elementos únicos.

Los índices comienzan en cero. `lista[0]` es el primer elemento y `lista[-1]` el último. El corte `lista[1:3]` incluye las posiciones 1 y 2, pero excluye la 3. Modificar una lista afecta a otros nombres que apunten a la misma lista; usa `.copy()` si necesitas una copia independiente superficial.


### Ejecución 04 · Organizar varios registros

**Haz esto:** Ejecuta y localiza el primer dato, el último, el corte y el valor agregado con append.

**Debes ver:** La lista tiene seis días y suma 5520 unidades; el diccionario tiene 970 buenas.

**Comprende:** Lista: secuencia de valores. Diccionario: registro con campos. Los índices comienzan en cero.

**Prueba y explica:** Agrega un séptimo valor a una copia de la lista y vuelve a sumar.


```python
produccion_diaria = [800, 920, 870, 1000, 950]
print(produccion_diaria[0], produccion_diaria[-1], produccion_diaria[1:3])
produccion_diaria.append(980)
print("Días:", len(produccion_diaria), "Total:", sum(produccion_diaria))
turno = {"linea": "A", "producidas": 1000, "defectuosas": 30}
turno["buenas"] = turno["producidas"] - turno["defectuosas"]
print(turno, turno.get("supervisor", "Sin registrar"))
coordenada = (2, 3)
lineas_unicas = set(["A", "B", "A", "C"])
print(sorted(lineas_unicas))
```

### 🧩 Reto 2 · Registro de turno

Crea un diccionario con línea, horas, operarios y producción. Agrega la productividad bruta por hora-persona. Usa 600 unidades, 5 horas y 4 operarios.

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
registro = dict(linea="B", horas=5, operarios=4, producidas=600)
registro["productividad_bruta"] = registro["producidas"] / (registro["horas"] * registro["operarios"])
print(registro)  # 30 unidades/hora-persona
```

</details>


## 4. Condicionales: convertir criterios en decisiones
`if` pregunta si una condición es verdadera, `elif` prueba otra y `else` cubre el resto. Python ejecuta la primera rama que corresponde. La sangría determina qué instrucciones pertenecen a cada rama.

Comparaciones: `==`, `!=`, `<`, `<=`, `>`, `>=`. Conecta condiciones con `and`, `or` y `not`. Para comprobar ausencia usa `valor is None`.

**Regla didáctica de calidad:** verde ≥ 98 %, amarillo ≥ 95 % y < 98 %, rojo < 95 %. Son umbrales de práctica, no estándares universales. En una empresa deben acordarse según producto y proceso.


### Ejecución 05 · Tomar decisiones con condiciones

**Haz esto:** Identifica el bloque que corresponde a calidad = 96.5 y ejecuta.

**Debes ver:** Amarillo y el mensaje de datos aptos para calcular unidades/hora.

**Comprende:** Se ejecuta la primera condición verdadera. La sangría delimita cada rama.

**Prueba y explica:** Prueba exactamente 95 y 98 para revisar las fronteras del semáforo.


```python
calidad = 96.5
if calidad >= 98:
    estado = "Verde"
elif calidad >= 95:
    estado = "Amarillo"
else:
    estado = "Rojo"
print(estado)

horas = 8
producidas = 1000
if horas > 0 and producidas >= 0:
    print("Datos aptos para calcular unidades/hora")
else:
    print("Revisar los datos antes de calcular")
```

### 🧩 Reto 3 · Fronteras del semáforo

Prueba calidades de 94.9, 95, 97.9, 98 y 100. Después agrega una validación que rechace valores menores que 0 o mayores que 100.

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
calidad = 101
if not 0 <= calidad <= 100:
    print("Calidad inválida")
elif calidad >= 98:
    print("Verde")
elif calidad >= 95:
    print("Amarillo")
else:
    print("Rojo")
```

</details>


## 5. Ciclos: repetir sin copiar instrucciones
Usa `for` para recorrer una colección o un rango. `range(1, 4)` genera 1, 2 y 3. `enumerate()` entrega posición y valor; `zip()` permite recorrer dos colecciones a la vez, pero se detiene en la más corta.

`while` repite mientras una condición sea verdadera: debe existir un cambio que permita terminar. `break` termina el ciclo; `continue` pasa a la siguiente iteración. Un **acumulador** suma valores; un **contador** cuenta ocurrencias. Una comprensión de listas abrevia transformaciones simples, sin reemplazar la claridad.


### Ejecución 06 · Repetir con ciclos

**Haz esto:** Sigue el acumulado en cada vuelta del for y luego observa el while.

**Debes ver:** El acumulado final es 3590. Hay tres inspecciones. La lectura se detiene al encontrar -1.

**Comprende:** for recorre datos; while necesita una condición de salida. continue omite una vuelta y break termina.

**Prueba y explica:** Explica por qué el 30 situado después del -1 no se procesa.


```python
totales = [800, 920, 870, 1000]
acumulado = 0
for dia, unidades in enumerate(totales, start=1):
    acumulado += unidades
    print(f"Día {dia}: {unidades}; acumulado: {acumulado}")

intentos = 0
while intentos < 3:
    intentos += 1
    print("Inspección", intentos)

for valor in [10, None, 20, -1, 30]:
    if valor is None:
        continue
    if valor < 0:
        print("Se detuvo por valor inválido")
        break
    print("Válido:", valor)

cumplimientos = [u / 900 * 100 for u in totales]
print(cumplimientos)
```

### 🧩 Reto 4 · Detector de turnos

Para [92, 98, 96, 99, 94], cuenta cuántos turnos tienen calidad menor que 95 %. Muestra sus posiciones contando desde 1.

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
alertas = 0
for posicion, calidad in enumerate([92, 98, 96, 99, 94], start=1):
    if calidad < 95:
        alertas += 1
        print("Revisar turno", posicion)
print("Alertas:", alertas)  # 2
```

</details>


## 6. Funciones: reglas que se pueden reutilizar
`def` define una función; los **parámetros** son los nombres de entrada y los **argumentos** son los valores que entregas. `return` devuelve un resultado; `print` solamente lo muestra. Una variable creada dentro de una función normalmente es local.

Una buena función tiene un propósito, nombres claros, documentación breve y validación de sus entradas. Un argumento predeterminado evita repetir una opción habitual. Las anotaciones de tipo ayudan a leer, pero no validan automáticamente.


### Ejecución 07 · Reutilizar una función

**Haz esto:** Ejecuta la definición y las dos llamadas al final de la celda.

**Debes ver:** Para 840, 21, 7 y 3: 819 buenas, 97.5 % de calidad, 117 buenas/hora y 39 buenas/hora-persona. Sin producción, calidad es None.

**Comprende:** Los argumentos entran, la validación revisa y return devuelve un diccionario de indicadores.

**Prueba y explica:** Explica la diferencia entre mostrar un valor y devolverlo.


```python
def calcular_indicadores(producidas, defectuosas, horas, operarios=1):
    """Calcula calidad y productividad de un turno con conteos enteros."""
    for nombre, valor in [("producidas", producidas), ("defectuosas", defectuosas), ("operarios", operarios)]:
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError(f"{nombre} debe ser entero")
    if isinstance(horas, bool) or not isinstance(horas, (int, float)):
        raise ValueError("horas debe ser numérico")
    import math
    if not math.isfinite(horas) or horas <= 0 or operarios <= 0:
        raise ValueError("Horas y operarios deben ser positivos y finitos")
    if producidas < 0 or not 0 <= defectuosas <= producidas:
        raise ValueError("Los conteos deben ser coherentes")
    buenas = producidas - defectuosas
    return {
        "buenas": buenas,
        "calidad_pct": buenas / producidas * 100 if producidas else None,
        "buenas_hora": buenas / horas,
        "buenas_hora_persona": buenas / (horas * operarios),
    }

resultado = calcular_indicadores(840, 21, 7, operarios=3)
print(resultado)
print(calcular_indicadores(0, 0, 8, 2))
```

### Cero no es lo mismo que no definido
Si no se produjo ninguna unidad, la calidad `buenas/producidas` no está definida. No corresponde inventar 0 % o 100 %. Si hubo horas trabajadas y cero buenas, la productividad sí es cero. Esta diferencia cambia la interpretación de un reporte.


### 🧩 Reto 5 · Función de cumplimiento

Define `cumplimiento(real, meta)` que devuelva porcentaje, rechace metas ≤ 0 y producción negativa. Prueba (900, 1000) y (1100, 1000). ¿Un resultado mayor que 100 siempre es un error?

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
def cumplimiento(real, meta):
    if meta <= 0 or real < 0:
        raise ValueError("Revisar real y meta")
    return real / meta * 100
print(cumplimiento(900, 1000))  # 90
print(cumplimiento(1100, 1000))  # 110: puede superar la meta
```

</details>


## 7. Errores, depuración y comprobaciones
| Mensaje | Causa típica | Acción |
|---|---|---|
| `SyntaxError` | Falta `:` o comilla | Revisa la línea indicada y la anterior |
| `IndentationError` | Sangría inconsistente | Alinea bloques con cuatro espacios |
| `NameError` | Variable inexistente | Revisa nombre y orden de ejecución |
| `TypeError` | Operación entre tipos incompatibles | Comprueba `type()` y convierte conscientemente |
| `ValueError` | Valor no convertible o no permitido | Valida y corrige la entrada |
| `ZeroDivisionError` | Denominador cero | Decide si corresponde rechazar o marcar ausente |
| `KeyError` | Clave o columna inexistente | Inspecciona nombres y espacios |
| `FileNotFoundError` | Ruta incorrecta | Revisa carpeta actual y archivo |
| `ModuleNotFoundError` | Librería ausente en el kernel | Instala en el entorno correcto |

Lee la última línea del error y luego la ubicación. Reproduce con pocos datos. `try/except` permite responder a errores esperados; no uses un `except` vacío que oculte fallos. `assert` ayuda en ejercicios y pruebas; la validación del programa debe usar condiciones y excepciones.


### Ejecución 08 · Reconocer un error esperado

**Haz esto:** Ejecuta el ejemplo completo, incluido try/except.

**Debes ver:** Se informa que la entrada fue rechazada y luego aparecen las comprobaciones superadas.

**Comprende:** El error es intencional: no puede haber 120 defectuosas entre 100 producidas. La celda lo captura para seguir.

**Prueba y explica:** Distingue ese mensaje controlado de un error rojo que interrumpe la ejecución.


```python
try:
    calcular_indicadores(100, 120, 8)
except ValueError as error:
    print("Entrada rechazada:", error)

assert calcular_indicadores(100, 5, 2, 2)["buenas"] == 95
assert calcular_indicadores(0, 0, 2)["calidad_pct"] is None
print("Comprobaciones superadas")
```

## 8. Librerías y reproducibilidad
Un **módulo** es código importable; un **paquete** organiza módulos. `import numpy as np` usa un alias convencional. Importar no instala: los paquetes deben existir en el entorno del kernel.

- Biblioteca estándar: `math`, `pathlib`, `csv`; viene con Python.
- NumPy: arreglos y cálculo numérico vectorizado.
- pandas: tablas, tipos, filtros, agrupaciones y archivos.
- Matplotlib: gráficos.
- ipywidgets: controles interactivos, opcionales en esta clase.

Si hace falta, ejecuta `%pip install numpy pandas matplotlib ipywidgets` en una nueva celda y reinicia el kernel si el entorno lo pide. `%pip` es una instrucción del notebook, no Python estándar. Registra versiones y usa un entorno virtual para reproducir un trabajo.


### Ejecución 09 · Cargar las librerías

**Haz esto:** Ejecuta antes de los ejemplos de NumPy y pandas.

**Debes ver:** Se muestran las versiones de NumPy y pandas y la carpeta de trabajo. Las versiones pueden variar.

**Comprende:** Importar pone las herramientas disponibles en este entorno. No carga todavía los datos de producción.

**Prueba y explica:** Si falta un paquete, ejecuta %pip install numpy pandas matplotlib ipywidgets en una celda aparte y vuelve aquí.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
print("NumPy", np.__version__, "pandas", pd.__version__)
print("Carpeta actual:", Path.cwd())
```

## 9. NumPy: pensar en arreglos
Una lista de Python es flexible; un arreglo NumPy suele almacenar elementos de un mismo tipo y realiza operaciones elemento a elemento. `lista * 2` repite una lista; `arreglo * 2` multiplica sus valores.

`shape` indica dimensiones, `ndim` cuántos ejes hay y `dtype` el tipo. En una matriz de días × líneas, `axis=0` resume sobre días y entrega un resultado por línea; `axis=1` resume sobre líneas y entrega un resultado por día.

Una máscara booleana selecciona elementos. La **vectorización** expresa una operación sobre el arreglo entero. El **broadcasting** permite operaciones entre formas compatibles, como dividir cada columna por su meta. `np.nan` representa un dato numérico ausente; no es un cero.


### Ejecución 10 · Calcular con NumPy

**Haz esto:** Ejecuta y compara lista * 2 con arreglo * 2.

**Debes ver:** La matriz tiene forma (3, 2); las sumas por línea son 2550 y 2850; las sumas por día son 1700, 1800 y 1900.

**Comprende:** Un arreglo opera elemento a elemento. El eje elegido determina qué dimensión se resume.

**Prueba y explica:** Explica por qué np.nan no debe reemplazarse automáticamente por cero.


```python
lista = [800, 900, 1000]
arreglo = np.array(lista)
print("Lista:", lista * 2, "Arreglo:", arreglo * 2)
matriz = np.array([[800, 900], [850, 950], [900, 1000]])
print("Forma:", matriz.shape, "Ejes:", matriz.ndim, "Tipo:", matriz.dtype)
print("Total por línea:", matriz.sum(axis=0))
print("Total por día:", matriz.sum(axis=1))
print("Cumplimiento por día y línea (%):", matriz / np.array([900, 1000]) * 100)
print("Valores mayores que 900:", matriz[matriz > 900])
print("Media:", arreglo.mean(), "Mediana:", np.median(arreglo))
print("Desviación poblacional:", arreglo.std(ddof=0))
print("Desviación muestral:", arreglo.std(ddof=1))
mediciones = np.array([10.0, np.nan, 12.0])
print("Media excluyendo ausente:", np.nanmean(mediciones))
```

La media resume nivel; la desviación resume dispersión. `ddof=0` describe la población disponible; `ddof=1` se usa para la estimación muestral habitual. Excluir ausentes cambia la base analizada: informa cuántos faltan y no sustituyas automáticamente por la media.


### 🧩 Reto 6 · Vectorizar calidad

Con producidas [100, 200, 0] y defectuosas [2, 10, 0], calcula calidad sin dividir por cero. El tercer resultado debe ser ausente.

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
p = np.array([100, 200, 0])
d = np.array([2, 10, 0])
q = np.divide(p-d, p, out=np.full(3, np.nan), where=p>0) * 100
print(q)  # [98., 95., nan]
```

</details>


## 10. pandas: trabajar con tablas
Una **Series** es una columna con índice; un **DataFrame** es una tabla. El índice identifica filas, pero no sustituye necesariamente una clave de negocio. Inspecciona antes de calcular: `head()`, `shape`, `columns`, `dtypes`, `info()` y `describe()`.

`df["columna"]` selecciona una serie; `df[["a", "b"]]` una tabla. `.loc` selecciona por etiquetas o condiciones; `.iloc` por posiciones. Usa `&` para «y», `|` para «o» y paréntesis en cada condición vectorizada. Evita asignaciones encadenadas; usa `.loc` o `.copy()`.


### Ejecución 11 · Explorar una tabla con pandas

**Haz esto:** Ejecuta; revisa la tabla, los tipos, el filtro y la agrupación.

**Debes ver:** La tabla original tiene tres filas. El filtro A y producidas ≥ 110 selecciona el registro de 120 unidades.

**Comprende:** Un DataFrame es una tabla. Filtrar selecciona registros y agrupar resume varios registros.

**Prueba y explica:** Busca las 215 buenas de A y las 141 buenas de B en el resumen.


```python
mini = pd.DataFrame({"linea": ["A", "B", "A"], "producidas": [100, 150, 120], "defectuosas": [2, 9, 3]})
display(mini.head())
print(mini.shape, mini.dtypes, sep="\n")
mini.info()
display(mini.describe())
display(mini.loc[(mini["linea"] == "A") & (mini["producidas"] >= 110), ["linea", "producidas"]])
display(mini.iloc[:2])
mini["buenas"] = mini["producidas"] - mini["defectuosas"]
display(mini.sort_values("buenas", ascending=False))
display(mini.groupby("linea", as_index=False)[["producidas", "buenas"]].sum())
```

### Archivos, faltantes y uniones
Lee CSV con `pd.read_csv("archivo.csv")`. Si usa `;` y coma decimal, especifica `sep=";", decimal=","`. Mira el archivo antes de escoger. Exporta con `index=False` para no agregar una columna de índices sin intención.

`isna()` detecta faltantes; `duplicated()` identifica repetidos; `pd.to_numeric(..., errors="coerce")` convierte texto inválido en ausente para detectarlo. `dropna()` descarta y `fillna()` imputa: ambas decisiones requieren justificación. No borres duplicados sin definir qué identifica un registro.

`merge` combina tablas por una clave. Una unión mal definida multiplica filas y puede inflar la producción. Usa `validate` para verificar la relación esperada. `pivot_table` reorganiza datos para comparar grupos.


### Ejecución 12 · Guardar, leer y unir tablas

**Haz esto:** Ejecuta y comprueba que aparezca mini_produccion.csv en el panel de archivos.

**Debes ver:** Se agregan los productos Envase/Tapa, se conserva la cantidad de filas y se muestra el resumen por línea.

**Comprende:** El archivo guarda una tabla. merge usa una clave y validate evita una relación inesperada.

**Prueba y explica:** Explica qué podría pasar si el catálogo repitiera una misma línea.


```python
catalogo = pd.DataFrame({"linea": ["A", "B"], "producto": ["Envase", "Tapa"]})
enriquecida = mini.merge(catalogo, on="linea", how="left", validate="many_to_one")
display(enriquecida)
mini.to_csv("mini_produccion.csv", index=False)
recuperada = pd.read_csv("mini_produccion.csv")
assert len(recuperada) == len(mini)
display(mini.pivot_table(index="linea", values="buenas", aggfunc="sum"))
```

### 🧩 Reto 7 · Filtrar y agrupar

En mini, muestra registros con más de 110 unidades y calcula el total de defectuosas por línea. ¿Qué diferencia existe entre el número de filas y el total producido?

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
display(mini.loc[mini["producidas"] > 110])
display(mini.groupby("linea")["defectuosas"].sum())
print(len(mini), mini["producidas"].sum())  # 3 registros; 370 unidades
```

</details>


## 11. Proyecto industrial: la planta de envases
Dos líneas fabrican el **mismo producto comparable** durante seis días. La jefatura necesita saber cuál cumple su meta, cuál pierde más unidades por calidad y dónde conviene investigar. Todos los datos son sintéticos.

### Diccionario y supuestos
| Campo | Significado | Regla |
|---|---|---|
| fecha | Día del registro | Fecha válida |
| linea | A o B | Junto a fecha forma la clave única |
| producidas | Unidades totales fabricadas | Entero ≥ 0 |
| defectuosas | Unidades no conformes distintas | Entero entre 0 y producidas |
| horas | Horas de trabajo del turno | Positivo; incluye paradas dentro del turno |
| operarios | Personas durante todo el turno | Entero positivo |
| meta | Unidades totales planeadas | Entero positivo |

Una unidad defectuosa se cuenta una vez aunque tenga varios defectos. No hay reproceso en este ejemplo. `horas × operarios` supone que todos trabajan las mismas horas; si no, suma las horas individuales. La productividad laboral usa unidades buenas/hora-persona. No es OEE: para OEE necesitaríamos disponibilidad, tiempo operativo y velocidad ideal claramente definidos.

Los datos están incluidos en el notebook para ejecutarlo sin descargar archivos adicionales. El CSV que se escribe aquí contiene los mismos registros que el archivo entregado.


### Ejecución 13 · Elegir y cargar los datos industriales

**Haz esto:** Para la primera práctica deja USAR_ARCHIVO_PROPIO = False y ejecuta. No subas archivos todavía.

**Debes ver:** Con los datos incluidos aparecen doce registros, dos líneas y siete columnas originales. Se informa el origen de los datos.

**Comprende:** Esta es la única celda de entrada del caso: raw contiene los registros que luego se validarán.

**Prueba y explica:** Para practicar la carga manual, sigue la explicación de archivo propio debajo; después vuelve a ejecutar desde aquí.


```python
from io import StringIO
CSV_DATOS = 'fecha,linea,producidas,defectuosas,horas,operarios,meta\n2026-09-01,A,1000,20,8,4,1000\n2026-09-01,B,900,45,8,3,950\n2026-09-02,A,1100,22,8,4,1000\n2026-09-02,B,950,19,8,3,950\n2026-09-03,A,980,49,8,4,1000\n2026-09-03,B,1000,20,8,3,950\n2026-09-04,A,1050,21,8,4,1000\n2026-09-04,B,920,46,8,3,950\n2026-09-05,A,1080,54,8,4,1000\n2026-09-05,B,980,49,8,3,950\n2026-09-06,A,1020,20,8,4,1000\n2026-09-06,B,960,24,8,3,950\n'
USAR_ARCHIVO_PROPIO = False
ARCHIVO_PROPIO = "produccion_usuario.csv"

if USAR_ARCHIVO_PROPIO:
    archivo = Path(ARCHIVO_PROPIO)
    if not archivo.is_file():
        raise FileNotFoundError(f"Sube {ARCHIVO_PROPIO} al panel de archivos antes de continuar")
    raw = pd.read_csv(archivo)
    print("Origen: archivo subido por ti →", ARCHIVO_PROPIO)
else:
    raw = pd.read_csv(StringIO(CSV_DATOS))
    print("Origen: datos sintéticos incluidos en el cuaderno")

print("Filas:", len(raw), "Columnas:", len(raw.columns))
display(raw)
```

### Práctica opcional: cargar el CSV desde tu computador

1. En la página de la clase abre **Materiales → Descargar datos CSV**. El archivo se llama **produccion.csv**.
2. En tu computador, crea una copia con el nombre **produccion_usuario.csv**. Conserva la extensión `.csv` una sola vez.
3. En Colab, abre el panel de **Archivos** (icono de carpeta a la izquierda), pulsa **Subir** y selecciona esa copia desde Descargas o la carpeta donde la guardaste.
4. Espera a que **produccion_usuario.csv** aparezca en la lista. Esto carga datos, no un notebook.
5. En la celda anterior cambia solo **USAR_ARCHIVO_PROPIO = False** por **USAR_ARCHIVO_PROPIO = True** y vuelve a ejecutarla.
6. Debe mostrarse «Origen: archivo subido por ti». Con la copia sin modificar seguirás viendo doce filas y siete columnas.
7. Continúa con la validación y vuelve a ejecutar todos los pasos del caso hasta exportar. Si cambias datos, no reutilices resultados anteriores.

El código no sobrescribe el archivo que subes. Si reinicias o pierdes el entorno de Colab, puede ser necesario subirlo de nuevo. Si necesitas trabajar sin subir archivos, vuelve a poner `False`.

Para un archivo distinto respeta las columnas `fecha,linea,producidas,defectuosas,horas,operarios,meta`, fechas como `2026-09-01`, separador coma y punto decimal. El catálogo del ejercicio admite A y B. No agregues dos registros de la misma fecha y línea. Si tu CSV usa punto y coma, adapta la lectura a `pd.read_csv(archivo, sep=";", decimal=",")` y verifica los tipos antes de continuar.


## 12. Validar antes de analizar
El programa rechaza registros inconsistentes: no corrige datos por adivinación. Para el caso completo no se permiten faltantes. En otro proyecto podrías separar registros rechazados, informar su proporción y pedir corrección a la fuente.

**Taller de detectives:** crea una copia de `raw`, cambia horas a cero, defectuosas a 2000 o línea a `C`, e intenta validarla. Luego duplica una fila. Explica cada mensaje. No modifiques la tabla original para continuar la clase.


### Ejecución 14 · Validar el archivo

**Haz esto:** Ejecuta la definición de validar_datos y su llamada con raw.

**Debes ver:** Con el conjunto incluido: Registros válidos: 12.

**Comprende:** Se verifican columnas, fechas, faltantes, enteros, rangos y clave fecha-línea. No se inventan correcciones.

**Prueba y explica:** Si tu archivo falla, corrígelo en la fuente, vuelve a cargarlo y repite este paso.


```python
def validar_datos(tabla):
    requeridas = ["fecha", "linea", "producidas", "defectuosas", "horas", "operarios", "meta"]
    faltantes = set(requeridas) - set(tabla.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas: {sorted(faltantes)}")
    if tabla.empty:
        raise ValueError("No hay registros")
    datos = tabla[requeridas].copy()
    datos["fecha"] = pd.to_datetime(datos["fecha"], errors="coerce")
    datos["linea"] = datos["linea"].astype("string").str.strip().str.upper()
    numericas = ["producidas", "defectuosas", "horas", "operarios", "meta"]
    for columna in numericas:
        datos[columna] = pd.to_numeric(datos[columna], errors="coerce")
    if datos.isna().any().any():
        raise ValueError("Hay ausentes, fechas inválidas o números no convertibles")
    if not np.isfinite(datos[numericas].to_numpy(dtype=float)).all():
        raise ValueError("Hay números infinitos")
    if not datos["linea"].isin(["A", "B"]).all():
        raise ValueError("Línea fuera del catálogo A/B")
    if datos.duplicated(["fecha", "linea"]).any():
        raise ValueError("Clave fecha-línea duplicada")
    enteras = ["producidas", "defectuosas", "operarios", "meta"]
    if ((datos[enteras] % 1) != 0).any().any():
        raise ValueError("Los conteos deben ser enteros")
    if (datos[["producidas", "defectuosas"]] < 0).any().any():
        raise ValueError("Conteos negativos")
    if (datos["defectuosas"] > datos["producidas"]).any():
        raise ValueError("Defectuosas supera producidas")
    if (datos[["horas", "operarios", "meta"]] <= 0).any().any():
        raise ValueError("Horas, operarios y meta deben ser positivos")
    return datos

df = validar_datos(raw)
print("Registros válidos:", len(df))
```

### Ejecución 15 · Probar una entrada incorrecta

**Haz esto:** Ejecuta la celda que crea prueba = raw.copy().

**Debes ver:** Error detectado correctamente: Horas, operarios y meta deben ser positivos.

**Comprende:** Se cambia una copia, no la tabla original. El error se provoca para demostrar la validación.

**Prueba y explica:** No copies ese cero a tus datos válidos.


```python
prueba = raw.copy()
prueba.loc[0, "horas"] = 0
try:
    validar_datos(prueba)
except ValueError as error:
    print("Error detectado correctamente:", error)
```

## 13. Indicadores: fórmulas, unidades y significado
| Indicador | Fórmula | Interpretación |
|---|---|---|
| Buenas | producidas − defectuosas | Unidades conformes |
| Calidad | buenas / producidas × 100 | Porcentaje de unidades conformes |
| Rechazo | defectuosas / producidas × 100 | Porcentaje de unidades no conformes |
| Cumplimiento | producidas / meta × 100 | Cumplimiento de meta bruta |
| Tasa de producción | producidas / horas | Unidades totales por hora de línea |
| Tasa de buenas | buenas / horas | Unidades conformes por hora de línea |
| Productividad laboral | buenas / horas-persona | Unidades conformes por hora-persona |

Calidad y rechazo deben sumar 100 % cuando hay producción. Cumplimiento puede superar 100 %. No confundas una meta de unidades totales con una meta de unidades buenas.

### Regla crucial: razón de sumas
La calidad global es `suma(buenas)/suma(producidas)`, no el promedio simple de porcentajes. Ejemplo: un turno con 9 buenas de 10 y otro con 100 buenas de 100 da 99.09 % global, no 95 %. Los tamaños de los turnos son distintos.


### Ejecución 16 · Calcular indicadores por registro y línea

**Haz esto:** Ejecuta después de validar. Lee las columnas buenas, calidad_pct y productividad_laboral.

**Debes ver:** Con los datos incluidos: A = 6044 buenas y B = 5507 buenas. Sus productividades son aproximadamente 31.48 y 38.24 buenas/hora-persona.

**Comprende:** Los porcentajes agrupados se calculan dividiendo sumas, no promediando porcentajes sin ponderación.

**Prueba y explica:** Señala el denominador de calidad y el de productividad; explica por qué son distintos.


```python
def agregar_indicadores(datos):
    tabla = datos.copy()
    tabla["buenas"] = tabla["producidas"] - tabla["defectuosas"]
    tabla["horas_persona"] = tabla["horas"] * tabla["operarios"]
    denominador = tabla["producidas"].replace(0, np.nan)
    tabla["calidad_pct"] = tabla["buenas"] / denominador * 100
    tabla["rechazo_pct"] = tabla["defectuosas"] / denominador * 100
    tabla["cumplimiento_pct"] = tabla["producidas"] / tabla["meta"] * 100
    tabla["producidas_hora"] = tabla["producidas"] / tabla["horas"]
    tabla["buenas_hora"] = tabla["buenas"] / tabla["horas"]
    tabla["productividad_laboral"] = tabla["buenas"] / tabla["horas_persona"]
    tabla["estado_calidad"] = np.select(
        [tabla["calidad_pct"].isna(), tabla["calidad_pct"] >= 98, tabla["calidad_pct"] >= 95],
        ["Sin producción", "Verde", "Amarillo"], default="Rojo")
    return tabla

def resumir(tabla, grupos):
    columnas = ["producidas", "defectuosas", "buenas", "horas", "horas_persona", "meta"]
    resumen = tabla.groupby(grupos, as_index=False)[columnas].sum()
    resumen["calidad_pct"] = resumen["buenas"] / resumen["producidas"].replace(0, np.nan) * 100
    resumen["cumplimiento_pct"] = resumen["producidas"] / resumen["meta"] * 100
    resumen["productividad_laboral"] = resumen["buenas"] / resumen["horas_persona"]
    return resumen

df = agregar_indicadores(df)
por_linea = resumir(df, "linea")
display(df.round(2))
display(por_linea.round(2))
```

**Interpretación de las horas:** al sumar horas de dos líneas simultáneas obtienes horas-línea, no el tiempo de reloj transcurrido en la planta. En cambio, sumar horas-persona representa el esfuerzo laboral total del caso. Escribe siempre la unidad completa.


### Ejecución 17 · Construir el resumen global

**Haz esto:** Ejecuta y contrasta con los totales de referencia.

**Debes ver:** 11940 producidas, 11551 buenas, calidad global 96.74 % y productividad global 34.38 buenas/hora-persona.

**Comprende:** El resumen global usa todas las unidades y todas las horas-persona del conjunto válido.

**Prueba y explica:** Si agregaste datos propios, tus resultados serán distintos: verifica con las fórmulas, no con estos totales fijos.


```python
total_producidas = df["producidas"].sum()
total_buenas = df["buenas"].sum()
calidad_global = total_buenas / total_producidas * 100
productividad_global = total_buenas / df["horas_persona"].sum()
print(f"Producción: {total_producidas:,} unidades")
print(f"Buenas: {total_buenas:,} unidades")
print(f"Calidad global: {calidad_global:.2f}%")
print(f"Productividad laboral: {productividad_global:.2f} unidades buenas/hora-persona")
print("Ejemplo razón de sumas:", (9+100)/(10+100)*100)
display(df.loc[df["calidad_pct"] < 98, ["fecha", "linea", "calidad_pct", "defectuosas"]])
```

### 🧩 Reto 8 · Pregunta de gerencia

¿Qué línea tiene mayor producción total? ¿Cuál tiene mayor productividad laboral? ¿Cuál tiene mayor calidad? Explica por qué no necesariamente gana la misma línea.

Antes de ejecutar, escribe tu predicción. Después modifica un dato y explica el cambio.


```python
# Escribe aquí tu propuesta. Puedes crear más celdas.
```

<details><summary>Ver una solución después de intentarlo</summary>

```python
for indicador in ["producidas", "productividad_laboral", "calidad_pct"]:
    fila = por_linea.loc[por_linea[indicador].idxmax()]
    print(indicador, fila["linea"], round(fila[indicador], 2))
# A: producción y calidad. B: productividad laboral.
# Los denominadores y las dotaciones son diferentes; esto no demuestra causalidad.
```

</details>


## 14. Visualizar para responder preguntas
Usa barras para comparar categorías y líneas para observar evolución temporal. Incluye títulos, unidades y umbrales cuando aporten contexto. Evita gráficos 3D y no recortes ejes sin explicarlo. Un porcentaje alto puede ocultar muchas unidades defectuosas si el volumen es grande.

**Antes de ejecutar:** dibuja a mano cuál crees que será la barra más alta de producción y la de productividad. Después contrasta con los gráficos.


### Ejecución 18 · Graficar los resultados

**Haz esto:** Ejecuta y observa las tres gráficas debajo de la celda.

**Debes ver:** A lidera producción; B lidera productividad laboral. Se genera indicadores.png.

**Comprende:** Un gráfico responde una pregunta concreta y debe mostrar unidades. Una barra mayor no significa mejor desempeño en todo.

**Prueba y explica:** Redacta una frase con cifra y unidad para cada una de las primeras dos gráficas.


```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].bar(por_linea["linea"], por_linea["producidas"], color="#2563eb")
axes[0].set(title="Producción total", ylabel="Unidades", xlabel="Línea")
axes[1].bar(por_linea["linea"], por_linea["productividad_laboral"], color="#059669")
axes[1].set(title="Productividad laboral", ylabel="Buenas / hora-persona", xlabel="Línea")
for linea, grupo in df.groupby("linea"):
    axes[2].plot(grupo["fecha"], grupo["calidad_pct"], marker="o", label=linea)
axes[2].axhline(98, color="gray", linestyle="--", label="Meta didáctica 98 %")
axes[2].set(title="Calidad diaria (eje 0–100)", ylabel="Calidad (%)", ylim=(0, 100))
axes[2].tick_params(axis="x", rotation=45)
axes[2].legend()
fig.tight_layout()
fig.savefig("indicadores.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 15. Laboratorio interactivo: ¿qué cambia si…?
Modifica producción, tasa de rechazo, horas y operarios. **Predice primero**. La simulación convierte la tasa solicitada en un conteo entero redondeado de defectuosas; por eso la calidad observada puede diferir ligeramente de la tasa ingresada.

1. Mantén 1000 unidades y reduce el rechazo de 5 % a 2 %. ¿Cuántas buenas recuperas?
2. Mantén todo lo demás y pasa de 4 a 3 operarios. El indicador sube matemáticamente. ¿Qué evidencia falta para afirmar que la operación puede sostenerlo?
3. Mantén las unidades y aumenta las horas. ¿Qué indicador disminuye?
4. Pon producción en cero. ¿Por qué la calidad no está definida?

Este es un modelo aritmético, no una predicción causal. Cambiar personal podría afectar velocidad, seguridad o calidad; el modelo no incluye esos efectos.


### Ejecución 19 · Experimentar con un escenario

**Haz esto:** Ejecuta. Si aparecen controles, modifícalos; si no, usa una nueva celda con simular(1000, 2.0, 8.0, 4).

**Debes ver:** El escenario inicial produce 950 buenas, 95 % de calidad y aproximadamente 29.69 buenas/hora-persona. Con 2 % de rechazo: 980, 98 % y 30.63.

**Comprende:** El simulador es una comparación aritmética de supuestos, no una predicción causal del proceso.

**Prueba y explica:** Conserva la producción y baja el rechazo. Explica qué indicador cambia y por qué.


```python
def simular(producidas=1000, rechazo_pct=5.0, horas=8.0, operarios=4):
    defectuosas = round(producidas * rechazo_pct / 100)
    r = calcular_indicadores(producidas, defectuosas, horas, operarios)
    calidad = "No definida" if r["calidad_pct"] is None else f"{r['calidad_pct']:.2f}%"
    print(f"Buenas: {r['buenas']} | Calidad: {calidad}")
    print(f"Productividad: {r['buenas_hora_persona']:.2f} buenas/hora-persona")

try:
    import ipywidgets as widgets
except ImportError:
    print("Sin widgets: modifica los argumentos de simular() y vuelve a ejecutar.")
    simular()
else:
    widgets.interact(simular,
        producidas=widgets.IntSlider(value=1000, min=0, max=2000, step=50),
        rechazo_pct=widgets.FloatSlider(value=5, min=0, max=20, step=0.5),
        horas=widgets.FloatSlider(value=8, min=1, max=12, step=0.5),
        operarios=widgets.IntSlider(value=4, min=1, max=10))
```

## 16. Exportar resultados y comunicar una decisión
El archivo de detalle permite auditar registros y el resumen responde preguntas gerenciales. Exportar conserva datos, pero también necesitas documentar fórmulas, filtros y supuestos. En Colab descarga los archivos desde el panel de archivos; son temporales dentro del entorno.


### Ejecución 20 · Exportar y entregar el análisis

**Haz esto:** Ejecuta al terminar los cálculos. Abre el panel de archivos de Colab y actualiza su lista si hace falta.

**Debes ver:** Aparecen detalle_indicadores.csv, resumen_por_linea.csv e indicadores.png.

**Comprende:** Guardar archivos en el entorno temporal no los descarga al computador. Cada archivo debe descargarse antes de cerrar la sesión.

**Prueba y explica:** Descarga esos tres archivos y tu copia del notebook; agrega una conclusión con dos cifras, una limitación y una recomendación.


```python
df.to_csv("detalle_indicadores.csv", index=False, encoding="utf-8-sig")
por_linea.to_csv("resumen_por_linea.csv", index=False, encoding="utf-8-sig")
print("Guardados: detalle_indicadores.csv, resumen_por_linea.csv e indicadores.png")
```

### Modelo de conclusión fundamentada
La línea A produjo más unidades y tuvo mayor calidad global; la línea B obtuvo mayor productividad laboral en estos datos. Recomendamos investigar los turnos de menor calidad de cada línea y comprobar producto, condiciones, horas reales y registro de defectos antes de atribuir causas. Una dotación menor no demuestra que reducir personal aumente la productividad real.

**Actividad de 5 minutos:** escribe cuatro frases: hallazgo con cifra y unidad, comparación, limitación y acción verificable. Evita «la línea B es mejor» sin nombrar el indicador.

## 17. Reto integrador · comité de producción
En equipos de tres: analista, responsable de operaciones y auditor. Cambien de rol a mitad del trabajo.

1. Ejecuten el notebook desde un kernel limpio.
2. Agreguen un séptimo día para cada línea con datos coherentes y expliquen su elección.
3. Verifiquen claves, faltantes, rangos y unidades.
4. Calculen indicadores diarios, por línea y globales mediante razones de sumas.
5. Identifiquen dos registros prioritarios y expliquen el criterio.
6. Comparen un escenario con menor rechazo sin alterar los datos originales.
7. Presenten un gráfico, dos hallazgos, una limitación y una recomendación.
8. Entreguen notebook ejecutado, CSV de detalle, CSV resumen y conclusión de 150–200 palabras.

**Extensión:** incorporen costo por unidad defectuosa con un supuesto explícito. Calculen pérdida estimada y separen lo medido de lo supuesto. No presenten esa estimación como costo contable real.

### Rúbrica (100 puntos)
| Criterio | Puntos | Evidencia de logro |
|---|---:|---|
| Entorno y reproducibilidad | 10 | Ejecuta de arriba abajo sin dependencias ocultas |
| Fundamentos | 20 | Variables, condiciones, ciclo y función aplicados y explicados |
| Validación | 20 | Detecta inválidos y justifica el tratamiento |
| Indicadores | 25 | Fórmulas, unidades y agregaciones correctas |
| Gráfico y análisis | 15 | Gráfico legible, cifras coherentes, limitaciones |
| Comunicación y colaboración | 10 | Recomendación sustentada y roles documentados |

Para cada criterio: evidencia completa y correcta = 100 % de sus puntos; parcial con errores menores = 60 %; intento con errores sustantivos = 30 %; sin evidencia = 0 %. La prioridad es explicar, no memorizar sintaxis.


## 18. Autoevaluación y cierre
Responde antes de abrir las soluciones.
1. ¿Qué diferencia hay entre `=` y `==`?
2. ¿Qué tipo devuelve `input()`?
3. ¿Qué elementos produce `range(2, 5)`?
4. ¿En qué se diferencian `print` y `return`?
5. ¿Qué hace `np.array([1, 2]) * 2`?
6. ¿Cómo filtras una tabla con dos condiciones?
7. ¿Por qué no promediar directamente porcentajes de calidad?
8. ¿Cómo reportas calidad cuando no hay producción?
9. ¿Qué representa `horas × operarios` en este caso?
10. ¿Reiniciar el kernel borra el texto guardado del notebook?
11. ¿Qué riesgo hay en una unión con claves duplicadas?
12. ¿Mayor producción implica mayor productividad?

<details><summary>Respuestas razonadas</summary>

1. Asignación frente a comparación.
2. Texto (`str`), que se convierte según el significado esperado.
3. 2, 3 y 4; el límite superior se excluye.
4. Mostrar frente a devolver para reutilizar.
5. Un arreglo `[2, 4]` mediante multiplicación elemento a elemento.
6. `df.loc[(condicion1) & (condicion2)]`, con paréntesis.
7. Los volúmenes pueden diferir; divide las sumas.
8. No definida/ausente, sin inventar 0 % o 100 %.
9. Horas-persona si todos trabajan la duración indicada.
10. No; elimina el estado de ejecución en memoria.
11. Multiplicar filas e inflar agregaciones.
12. No; productividad relaciona resultado y recurso consumido.

</details>

### Ticket de salida
Completa: «Antes pensaba…; ahora puedo…; todavía necesito practicar…». Explica sin código por qué la calidad global requiere ponderación.

### Glosario rápido
**Kernel:** proceso que ejecuta las celdas. **Variable:** nombre asociado a un valor. **Booleano:** verdadero/falso. **Iteración:** una repetición. **Función:** operación reutilizable con entradas y salida. **Vectorizar:** operar sobre un arreglo. **DataFrame:** tabla con índice y columnas. **NaN:** ausencia numérica. **Agregación:** resumen de varios registros. **Indicador:** medida con definición y unidad. **Reproducibilidad:** obtener el resultado con los mismos datos, pasos y entorno.

### Consulta oficial para seguir aprendiendo
- [Tutorial de Python en español](https://docs.python.org/es/3/tutorial/)
- [Instalación de JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
- [Preguntas frecuentes de Google Colab](https://research.google.com/colaboratory/faq.html)
- [NumPy para principiantes](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Tutoriales de pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)

El desarrollo pedagógico, los ejercicios y el caso son originales. Las referencias apoyan la consulta de sintaxis y entornos; no sustituyen la práctica guiada.
