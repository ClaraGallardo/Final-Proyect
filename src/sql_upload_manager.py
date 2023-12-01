import mysql.connector
from sqlalchemy import create_engine, text

import pandas as pd

def add_table(file,key_type,database,password,folder):
    
    try:
        
        try:
            
            df = pd.read_csv(f'../data/{file}.csv')
            
        except:
            
            return print(f"Error: couldn't find {file}.csv in ../{folder}/")
            
    except:
        
        engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/{database}', echo=True)
        
        
        df.to_sql(file, con=engine, if_exists='append', index=False) # type: ignore

        if key_type == 'primary':
            
            with engine.connect() as con:
                con.execute(text(f'ALTER TABLE `{file}` ADD PRIMARY KEY (`id`)'))
            print(f"The table {file} has been successfully loaded into SQL with the associated {key_type} key.")
        
        else:
            
            with engine.connect() as con:
                con.execute(text(f'ALTER TABLE `{file}` ADD FOREIGN KEY (`id`) REFERENCES `id`(`id`)'))
            print(f"The table {file} has been successfully loaded into SQL with the associated {key_type} key.")    


def conection_to_SQL(usuario, clave, host, database=None):
    try:

        conexion = mysql.connector.connect(user=usuario, password=clave, host=host, database=database)

        cursor = conexion.cursor()

        print("Conexión a MySQL exitosa")
        
        return conexion, cursor

    except mysql.connector.Error as err:

        print(f"Error al conectar a MySQL: {err}")
        return None, None
    
def add_table_test(file,key_type,database,password,folder):
           
    df = pd.read_csv(f'../data/{file}.csv')        
        
    engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/{database}', echo=True)
    print(engine)
            
    df.to_sql(file, con=engine, if_exists='append', index=False)
        
    if key_type == 'primary':
            
        with engine.connect() as con:
             con.execute(text(f'ALTER TABLE `{file}` ADD PRIMARY KEY (`id`)'))
        print(f"The table {file} has been successfully loaded into SQL with the associated {key_type} key.")
        
    else:
            
        with engine.connect() as con:
            con.execute(text(f'ALTER TABLE `{file}` ADD FOREIGN KEY (`id`) REFERENCES `id`(`id`)'))
        print(f"The table {file} has been successfully loaded into SQL with the associated {key_type} key.")  