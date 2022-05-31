# https://admin.cerofilas.gob.cl/
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SELENIUM_GRID_HOST = os.environ.get('SELENIUM_GRID_HOST', 'localhost')

driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://%s:4444" % SELENIUM_GRID_HOST
        )

driver.get("https://admin.cerofilas.gob.cl/")
print(driver.title)
titulo = driver.find_element(By.CLASS_NAME, "title")
print("*"*50)
print(titulo)
print("*"*50)
print(driver.current_url)
driver.close()