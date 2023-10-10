
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import sleep
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
def startnav(link):

    try:
        service = Service(ChromeDriverManager().install())
        nav =  webdriver.Chrome(service=service)
        nav.get(link)
    except PermissionError:
        print('\33[1;31mPermissão Negada, tente novamente mais tarde!\33[0m')
        raise

def coleta_cont():
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

def gera_blocos(lista):
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

def quadrado():
    # classe do quadrado de mensagem
    lista_elementos = nav.find_elements('class name','_2AOIt')
    for elemento in lista_elementos:
        texto = elemento.text.replace('\n', '')
        if texto:
            item = element

