from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

drive = Firefox()
timeout = 5

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
drive.get(url)

dict = {}
dict_final = {}

try:
    H1_pres = EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    titulo = WebDriverWait(drive, timeout).until(H1_pres)
except TimeoutException:
    print('O carregamento da página atingiu timeout.')

atributos = drive.find_elements(By.TAG_NAME, 'p')
for i in range(len(atributos)):
    atrib = atributos[i].get_attribute('atributo')
    dict.update({f'{atrib}': atributos[i].text})
    # hard code nas chaves porque não sei como extrair o valor de "atributo"

dict_final.update({f'{titulo.text}': dict})

print(dict_final)

drive.quit()
