nota1 = float(input("Digite sua nota 1°: "))
nota2 = float(input("Digite sua nota 2°: "))
nota3 = float(input("Digite sua nota 3°: "))
nota4 = float(input("Digite sua nota 4°: "))
media = nota1 + nota2 + nota3 + nota4 / 4
if media >= 19.5:
    media = "%.2f" %media
    print("Aluno aprovado! com média ",media)
else:
    media = "%.2f" %media
    print("Aluno reprovado com média ",media)