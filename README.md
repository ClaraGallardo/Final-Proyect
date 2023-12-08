![Vista previa del proyecto](https://github.com/ClaraGallardo/Final-Proyect/blob/main/image/_e892beb1-ce74-4650-a16d-0ebd744866fd.jpeg)


# INDISALUD⚕️

Este repositorio se centra en la recopilación, análisis y visualización de indicadores de salud clave para proporcionar una comprensión integral del estado de salud de una población. Los indicadores de salud son medidas cuantificables que nos permiten evaluar y monitorear diversos aspectos de la salud pública, desde tasas de enfermedades específicas hasta factores determinantes del bienestar.

El objetivo principal de este proyecto es proporcionar a los usuarios una herramienta eficaz para interpretar y comunicar datos de salud de manera clara y accesible. Ya sea que seas un profesional de la salud, un investigador, o simplemente alguien interesado en comprender las tendencias y desafíos en el ámbito de la salud, este repositorio te brindará las herramientas necesarias para explorar, analizar y sacar conclusiones a partir de los indicadores de salud proporcionados.

A través de visualizaciones interactivas, análisis detallados y documentación clara, esperamos que este proyecto contribuya significativamente a la comprensión y mejora de la salud pública. ¡Explora, contribuye y únete a nosotros en este esfuerzo por hacer que la información de salud sea más accesible y valiosa para todos!

## Procedimiento ⚒️:

1. Extracción con Selenium:

Utilizando Selenium, se automatiza la navegación a través de la interfaz web del sitio para acceder a las secciones relevantes que contienen la información de interés.

2. Descarga de Archivos Excel:

Se identifican los enlaces o botones que permiten la descarga de archivos Excel desde el sitio web. Selenium se utiliza para simular las interacciones necesarias (clics, formularios, etc.) que activan las descargas de archivos.

3. Almacenamiento Local:

Los archivos Excel descargados se almacenan localmente en el sistema de archivos para su posterior procesamiento.

4. Transformación de Datos:

Se utiliza una biblioteca de manipulación de datos, como pandas en Python, para cargar y transformar los datos de los archivos Excel según sea necesario además de la creación de funciones específicas para los procesos. Esto puede incluir la limpieza de datos, la conversión de formatos y la selección de columnas relevantes.

5. Creación de la Base de Datos SQL:

Se emplea SQL para crear una base de datos que refleje la estructura deseada para los datos extraídos. Se definen tablas que representan las entidades y relaciones relevantes.

6. Carga de Datos en la Base de Datos:

Utilizando comandos SQL o herramientas específicas desde Python, se cargan los datos transformados desde los archivos Excel en la base de datos SQL recién creada. Esto implica la inserción de registros en las tablas correspondientes.


Este proceso automatizado garantiza la obtención eficiente y precisa de los datos del sitio web(https://inclasns.sanidad.gob.es/main.html), seguido de su preparación y almacenamiento en una base de datos SQL, lo que facilita su análisis y consulta posterior.

## EDA:

Se realiza un analisis exploratorio de los datos oara comprender y explorar la naturaleza d elos datos recopilados.
Al trabajar con muhcas variables se decide agruparlas para un mejor manejo y estudio posterior. Las categorías o grupos son:

1. Esperanza de vida
2. Morbilidad
3. Mortalidad
4. Estilo de vida
5. Region
   

## Estructura de repositorio 📂:

proyecto/
│
├── data/                  # Carpeta para almacenar los datos
│   ├── raw/               # Datos sin procesar
│   ├── processed/         # Datos procesados
│ 
│
├── notebooks/             # Jupyter notebooks
│   
│
├── scripts/               # Scripts de Python
│
├── tests/                 # Pruebas unitarias y de integración
│   ├── test_extraccion.py # Pruebas para el módulo de extracción
│   ├── test_limpieza.py   # Pruebas para el módulo de limpieza
│   └── test_sql.py        # Pruebas para el módulo de SQL
│
├── .gitignore             # Archivo de gitignore
├── README.md              # Documentación del proyecto
├── LICENSE                # Licencia del proyecto

Este repositorio sigue una estructura organizada para facilitar el desarrollo y la comprensión del proyecto.

## Técnologías usadas 👩‍💻:

Selenium:

Utilizado para la automatización de la navegación web y la interacción con la interfaz del sitio https://inclasns.sanidad.gob.es/main.html.

Python:

Lenguaje de programación principal para la implementación de la automatización y la manipulación de datos.

pandas:

Biblioteca de Python utilizada para la manipulación y transformación eficiente de datos, especialmente en la fase de procesamiento de archivos Excel.

SQL:

Lenguaje de consultas utilizado para la creación de la base de datos y la manipulación de datos almacenados.
Herramientas de Desarrollo en Python:

Editores de código, entornos virtuales y otras herramientas utilizadas para el desarrollo y ejecución del código Python.
Gestor de Base de Datos SQL (MySQL Workbench):

Utilizado para la creación de la base de datos y la gestión del almacenamiento y recuperación de datos.
Sistema de Control de Versiones (GitHub):

Empleado para el seguimiento de cambios en el código fuente y la colaboración en el desarrollo del proyecto.
