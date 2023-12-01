import mysql.connector
from sqlalchemy import create_engine, text

import pandas as pd

def conection_to_SQL(user,password,host,database = None):

    conexion = mysql.connector.connect(user = user, password = password, host = host, database = database)
    cursor = conexion.cursor()
    
    return cursor 

def add_table(file,key_type,database,password):
    
    try:
        
        try:
            
            df = pd.read_csv(f'../data/{file}.csv')
            
        except:
            
            return print(f"Error: couldn't find {file}.csv in ../data/")
            
    except:
        
        engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/{database}', echo=True)
        
        df.to_sql(file, con=engine, if_exists='append', index=False) # type: ignore

        if key_type == 'primary':
            
            with engine.connect() as con:
                con.execute(text(f'ALTER TABLE `{file}` ADD PRIMARY KEY (`id`)'))
                            
        else:
            
            with engine.connect() as con:
                con.execute(text(f'ALTER TABLE `{file}` ADD FOREIGN KEY (`id`) REFERENCES `id`(`id`)'))
                
                