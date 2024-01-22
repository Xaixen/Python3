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
        sleep(5)
        raise
         
app = QtWidgets.QApplication([])
janela = uic.loadUi("interface_grafica.ui")
#janela.gerenciador_telas.setCurrentWidget(janela.login)
janela.botao_entrar.clicked.connect(login)
janela.botao_iniciar.clicked.connect(navegador)

janela.show()
sys.exit(app.exec_())
