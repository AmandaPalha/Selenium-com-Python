from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

def find_by_text(drive, tag, text):
    """
    Encontrar o elemento com o texto 'text'.
    drive = instância do browser
    tag = onde o texto será procurado
    text = conteúdo que deve estar na tag
    """
    elementos = drive.find_elements(By.TAG_NAME, tag) # lista
    for elemento in elementos:
        if elemento.text == text:
             return elemento

def find_by_href(drive, link):
    """
    Encontrar o elemento 'a' com  'link'.
    drive = instância do browser
    link = link a ser buscado em todas as tags âncora
    """
    elementos = drive.find_elements(By.TAG_NAME, 'a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

def give_href_by_text(drive, tag, text):
    elementos = drive.find_elements(By.TAG_NAME, tag) # lista
    for elemento in elementos:
        if elemento.text == text:
            return elemento.get_attribute('href')

def give_text_by_href(drive, link):
    elementos = drive.find_elements(By.TAG_NAME, 'a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento.text

drive = Firefox()
url = 'http://selenium.dunossauro.live/aula_04_a.html'
drive.get(url)

# usando find_by_text
elem_ddg = find_by_text(drive, 'a', 'DuckDuckGo')
link_ddg = elem_ddg.get_attribute('href') # pega link do elemento com texto
print(link_ddg)

# usando find_by_href
elem_ddg2 = find_by_href(drive, 'ddg')
text_ddg = elem_ddg2.text # pega texto do elemento com link
print(text_ddg)

print(give_href_by_text(drive, 'a', 'DuckDuckGo'))
print(give_text_by_href(drive, 'ddg'))

drive.quit()
