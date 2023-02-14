import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
Check_selected = driver.find_element(By.ID, 'checkbox2').is_selected()
print(Check_selected)
time.sleep(4)
Check_Button_Enable = driver.find_element(By.ID, 'but1').is_enabled()
print(Check_Button_Enable)
time.sleep(4)
Check_Button_Displayed = driver.find_element(By.ID, 'hbutton').is_displayed()
print(Check_Button_Displayed)
time.sleep(4)
driver.close()