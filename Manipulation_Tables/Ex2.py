#import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(4)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(4)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(4)
driver.close()