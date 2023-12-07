#Importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


print('\33[30;42m-=' * 40, '\33[m')
print(f'\33[1;30;42m{"AUTOMAÇÃO DE WHATSAPP":^80}', '\33[m')
print('\33[30;42m-=' * 40, '\33[0m')
print()
import database
database.login()
sleep(1)
print('--' * 10)
print('\33[1mIniciando...\33[0m')
try:
    service = Service(ChromeDriverManager().install())
    nav =  webdriver.Chrome(service=service)
    nav.get('https://web.whatsapp.com')
except PermissionError:
    print('\33[1;31mPermissão Negada, tente novamente mais tarde!\33[0m')
    raise
sleep(30)
print('-=' * 40)
print('\33[1;33mApós logar no whatsapp aperte ENTER para começar!\33[0m')
print('-=' * 40)
input()
sleep(1.2)

from selenium.webdriver.common.keys import Keys
import pyperclip
#Meu numero
nav.find_element('xpath', '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[3]/div').click()
sleep(0.4)
nav.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[1]/div/div[2]/div/div[1]/p').send_keys('(você)')
sleep(0.5)
meu_numero = nav.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/span[1]').text
meu_numero = meu_numero + '(você)'
for c in range(7):
    nav.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[1]/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
sleep(1)
#Rolando para baixo
nav.find_element('xpath', '/html').send_keys(Keys.TAB)
sleep(0.1)
nav.find_element('xpath', '/html').send_keys(Keys.TAB)
sleep(0.1)
nav.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div[1]').send_keys(Keys.TAB)
sleep(0.1)
nav.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div[3]').send_keys(Keys.TAB)
#Coletando contatos
lista = list()
lista_reserva = list()
print('\33[1;33mColetando contatos...\33[0m')
for c in range(100):
    nav.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div[5]/div').send_keys(Keys.PAGE_DOWN)
    nav.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div[5]/div').send_keys(Keys.PAGE_DOWN)
    sleep(0.2)
    contato = nav.find_elements('class name', '_21S-L')
    for item in contato:
        nome = item.text.replace('\n', '')
        if not nome in lista:
            lista.append(nome)
        if meu_numero in lista:
            lista.remove(meu_numero)
    if lista == lista_reserva:
        break
    lista_reserva = lista[:]
print('\33[1;33mContatos carregados\33[0m')
sleep(0.9)
nav.find_element('xpath', '/html').send_keys(Keys.ESCAPE)
sleep(0.9)   
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys('(você)')
sleep(0.3)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
sleep(0.2)
# escrever a mensagem para nós mesmos
print('\33[1;32;40m-=' * 40)
print(f'{"Faça sua mensagem normalmente e envie para você mesmo!":^80}')
print('-=' * 40,'\33[0m')
sleep(4)

from selenium.webdriver.common.action_chains import ActionChains
print('\33[1;33mAperte ENTER para enviar para seus contatos\33[0m')
input()
sleep(1.5)
#Gerador de blocos para mandar de 5 em 5 
qntd_contatos = len(lista)
if qntd_contatos % 5 == 0:
    qntd_blocos = int(qntd_contatos / 5)
else:
    qntd_blocos = qntd_contatos // 5 + 1
print(f'\33[1;33mEnviando {qntd_blocos} blocos: \33[0m')
print('__' * 40)
for i in range(qntd_blocos):
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista[i_inicial:i_final]
    # classe do quadrado de mensagem
    lista_elementos = nav.find_elements('class name','_2AOIt')
    for elemento in lista_elementos:
        texto = elemento.text.replace('\n', '')
        if texto:
            item = elemento

    #classe da setinha
    ActionChains(nav).move_to_element(item).perform()
    sleep(0.1)
    try:
        item.find_element('class name', '_3u9t-').click()
        sleep(0.3)
        nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
        sleep(1.6)
        nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]').click()
        sleep(2.0)
    except:
        pass
        item.find_element('class name', '_3Gzl9').click()
        sleep(0.3)
        nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[5]/div').click()
        sleep(1.6)
        nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]').click()
        sleep(2.0)  
        
#selecionar 5 contatos para enviar
    for name in lista_enviar:
        pyperclip.copy(name)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.CONTROL + 'v')
        sleep(1.7)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        if nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div').text:
            nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/span/button').click()
        sleep(0.6)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        sleep(1.2)
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div').click()
    sleep(3)
    print(f'\33[1;33m{i+1}º Bloco enviado\33[0m')
    sleep(1.2)
for c in range(3):
    nav.find_element('xpath', '/html').send_keys(Keys.ESCAPE)
    sleep(0.5)
print()
print(f'\33[1;33mA mensagem foi enviada para {qntd_contatos} contatos com sucesso\33[0m')
print('-=' * 40)