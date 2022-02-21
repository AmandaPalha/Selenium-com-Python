from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads

drive = Firefox()
url = 'http://selenium.dunossauro.live/aula_05.html'
drive.get(url)
sleep(2)

def preencher(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()

valores = {'nome': 'Amanda',
            'email': 'amandateste@gmail.com',
            'senha': 'not4password',
            'telefone': '(12)987654321'
            }

preencher(drive, **valores) # ** descompacta o dicionário nos argumentos
"""
Resultado do click: url =
https://selenium.dunossauro.live/aula_05.html
?nome=Amanda
&email=amandateste%40gmail.com
&senha=not4password
&telefone=%2812%29987654321
&btn=Enviar%21#
    ? = query string
"""

sleep(2)

nova_url = urlparse(drive.current_url)
nova_query = nova_url.query.split('&')
print(f'Query de url atualizada:\n{nova_query[:-1]}\nInput:\n{valores}')

texto_result = drive.find_element(By.ID, 'result').text
dict_result = loads(texto_result.replace('\'', '\"'))
""" loads transforma a estrutura em uma string.
O replace resolve o problema de loads não reconhecer ', apenas "
"""

try: # verifica se os valores exibidos em 'result' conferem com input
    assert dict_result == valores
    print('Conferência retornou identidade.')
except AssertionError:
    print('Conferência retornou divergência.')
except:
    print('Não foi possível realizar a validação')

drive.quit()
