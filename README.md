1. Descarga de datos https://inclasns.sanidad.gob.es/main.html'  🆗
2. Obtengo excel y muevo de descargas a data 🆗
3. Estudio excel :

df1 = df1.drop(df1.tail(3).index) # BORRAR LAS TRES ULTIMAS FILAS , OLO TODOS LO TIENEN ¡¡
dato esta en df.iloc[3:, 1:]

4. LIMPIEZA :

df1 = df1.drop(df1.tail(3).index) # BORRAR LAS TRES ULTIMAS FILAS , OLO TODOS LO TIENEN ¡¡
dato esta en df.iloc[3:, 1:] 

quitar froze list = df.reset_index()

subcolumnas=test.index.names

- Comprobamos si el dataframe tiene subcolumnas

if len(subcolumnas) >0:

  print("El dataframe tiene subcolumnas") # para hacer la funcion de limpieza, añadir df.reset_index()

else:

  print("El dataframe no tiene subcolumnas")

5. CREAR SQL:
6. DREAMLIT :
