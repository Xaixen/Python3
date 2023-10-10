import flet as ft

def main(pagina):
    texto = ft.Text('Hashzap')
    chat = ft.Column()
    nome_usuario = ft.TextField(label='Escreva seu nome')
    enviar_mensagem = ft.TextField(label='Digite sua mensagem')
    botao_enviar_mensagem = ft.ElevatedButton('Enviar')
    def entrar_popup(evento):
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao)
        pagina.remove(texto)
        pagina.add(enviar_mensagem)
        pagina.add(botao_enviar_mensagem)
        pagina.add(ft.Row([enviar_mensagem, botao_enviar_mensagem]))
        pagina.update()
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Bem vindo ao Hashzap'),
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
ft.app(target=main, view=ft.WEB_BROWSER)