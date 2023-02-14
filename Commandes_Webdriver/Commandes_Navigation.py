import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium")
time.sleep(4)
driver.get("https://www.google.ca")
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()
time.sleep(4)
driver.refresh()
time.sleep(4)
driver.close()