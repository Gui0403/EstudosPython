nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(nome," tem ", idade, " Anos e é de maior\n")
else:
    print(nome," tem ", idade, " Anos e é de menor\n")