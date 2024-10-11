valor = float(input("Digite o valor do produto: "))
pagamento = int(input("Digite a forma de pagamento:\nPix ou dinheiro - 1\ncartão de crédito à vista - 2\nparcelamento em 2 vezes - 3\nparcelamento mais de 3 vezes - 4\n"))

if pagamento == 1:
        valor = valor  - valor*0.15
        print("Valor a pagar: ", valor)
elif pagamento == 2:
        valor = valor  - valor*0.10
        print("Valor a pagar: ", valor)
elif pagamento == 3:
        print("Valor a pagar: ", valor)
elif pagamento == 4:
        valor = valor  + valor*0.10
        print("Valor a pagar: ", valor)
else:
    print("Valor inválido!")
valor = float(input("Digite o valor do produto: "))
pagamento = int(input("Digite a forma de pagamento:\nPix ou dinheiro - 1\ncartão de crédito à vista - 2\nparcelamento em 2 vezes - 3\nparcelamento mais de 3 vezes - 4\n"))