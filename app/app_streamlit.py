import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
from sqlalchemy import True_, create_engine

# # Configuración de la conexión a la base de datos (cambia según tus datos)
DATABASE_URL = "mysql://root:Cascos1993.@localhost:3306/indisalud"
engine = create_engine(DATABASE_URL)

# # Consulta SQL para obtener las categorías desde la tabla en la base de datos
query = "SELECT Categoría FROM categoría;"
categorias = pd.read_sql(query, engine)['Categoría'].tolist()


# Configuración de la página
st.set_page_config(page_title="IndiSalud", page_icon="🩺", layout="wide")

# Animación del título
st.title("IndiSalud")

# Logo e introducción image\logo.jpeg
st.image("../image/logo.jpeg", use_column_width=True, caption="Tu Logo")

st.write("""
Bienvenido a IndiSalud, tu fuente de información sobre indicadores de salud en España. 
Aquí encontrarás información sobre diversos aspectos relacionados con la salud en distintas categorías y comunidades autónomas.
""")

# Categorías en el lado derecho
st.sidebar.title("Categorías")
categoria_seleccionada = st.sidebar.selectbox("Selecciona una categoría", categorias)

# Aquí puedes agregar más secciones según sea necesario, como visualizaciones de datos, gráficos, etc.

# Información específica de la categoría seleccionada (por ejemplo, desde la base de datos)
st.write(f"### Información sobre la categoría: {categoria_seleccionada}")

