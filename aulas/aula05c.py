from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

drive = Firefox()
url = 'http://selenium.dunossauro.live/aula_05_c.html'
drive.get(url)

"""
NAME é um atributo de formulário; todo imput tem um NAME
"""

def melhor_filme(browser, filme, email, telefone):
    browser.find_element(By.NAME, 'filme').send_keys(filme)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'enviar').click()

melhor_filme(drive,
            'Parasita',
            'emailteste@gmail.com',
            '(019)987654321'
            )
