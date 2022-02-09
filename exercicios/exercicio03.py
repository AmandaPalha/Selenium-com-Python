from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from time import sleep

drive = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_03.html'
drive.get(url)
timeout = 15

""" Etapa 1 """
sleep(2)
main = drive.find_element(By.ID, 'main')

comecar = main.find_element(By.TAG_NAME, 'a')
comecar.click()

""" Etapa 2 """
sleep(2)
main = drive.find_element(By.ID, 'main')

p_lista = main.find_elements(By.TAG_NAME, 'p')[-1].text.split()
produto = int(p_lista[0]) * int(p_lista[2])

anchors2 = main.find_elements(By.TAG_NAME, 'a')
for anchor2 in anchors2:
    if int(anchor2.text) != produto:
        anchor2.click()
        break

""" Etapa 3 """
sleep(30)
main = drive.find_element(By.ID, 'main')

anchors3 = main.find_elements(By.TAG_NAME, 'a')
for anchor3 in anchors3:
    if anchor3.text == drive.title:
        anchor3.click()
        break

""" Etapa 4 """
sleep(2)
main = drive.find_element(By.ID, 'main')

anchors4 = main.find_elements(By.TAG_NAME, 'a')
pars_url = urlparse(drive.current_url)
for anchor4 in anchors4:
    if anchor4.text == pars_url.path[1:]: # path sem /
        anchor4.click()
        break

""" Etapa 5 """
sleep(2)
drive.refresh()
sleep(2)

main = drive.find_element(By.ID, 'main')
pre = main.find_element(By.TAG_NAME, 'pre')
if 'unicórnio' in pre.text.split():
    print('Parabéns! Você completou o jogo.')
else:
    print('Ops! Algo deu errado...')
