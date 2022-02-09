from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

"""
1. Pegar todos os links de aulas
    dict: {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    Achar a url do Exercício 3 e ir até lá
"""

drive = Firefox()
url = 'http://selenium.dunossauro.live/aula_04.html'
drive.get(url)

def get_links(browser, elemento): # dicionário
    """
    Pega todos os links dentro de um elemento.
    browser = instância do navegador
    elemento = WebElement ('aside', 'main', 'body', 'ul', etc)
    """
    resultado = {}
    element = browser.find_element(By.TAG_NAME, elemento)
    anchors = element.find_elements(By.TAG_NAME, 'a')
    for anchor in anchors:
        resultado[anchor.text] = anchor.get_attribute('href')
    return resultado


""" Parte 1 """
sleep(2)

aulas = get_links(drive, 'aside')
pprint(aulas)


""" Parte 2 """

exercicios = get_links(drive, 'main')
pprint(exercicios)

drive.get(exercicios['Exercício 3'])
