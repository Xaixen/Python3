from PyQt5 import QtWidgets, uic
import sys

def login():    
    import pymysql

    conexao = pymysql.connect(
                            host='localhost',
                            port=3306,
                            user='root',
                            password='',
                            database='login'
    )

    with conexao:
            nome = janela.usuario.text()
            Senha = janela.senha.text()
            cursor = conexao.cursor()
            cursor.execute(f'SELECT * FROM login WHERE nome=%s AND senha=%s;', (nome, Senha))
            user = cursor.fetchone()
            if user:
                import datetime
                agora = (datetime.date.today(),)
                cursor.execute(f'SELECT expirado FROM login WHERE nome=%s AND senha=%s;', (nome, Senha))
                mostrar = cursor.fetchone()
                if agora >= mostrar:
                    cursor.execute(f'DELETE FROM login WHERE nome=%s AND senha=%s;', (nome, Senha))
                    conexao.commit()
                    cursor.close()
                janela.gerenciador_telas.setCurrentWidget(janela.massa) 
                mostrar = str(mostrar).replace('datetime.date', '').replace('(', '').replace(')', '').replace(',', ' /')
                janela.false_1.setText(f'Nome: {nome}       Expira: {mostrar}')
            else:
                janela.label_6.setText('Usuário ou senha. Não encontrado!')
                janela.usuario.setText('')
                janela.senha.setText('')

#Importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyperclip
def navegador():
    janela.botao_iniciar.deleteLater()
    janela.update()
    try:
        service = Service(ChromeDriverManager().install())
        nav =  webdriver.Chrome(service=service)
        nav.get('https://web.whatsapp.com')
        janela.false_2.setText('ok')

    except PermissionError:
        janela.false_2.setText('Permissao Negada')
    janela.false_3.setText('Aguarde...')
    sleep(120)
    janela.false_3.setText("ok")
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
        
app = QtWidgets.QApplication([])
janela = uic.loadUi("interface_grafica.ui")
#janela.gerenciador_telas.setCurrentWidget(janela.login)
janela.botao_entrar.clicked.connect(login)
janela.botao_iniciar.clicked.connect(navegador)

janela.show()
sys.exit(app.exec_())
