from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from urllib.parse import parse_qsl # parseia uma query em string e retorna uma lista de tuplas
from json import loads
from time import sleep

drive = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_04.html'
drive.get(url)
sleep(2)

def preencher(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()

valores = {'nome': 'João Cézar',
            'email': 'joaocezar@gmail.com',
            'senha': 'not4pass',
            'telefone': '(11)987654321'
            }

preencher(drive, **valores)
sleep(2)

nova_query = parse_qsl(urlparse(drive.current_url).query, encoding='utf-8')[:-1] # retorna uma lista de tuplas
dict_query = {nova_query[0][0]: nova_query[0][1],
                nova_query[1][0]: nova_query[1][1],
                nova_query[2][0]: nova_query[2][1],
                nova_query[3][0]: nova_query[3][1]
                } # contrói dicionário transformando cada tupla em {chave: valor}
print(f'Query da url atualizada:\n{dict_query}')

dict_result = loads(drive.find_element(By.TAG_NAME, 'textarea').text.replace('\'', '\"').replace('+', ' '))
print(f'Resultado impresso em página:\n{dict_result}')

try: # verifica se os valores exibidos em 'result' conferem com input
    assert dict_result == dict_query
    print('Conferência retornou identidade.')
except AssertionError:
    print('Conferência retornou divergência.')
except:
    print('Não foi possível realizar a validação')

drive.quit()
