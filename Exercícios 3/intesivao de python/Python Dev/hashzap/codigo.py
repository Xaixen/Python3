import flet as ft

def main(pagina):
    texto = ft.Text('Xablazap', size=100)
    chat = ft.Column()
    nome_usuario = ft.TextField(label='Escreva seu nome')
    
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem['tipo']
        if tipo == 'mensagem':
            texto_mensagem = mensagem['texto']
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}")) 
        else:
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(ft.Text(f'{usuario_mensagem} entrou no chat', size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({'texto': campo_mensagem.value, 'usuario': nome_usuario.value, 'tipo': 'mensagem'})
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(label='Digite sua mensagem')
    botao_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    def entrar_popup(evento):
        popup.open = False
        pagina.pubsub.send_all({'usuario': nome_usuario.value, 'tipo': 'entrada'})
        pagina.remove(botao)
        pagina.remove(texto)
        pagina.add(chat)
        pagina.add(ft.Row([campo_mensagem, botao_mensagem]))
        pagina.update()
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Bem vindo ao Xablazap'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('entrar', on_click=entrar_popup)],
    )
    def entrar_chat(evento):
       pagina.dialog = popup
       popup.open = True
       pagina.update()

    botao = ft.ElevatedButton('Iniciar chat', on_click=entrar_chat)
    pagina.add(texto)
    pagina.add(botao)
ft.app(target=main)