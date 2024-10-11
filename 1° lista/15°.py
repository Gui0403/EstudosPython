from datetime import datetime
ano_nascimento = int(input("Digite o ano de nascimento: "))
#Obter a data atual
data_atual = datetime.now()
#Calculo de anos
idade_anos = data_atual.year - ano_nascimento
#Calculo de meses
idade_meses = (data_atual.year - ano_nascimento) * 12 + data_atual.month
#Calculo de dias
idade_dias = (data_atual - datetime(ano_nascimento, data_atual.month, data_atual.day)).days
#Saída
print(f"Idade: {idade_anos} anos, {idade_meses} meses, {idade_dias} dias.")