import pymysql

conexao = pymysql.connect(
                          host='localhost',
                          user='root',
                          password='',
                          database='login'
)

def login():    
        nome = input('nome:')
        senha = input('senha:')
        with conexao:
            cursor = conexao.cursor()
            sql = f'SELECT * FROM login WHERE nome=%s AND senha=%s;'
            cursor.execute(sql, (nome, senha))
            user = cursor.fetchone()
            cursor.close()
        
        if user:
            print('\33[1;32mlogado com sucesso\33[0m')
        else:
            print('\33[1;33mUsuário não encontrado\33[0m')
            raise
            
login()