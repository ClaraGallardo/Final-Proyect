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
- Incidencia de tuberculosis por 100 000 hab. no sale bien este tipo de tablas

5. CREAR SQL:
   Automatizar proceso 🤔 , puede que creando un método o clase me haga la estructura de las tablas en SQL y me carge los datos?
6. DREAMLIT :

- Intertar crear un chat para interactuar con los filtros, ej: dime donde se produjeron el mayor numero de accidentes de tráfico
