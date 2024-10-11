estacionamento = [
        [{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'}],
        [{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'}],
]



def imprimir_estacionamento():        
    print('Estacionamento:')
    n_vaga = int(1)
    n_setor = int(1)
    for setor_list in estacionamento:
        print(f'\nsetor{n_setor}')
        n_setor += 1
        n_vaga = 1
        for vaga in setor_list:
            print('\n')
            print(f'Vaga {n_vaga}')
            n_vaga += 1
            for key in vaga.keys():
                print(f'{key} : {vaga[key]}')



def menu():
    print('\n1 - Estacionar')
    print('2 - Retirar')
    print('3 - Adicionar setor')
    print('4 - Adicionar vaga')
    print('5 - Remover setor')
    print('6 - Remover vaga')
    print('7 - Sair')

sair = True
while sair:
    imprimir_estacionamento()
    menu()
    op = input('Digite sua escolha: ')
    if op == '1':
        setor = int(input('informe o setor: '))
        setor -= 1
        vaga = int(input('informe a vaga: '))
        vaga -= 1

        if estacionamento[setor][vaga]['status'] == 'vago':
            print('Vaga Ocupada!\n')
        else:
            estacionamento[setor][vaga]['Placa'] = input('informe sua placa: ')
            estacionamento[setor][vaga]['marca'] = input('Informe sua marca de carro:')
            estacionamento[setor][vaga]['cor'] = input('Informe sua cor de carro: ')
            estacionamento[setor][vaga]['status'] = 'Vago'
            print('Estacionou!\n')
    elif op == '2':
        setor = int(input('informe o setor: '))
        setor -= 1
        vaga = int(input('informe a vaga: '))
        vaga -= 1

        if estacionamento[setor][vaga]['status'] == 'vazio':
            print('Vaga está livre já!\n')
        else:
            estacionamento[setor][vaga]['status'] = 'vazio'
            print('Retirou!\n')
        
    elif op == '3':
        estacionamento.append([{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'},{'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'}])
    elif op == '4':
        setor = int(input('Informe o setor'))
        setor -= 1
        estacionamento[setor].append({'Placa': 'vazio','marca': 'vazio', 'cor': 'vazio', 'status': 'vazio'})
        
    elif op == '5':
        setor = int(input('Informe o setor'))
        setor -= 1
        carros = 0
        for list_vaga in range(0, len(estacionamento[setor])):
            if estacionamento[setor][list_vaga]['status'] == 'vago':
                
                estacionamento[setor][list_vaga]['status'] = 'vazio'
                estacionamento[setor][list_vaga]['Placa'] = 'vazio'
                estacionamento[setor][list_vaga]['marca'] = 'vazio'
                estacionamento[setor][list_vaga]['cor'] = 'vazio'
                carros += 1
        estacionamento.pop(setor)
        
        for list_vaga in range(0,len(estacionamento[-1])):
            if estacionamento[-1][list_vaga]['status'] == 'vazio' and carros > 0:
                estacionamento[-1][list_vaga]['status'] = 'vago'
                 
    elif op == '6':
        setor = int(input('Informe o setor'))
        setor -= 1
        vaga = int(input('informe a vaga: '))
        vaga -= 1
        carros = 0
        for list_vaga in range(0, len(estacionamento[setor][vaga])):
            if estacionamento[setor][list_vaga]['status'] == 'vago':
                
                estacionamento[setor][list_vaga]['status'] = 'vazio'
                estacionamento[setor][list_vaga]['Placa'] = 'vazio'
                estacionamento[setor][list_vaga]['marca'] = 'vazio'
                estacionamento[setor][list_vaga]['cor'] = 'vazio'
                carros += 1
        estacionamento[setor].pop(vaga)
    
        for list_vaga in range(0,len(estacionamento[-1])):
            if estacionamento[-1][list_vaga]['status'] == 'vazio' and carros > 0:
                estacionamento[-1][list_vaga]['status'] = 'vago'
    elif op == '7': 
        sair = False
        print('Saiu do App!\n')

    else:         
        print('Opção inválida!\n')