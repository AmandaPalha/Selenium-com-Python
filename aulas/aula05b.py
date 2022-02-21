from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

drive = Firefox()
url = 'http://selenium.dunossauro.live/aula_05_b.html'
drive.get(url)

topico = drive.find_elements(By.CLASS_NAME, 'topico') # lista
linguagens = drive.find_elements(By.CLASS_NAME, 'linguagens') # lista

for linguagem in linguagens:
    print(
        (linguagem.find_element(By.TAG_NAME, 'h2').text,
         linguagem.find_element(By.TAG_NAME, 'p').text
         )
    )
"""
Atributos globais:
    id
    class
    autofocus
    acesskey
    title
    hidden
"""

drive.quit()
