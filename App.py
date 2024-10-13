import flet as ft

def main(pagina): 
    texto = ft.Text("PyChat")


    chat = ft.Column()

    def enviar_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
    pagina.pubsub.subscribe(enviar_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Write your mensage", on_submit=enviar_mensagem, autofocus=True)
    botao_enviar = ft.ElevatedButton("Send", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    
    def entrar_chat(evento):
        popup.open=False
        pagina.remove(texto)
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} joined the chat")
        pagina.add(linha_enviar)
        pagina.update()
    
    titulo_popup = ft.Text("Welcome to PyChat!")
    nome_usuario = ft.TextField(label="Write your name here", on_submit=entrar_chat, autofocus=True)
    botao_popup = ft.ElevatedButton("Enter Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_popup]
    )
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Start Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)
