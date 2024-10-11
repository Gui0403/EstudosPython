def cript(nome, frase, valor_cripto):
    discritor = open(nome,'a')
    new_frase = ''
    for letra in frase:
        new_frase += chr((ord(letra)+valor_cripto)%127)
    discritor.write(new_frase + '\n')
   

def descript(nome, valor_cripto):
    discritor = open(nome,'r')
    new_frase = ''
    for letra in discritor.read():
        if ord(letra)%127 == 10:
            letra = ' '
        else:
            new_frase += chr((ord(letra)- valor_cripto)% 127)
    discritor.close()
    print(new_frase)
