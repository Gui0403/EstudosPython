nome = str(input("Digite o nome do Usuário para cadastro: "))
senha = str(input("Digite sua senha: "))
while nome == senha:
    print("Usuário é igual a senha, tente novamente!")
    nome = str(input("Digite o nome do Usuário para cadastro: "))
    senha = str(input("Digite sua senha: "))
print("Usuário cadastrado com sucesso!")