from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from pprint import pprint

drive = Firefox()
drive.get('https://rennerocha.github.io/xpath/')

title = drive.find_element(By.XPATH, '/html/head/title[.]') # '//title' busca todos 'title' a partir da raiz
print(title.text)
""" por que retorna vazio? """
print(drive.title) # retorna certo

h1_1 = drive.find_element(By.XPATH, '/html/body/div/div[1]/h1/a')
print(h1_1.text)

drive.close()
