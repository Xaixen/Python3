def login():    
    import pymysql

    conexao = pymysql.connect(
                            host='localhost',
                            user='root',
                            password='',
                            database='login'
    )

    with conexao:
        c = 0
        while True:
            c += 1
            print('--' * 10)
            print(f'{"LOGIN":^20}')
            print('--' * 10)
            nome = input('nome:')
            senha = input('senha:')
            cursor = conexao.cursor()
            expirado()
            sql = f'SELECT * FROM login WHERE nome=%s AND senha=%s;'
            cursor.execute(sql, (nome, senha))
            user = cursor.fetchone()
            cursor.close()
            
            if user:
                print('\33[1;32mlogado com sucesso\33[0m')
                break
            elif c == 5:
                print('--' * 10)
                print(f'\33[1;31m{c}º tentativa, fale com o ADM e crie um novo Usuário\33[0m')
                raise 
            else:
                print('\33[1;33mUsuário não encontrado\33[0m')
            
def expirado():
    from datetime import datetime
    agora = datetime.now()
    cursor.execute('SELECT expirado FROM login')
    for x in cursor:
        print(x)
        if agora == x:
            delete = f'DELETE FROM login WHERE nome=%s and senha=%s'
            cursor.execute(delete, nome, senha)
    print(agora)

login()
