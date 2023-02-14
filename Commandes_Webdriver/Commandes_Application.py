#commandes lier a l'application sous test
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium")
titre_page = driver.title
print(titre_page)
URL_page = driver.current_url
print(URL_page)
Code_source = driver.page_source
print(Code_source)
time.sleep(4)
driver.close()