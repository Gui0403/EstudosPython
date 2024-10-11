# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

#importando o flet
import flet as ft

#criar a função principal do seu app
def main(pagina):
    # criar todas as funcionalidades 
    # cria o elemento
    titulo = ft.Text('ChatZinho')
    titulo_janela = ft.Text('Bem vindo ao ChatZinho')
    campo_usuario = ft.TextField(label='Escreva seu nome pro chat')
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()
      
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
      
    def enviar_mensegem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_usuario.value
        mensagem = f'{nome_usuario}: {texto_mensagem}'
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ''
        pagina.update()

        
        
        
    campo_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensegem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensegem)
    
    
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar]) 
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        texto_chat = f'{campo_usuario.value} entrou no chat!'
        pagina.pubsub.send_all(texto_chat)
        pagina.update()
    
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    
          
  
    janela = ft.AlertDialog(
        title=titulo_janela, 
        content=campo_usuario, 
        actions=[botao_entrar])
    
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    
    
    
    # adiciona o seu elemento
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    

#rodar o seu app
ft.app(main, view= ft.WEB_BROWSER)


