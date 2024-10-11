numeros_pares = []
numeros =[15]
for i in range(1, 15):
    numero = int(input("Digite um numero: "))
    if numero %2 == 0:
        numeros_pares.append(numero)
numeros_pares.sort()
print(f"Os numeros pares (em ordem) digitados foram: {numeros_pares}")