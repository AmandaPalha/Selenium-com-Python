from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = Firefox() # cria e inicializa o objeto do navegador
timeout = 5

url = 'https://curso-python-selenium.netlify.app/aula_03.html' # armazena em 'url' a url que será aberta
browser.get(url) # abre 'url' em 'browser'

try:
    a_pres = EC.presence_of_element_located((By.TAG_NAME, 'a'))
    a = WebDriverWait(browser, timeout).until(a_pres)
except TimeoutException:
    print("Timeout.")

    """
    EC (expected_conditions) estabelece uma condicional e retorna um bool.
    No caso, a condicional é a presença no DOM do WebElement com tag 'a',
    pelo método presence_of_element_located(localizador). Armazena o bool em a_pres.
    WebDriverWait faz o browser esperar, até o limite de timeout, e o método until
    retorna o WebElement assim que a_pres para de retornar False.
    print(f'texto de a: {a.text}')
    """

for clique in range(0, 11):
    ps = browser.find_elements(By.TAG_NAME, 'p')
    # armazena uma lista de todos os elementos com tag 'p' em ps.
    a.click()
    print(f'Valor de p: {ps[-1].text}, para clique {clique}')
    print(f'Os valores são iguais? {int(ps[-1].text) == clique}')
    # o módulo .text retorna uma string

browser.quit()
