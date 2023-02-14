#import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
#Recuperation du nb de ln et col d une table
nb_ligne=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(nb_ligne))
nb_col=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(nb_col))
#recupere la valeur d une celllule de la table
val_cell=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
print(val_cell.text)
#recuperer toutes les donnees du tableau
nb_lignes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
nb_cols=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
val_head=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
"""for h in range(1,len(val_head)+1):
    data_head=driver.find_element(By.XPATH,"//table[@name='BookTable']//th["+str(h)+"]").text
    print(data_head)
    time.sleep(3)"""
for r in range(2,nb_lignes+1):
    for c in range(1,nb_cols+1):
        data= driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='     ')
    print()
driver.close()