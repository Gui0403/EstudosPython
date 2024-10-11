vlr_Aula = float(input("Digite o valor da hora-aula: "))
n_Aulas = float(input("Digite a quantia de aulas lecionadas no mês: "))
inss = float(input("Digite o valor de desconto do INSS:\n(apenas valor inteiro)\nexemplo: 5% = 5 "))
inss = inss/ 100
print(f"R$ {vlr_Aula * n_Aulas - inss} Esse é seu salário!")