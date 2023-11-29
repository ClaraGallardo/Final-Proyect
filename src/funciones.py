from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time  

PATH = "driver/chromedriver.exe"
driver = webdriver.Chrome()

# PAGINA PPAL SELECCION datos DE SCRAPEO:

def descarga(url):
    
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