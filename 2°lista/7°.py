nome = str(input("Digite seu nome: "))
if len(nome) <= 3:
    print("Dados inválidos!\n")
    nome = str(input("Digite seu nome: "))
    
idade = int(input("Digite sua idade: "))
if idade <= 1 and idade >= 149:
    print("Dados inválidos!\n")
    idade = int(input("Digite sua idade: "))
    
salario = float(input("Digite seu salário: "))
if salario <= 0:
    print("Dados inválidos!\n")
    salario = float(input("Digite seu salário: "))
    
sexo = str(input("Digite seu sexo\nM - 1\nou\nF - 2:"))
if sexo != 1 or 2:
    print("Dados inválidos!\n")
    sexo = str(input("Digite seu sexo\nM - 1\nou\nF - 2: "))
print("Cadastro concluído com sucesso!")   