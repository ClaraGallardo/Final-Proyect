tabla1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[1]/div/div/table').text

tabla1

time.sleep(1)

x_path = '/html/body/div[1]/div[4]/div/div[4]/div[2]/ul/li[2]'  

driver.find_element(By.XPATH, x_path).click()

time.sleep(3)

tabla2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[2]/div/div/table').text 

tabla2

time.sleep(1)

x_path = '/html/body/div[1]/div[4]/div/div[4]/div[2]/ul/li[3]'  

driver.find_element(By.XPATH, x_path).click()

time.sleep(3)

tabla3 = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[3]/div/div/table').text 

tabla3

time.sleep(1)

x_path = '/html/body/div[1]/div[4]/div/div[4]/div[2]/ul/li[4]'  
driver.find_element(By.XPATH, x_path).click()

time.sleep(3)

tabla4 = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[4]/div[2]/div[4]/div/div/table').text 

tabla4