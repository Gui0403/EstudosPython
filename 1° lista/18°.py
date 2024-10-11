fran = float(1.5)
sara = float(1.1)
ano = 0

while sara <= fran:
    ano = ano+1
    fran = fran + 0.02
    sara = sara + 0.03
    fran =float("%.2f" %fran)
    sara =float("%.2f" %sara)
    
    print(f"Sara tem  {sara} de altura \tFrancisco tem {fran} de altura\t anoatual é: {ano}")