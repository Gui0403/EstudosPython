time = int(input("Digite o tempo gasto na viagem em horas: "))
Vm = int(input("Digite a velocidade percorrida em Km: "))
dist = time * Vm
litros_Usados = dist / 12
print(f"A quantia de litros usados foi de aproximadamente {"%.2f " %litros_Usados} Litros\nDistância percorrida {dist}Km\nTempo gasto {time} horas\tVelocidade média {Vm} Km/h")