from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time  

PATH = "driver/chromedriver.exe"
driver = webdriver.Chrome()

# PAGINA PPAL SELECCION datos DE SCRAPEO:

def descarga_tablas(url):
    
    '''
    Descarga de tablas(Excel)
    '''

    PATH = "driver/chromedriver.exe"
    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(4)   

    #  SELECCION CAMPOS  

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
            # Descargar el archivo Excel
            download_button = driver.find_element_by_xpath(f'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[{i}]/div/div/div[2]/span[2]')
            download_button.click()

            # Obtener el nombre del archivo Excel y añadirlo a la lista
            excel_name = driver.find_element_by_xpath(f'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[{i}]/div/div/table/caption').text
            excel_names.append(excel_name)

            # Hacer clic en el botón "Siguiente"
            next_button = driver.find_element_by_xpath(f'/html/body/div[1]/div[4]/div/div[4]/div[2]/ul/li[{i+1}]/a')
            next_button.click()

        except NoSuchElementException:
            # Si no se encuentra el botón "Siguiente", salir del bucle
            break

    # Devolver la lista de nombres de archivos Excel
    return excel_names
