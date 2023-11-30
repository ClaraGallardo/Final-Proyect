from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time  

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
