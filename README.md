
!image[https://github.com/ClaraGallardo/Final-Proyect/blob/main/image/_e892beb1-ce74-4650-a16d-0ebd744866fd.jpeg]

1. Descarga de datos https://inclasns.sanidad.gob.es/main.html'  🆗
2. Obtengo excel y muevo de descargas a data 🆗
3. Estudio excel  y limpieza. 🆗





Creaciónd e funciones para limpiar todos los xls de golpe.

df1 = df1.drop(df1.tail(3).index) # BORRAR LAS TRES ULTIMAS FILAS , OLO TODOS LO TIENEN ¡¡
dato esta en df.iloc[3:, 1:]

quitar froze list = df.reset_index()

subcolumnas=test.index.names

- Comprobamos si el dataframe tiene subcolumnas

if len(subcolumnas) >0:

  print("El dataframe tiene subcolumnas") # para hacer la funcion de limpieza, añadir df.reset_index()

else:

  print("El dataframe no tiene subcolumnas")

- Ojo todo es objeto hay que cambiarlo a numérico
- Incidencia de tuberculosis por 100 000 hab. no sale bien este tipo de tablas (REGION,AÑOS,TOTAL)

Añadir a tablas id por comunidad y crear tabla con id

4. CREAR SQL:

Automatizar proceso 🤔

- Columna id en algunas tablas como float ojo si no tienen el mismo formato te tira para atras
- subir primero tabla id para que se creen las primary key, si no, las foreign dan error al no tener columna de referencia

DREAMLIT :

- Intertar crear un chat para interactuar con los filtros, ej: dime donde se produjeron el mayor numero de accidentes de tráfico.

ESTRUCTURA CARPETAS:

proyecto/
│
├── data/                  # Carpeta para almacenar los datos
│   ├── raw/               # Datos sin procesar
│   ├── processed/         # Datos procesados
│   └── external/          # Datos externos (si los hay)
│
├── notebooks/             # Jupyter notebooks
│   ├── exploracion.ipynb  # Notebook de exploración de datos
│   └── limpieza.ipynb     # Notebook de limpieza de datos
│
├── scripts/               # Scripts de Python
│   ├── extraccion.py      # Script para la extracción de datos
│   ├── limpieza.py        # Script para la limpieza de datos
│   ├── almacenamiento.py  # Script para el almacenamiento de datos
│   ├── sql.py             # Script para la interacción con SQL
│   └── visualizacion.py   # Script para la visualización de datos
│
├── app/                   # Código de la aplicación
│   ├── main.py            # Script principal de Streamlit
│   └── requirements.txt    # Archivo con las dependencias del proyecto
│
├── tests/                 # Pruebas unitarias y de integración
│   ├── test_extraccion.py # Pruebas para el módulo de extracción
│   ├── test_limpieza.py   # Pruebas para el módulo de limpieza
│   └── test_sql.py        # Pruebas para el módulo de SQL
│
├── config/                # Configuración del proyecto
│   ├── config.yaml        # Archivo de configuración
│   └── logging.conf       # Configuración del registro (logging)
│
├── .gitignore             # Archivo de gitignore
├── README.md              # Documentación del proyecto
├── requirements.txt       # Archivo con las dependencias del proyecto
├── LICENSE                # Licencia del proyecto
└── .git/                  # Carpeta git (control de versiones)
