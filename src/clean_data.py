from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time  

import pandas as pd

def download_tables(url):
    
    """
    Automates the download of tables (Excel) from the specified website using Selenium.

    Parameters:
    - url (str, optional): URL of the website containing the tables to download. 
      input = "https://inclasns.sanidad.gob.es/main.html".

    Returns:
    - excel_names (list): List of names of the downloaded Excel files.
    - num_files (int): Number of Excel files downloaded.

    Requires the use of Selenium and ChromeDriver for browser automation.

    Example:
    ```python
    excel_names, num_files = download_tables(url)
    ```

    Note:
    Make sure you have the following packages installed:
    - Selenium: pip install selenium
    - ChromeDriver: Ensure that ChromeDriver is installed and its path is specified in the 'PATH' variable.

    Additional Requirements:
    - This function is specifically designed for the website "https://inclasns.sanidad.gob.es/main.html".
    - Make sure the ChromeDriver executable is available in the specified 'PATH' or provide the correct path in the 'PATH' variable.

    Warning:
    This function may break if the structure of the website changes.

    Returns a list of file names and the total number of downloaded Excel files.

    Usage:
    ```python
    excel_names, num_files = download_tables()
    ```

    Note:
    The function may not work as expected if the structure of the website changes.
    """


    PATH = "driver/chromedriver.exe"
    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(4)   

    x_path = '//*[@id="aceptarCookie"]'    # Aceptar cookies

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="ui-id-1"]/span[2]'   # Bienestar

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="ui-id-3"]/span[2]'   # Enfermedad

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="ui-id-5"]/span[2]'   # Mortalidad

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="ui-id-7"]/span[2]'   # Determinantes socioeconomicos 

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="ui-id-9"]/span[2]'   # Estilo de vida

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="ui-id-11"]/span[2]'   # Estilo de vida

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="ui-id-26"]'   # despleglable Años

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="year"]/label[28]'   # 2017 

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="year"]/label[29]'   # 2018  //*[@id="year"]/label[29]

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="year"]/label[30]'   # 2019 //*[@id="year"]/label[30]

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="year"]/label[31]'   # 2020 //*[@id="year"]/label[31]

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="year"]/label[32]'   # 2021 //*[@id="year"]/label[32]

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="year"]/label[34]' #

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)

    x_path = '//*[@id="selection"]/a[1]'   # Comenzar análisis

    driver.find_element(By.XPATH, x_path).click()

    time.sleep(4)
    
    excel_names = [] 
    
    i = 1
    
    while True:
        try:
            
            time.sleep(2)
            
            # Descargar el archivo Excel
            download_button = driver.find_element(By.XPATH,f'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[{i}]/div/div/div[2]/span[2]')
            download_button.click()
            
            time.sleep(1)

            # Obtener el nombre del archivo Excel y añadirlo a la lista
            excel_name = driver.find_element(By.XPATH,f'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[{i}]/div/div/table/caption').text
            excel_names.append(excel_name)
            
            time.sleep(1)

            # Hacer clic en el botón "Siguiente"
            next_button = driver.find_element(By.XPATH,f'/html/body/div[1]/div[4]/div/div[4]/div[2]/ul/li[{i+1}]/a')
            next_button.click()
            
            i+=1
            
            time.sleep(2)

        except NoSuchElementException:
            # Si no se encuentra el botón "Siguiente", salir del bucle
            break

    return excel_names, len(excel_names)


def move_excel(origen, destino):
    """
    Move Excel files from a source directory to a destination directory.

    Parameters:
    - origin (str): Path of the source directory containing the Excel files to move.
    - destination (str): Path of the destination directory where the Excel files will be moved.

    Returns:
    None

    Example:
    ```python
    move_excel("downloads", "excel_files")
    ```

    Note:
    - Make sure the source directory contains files with the ".xls" extension.
    - If the destination directory does not exist, it will be created automatically.

    Warning:
    - This function copies the files from the source to the destination, so if a file with the same name already exists in the destination, it will be overwritten.
    - Information about the copied files and any potential errors during execution is printed.

    """
    
    import os
    import shutil
    
    try:
        
        archivos_descargas = os.listdir(origen)
                
        archivos_excel = [archivo for archivo in archivos_descargas if archivo.endswith(".xls")]
        print(archivos_excel)
        
        if not os.path.exists(destino):
            os.makedirs(destino)

        for archivo_excel in archivos_excel:
            ruta_origen = os.path.join(origen, archivo_excel)
            ruta_destino = os.path.join(destino, archivo_excel)
            shutil.copyfile(ruta_origen, ruta_destino)
            print(f"Archivo {archivo_excel} copiado a {destino}")

    except Exception as e:
        print(f"Error al extraer archivos Excel: {e}")
        


def clean_columns(df):
    
    df_copy = df.copy()
    
    years = df_copy.iloc[1].values
    genders = df_copy.iloc[2].values
    
    new_columns = []
    current_year = None
    
    #SEPARACION AÑOS Y GÉNERO
    
    for i in range(len(years)):
        if pd.isna(years[i]):
            new_columns.append(f'{current_year}_{genders[i]}')
        else:
            current_year = years[i]
            new_columns.append(f'{current_year}_{genders[i]}')
    
    df_copy.columns = new_columns
    
    df_copy = df_copy.iloc[3:]
    
    df_copy.set_index(df_copy.columns[0], inplace=True)
    
    # Eliminar las tres últimas filas si tienen más de un 90% de valores nulos, hay algunos excel que tienen nulos al final como observaciones
    
    rows_to_drop = df_copy.tail(3).index[df_copy.tail(3).isnull().mean(axis=1) > 0.9]
    df_copy = df_copy.drop(rows_to_drop)
    
    # QUITAR MULTIINDEX
    
    df_copy = df_copy.reset_index()
      
    df_copy.rename(columns={'None_nan': 'Region'}, inplace=True)
      
    return df_copy

def create_df(df):
    
    df_new = pd.DataFrame(columns=['Region', 'Año', 'Hombre', 'Mujer', 'Total'])
    
    # dependiendo del df tenemos diferentes años:
    
    years = set(col.split('_')[0] for col in df.columns if '_' in col)  # cogemos año 
    
    for year in years:
        
        if f'{year}_Hombres' in df.columns and f'{year}_Mujeres' in df.columns and f'{year}_Total' in df.columns:
            
            df_year = df[['Region', f'{year}_Hombres', f'{year}_Mujeres', f'{year}_Total']].copy()
            df_year.columns = ['Region', 'Hombre', 'Mujer', 'Total']
            df_year['Año'] = year
            df_new = pd.concat([df_new, df_year], ignore_index=True)
            
    return df_new