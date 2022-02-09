from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

drive = Firefox()
timeout = 5

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
drive.get(url)

try:
    ancora_pres = EC.presence_of_element_located((By.TAG_NAME, 'a'))
    ancora = WebDriverWait(drive, timeout).until(ancora_pres)
except TimeoutException:
    print('O carregamento da página atingiu timeout.')

temp = drive.find_elements(By.TAG_NAME, 'p')[-1].text.split()
expect = temp[-1]

tentativas = 0
control = False
while control == False:
    ancora.click()
    temp = drive.find_elements(By.TAG_NAME, 'p')[-1].text.split()
    novo = temp[-1]
    tentativas += 1
    if novo == expect:
        print(f'Você ganhou! Acertou o número {novo} em {tentativas} tentativas!')
        control = True

drive.quit()
