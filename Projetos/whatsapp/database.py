
def login():    
    import pymysql

    conexao = pymysql.connect(
                            host='monorail.proxy.rlwy.net',
                            port=26474,
                            user='root',
                            password='A4cgceD51E2b1f2gfAhChCcb4b2Ag-CH',
                            database='railway'
    )

    with conexao:
        c = 0
        while True:
            c += 1
            print('--' * 10)
            print(f'{"LOGIN":^20}')
            print('--' * 10)
            nome = input('Usuário: ')
            senha = input('Senha: ')
            cursor = conexao.cursor()
            cursor.execute(f'SELECT * FROM login WHERE nome=%s AND senha=%s;', (nome, senha))
            user = cursor.fetchone()
            if user:
                import datetime
                agora = (datetime.date.today(),)
                cursor.execute(f'SELECT expirado FROM login WHERE nome=%s AND senha=%s;', (nome, senha))
                mostrar = cursor.fetchone()
                print('\33[1;32mlogado com sucesso\33[0m')
                if agora >= mostrar:
                    cursor.execute(f'DELETE FROM login WHERE nome=%s AND senha=%s;', (nome, senha))
                    conexao.commit()
                    cursor.close()
                else:
                    return False
                break
            elif c == 5:
                print('--' * 10)
                print(f'\33[1;31m{c}º tentativa, fale com o ADM e crie um novo Usuário.\33[0m')
                raise 
            else:
                print('\33[1;33mUsuário não encontrado\33[0m')    