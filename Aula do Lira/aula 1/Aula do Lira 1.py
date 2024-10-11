# 1°projeto
# Passo 1: Entrar no sistema da empresa 
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui as pa
import time
pa.PAUSE = 0.2

# pa.write -> escrever um texto
# pa.press -> apertar 1 tecla
# pa.click -> clicar em algum lugar da tela
# pa.hotkey -> combinação de teclas

#Fazer login
#Abrir/Importar a base de dados de produtos para cadastrar
#Cadastrar um produto
#Repetir isso tudo até acabar a lista de produtos

#2 Abrir navegador
pa.press("win")
pa.write("edge")
pa.press("enter")

#Entrar no site
time.sleep(1.5)
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(1.5)

#3 login
pa.press("TAB")
pa.write("pabloguilhermemartinez@gmail.com")
pa.press("TAB")
pa.write("@p4blo0403")
pa.press("TAB")
pa.press("enter")

#4 cadastro de produtos
import pandas as pd

produtos = pd.read_csv("produtos.csv")
for linha in produtos.index:
    
    codigo = str(produtos.loc[linha,"codigo"])
    marca = str(produtos.loc[linha,"marca"])
    tipo = str(produtos.loc[linha,"tipo"])
    categoria = str(produtos.loc[linha,"categoria"])
    preco_unitario = str(produtos.loc[linha,"preco_unitario"])
    custo = str(produtos.loc[linha,"custo"])
    obs = str(produtos.loc[linha,"obs"])
  
    pa.click(x=654, y=245)
    pa.write(codigo)
    pa.press("TAB")

    pa.write(marca)
    pa.press("TAB")

    pa.write(tipo)
    pa.press("TAB")

    pa.write(categoria)
    pa.press("TAB")

    pa.write(preco_unitario)
    pa.press("TAB")

    pa.write(custo)
    pa.press("TAB")
    
    if obs != "nan":
        pa.write(obs)
    else:
        pa.write("Nada solicitado")
   
    pa.press("TAB")
    pa.press("enter")
    time.sleep(0.5)
    pa.scroll(5000)