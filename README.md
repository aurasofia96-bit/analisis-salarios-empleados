# Reporte de Datos Laborales y Salarios

Programa en Python que automatiza la recolección, clasificación y análisis estadístico de datos de trabajadores por consola.

## Descripción

Este programa optimiza el procesamiento de datos del personal administrativo. Solicita de forma consecutiva el salario, los años de antigüedad y la edad de 10 trabajadores, valida que la información sea coherente en tiempo de ejecución, clasifica al personal en tres grupos distintos según su experiencia y calcula automáticamente métricas clave como promedios salariales, sumas totales e incrementos porcentuales condicionales por cada grupo.

## Características

- Validación estricta ante entradas de salarios, edades o antigüedades inválidas.
- Clasificación automática de los trabajadores en Grupos A, B o C según su antigüedad.
- Cálculo dinámico de promedios de edad, sumas salariales y porcentajes de incremento.
- Presentación de resultados ordenados por grupo en la terminal.

## Tecnologías

- Python 3

## Cómo ejecutar

1. Clona este repositorio o descarga el archivo.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
python reporte_horas.py
```

## Lo que practiqué

En este proyecto utilicé:

- Estructuras de datos complejas mediante listas anidadas (matrices de acumulación).
- Control de flujo combinado usando ciclos fijos for junto con ciclos while dedicados a la validación de errores.
- Lógica condicional múltiple (if, elif, else) para segmentación de datos y asignación de porcentajes.
- Operadores aritméticos y funciones nativas de redondeo de datos (round()).

### Próximas mejoras

* **Funciones independientes:** Para separar la captura de datos, los cálculos y la muestra de resultados en bloques limpios.
* **Control de errores:** Para evitar que el programa falle si el usuario ingresa texto en lugar de números.
* **Carga de datos dinámica:** Para permitir que la lista de trabajadores se lea automáticamente desde un archivo de Excel o CSV en lugar de pedirlos uno a uno.

## Estado del proyecto

Proyecto finalizado como práctica de Python.
