# Motocicleta, Carro, Carro Grande
from enum import Enum
from datetime import datetime
import os 
import math

class TipoVeiculo(Enum):
    Motocilceta = 0
    Carro = 1
    CarroGrande = 2
    

class Veiculo:
    def __init__(self, placa, proprietario, tipoveiculo, cor):
        self.placa = placa
        self.proprietario = proprietario
        self.tipoveiculo = tipoveiculo
        self.cor = cor
        self.hora_entrada = datetime.now()
        self.hora_saida = datetime.now()
        
class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.faturamento = 0
    
    
    def registar_saida(self,placa):
        # registrar saida de veiculo
        veiculo_encontrado = None
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                veiculo_encontrado = veiculo
        if veiculo_encontrado == None:
            print(f'Veiculo não encontrado pela placa {placa}')
            return
        valor_cobrado = 0
        veiculo_encontrado.hora_saida = datetime.now()
        diferenca = veiculo_encontrado.hora_saida - veiculo_encontrado.hora_entrada
        if veiculo_encontrado.tipoveiculo == '0':
            # Moto
            valor_cobrado = 5 + (5 * math.floor((diferenca.seconds) / 3600))
            print('Hora de entrada ' + str(veiculo_encontrado.hora_entrada))
            print('Hora de saída ' + str(veiculo_encontrado.hora_saida))
            print(f'Valor cobrado: {valor_cobrado}')
        elif veiculo_encontrado.tipoveiculo == '1':
            # Carro
            valor_cobrado = 10 + (6 * math.floor((diferenca.seconds) / 3600))
            print('Hora de entrada ' + str(veiculo_encontrado.hora_entrada))
            print('Hora de saída ' + str(veiculo_encontrado.hora_saida))
            print(f'Valor cobrado: {valor_cobrado}')
        else:
            # Carro Grande
            valor_cobrado = 15 + (7 * math.floor((diferenca.seconds) / 3600))
            print('Hora de entrada ' + str(veiculo_encontrado.hora_entrada))
            print('Hora de saída ' + str(veiculo_encontrado.hora_saida))
            print(f'Valor cobrado: {valor_cobrado}')
        self.faturamento += valor_cobrado
        
        
    def registrar_veiculo(self,Veiculo: Veiculo):
        # registrar veiculo
        self.veiculos.append(Veiculo)
        Veiculo.hora_entrada = datetime.now()
        print('Veiculo foi registrado com sucesso')
    
    def exibir_faturamento(self):
        # exibir faturamento 
        print('Faturamento total: '+ str(self.faturamento))
         
    
    def listar_veiculos(self):
        # lista veiculo
        for veiculo in self.veiculos:
            print(f'Placa: {veiculo.placa}')
            print(f'Proprietário: {veiculo.proprietario}')
            print(f'Cor: {veiculo.cor}')
            print(f'Tipo de veiculo: {veiculo.tipoveiculo}')
        
def exibir_menu():
    print('''
--------------------------------------------------------------------------------------------------
Projeto estacionamento!
Escolha uma opção:
1 - Registrar entrada do veiculo
2 - Registrar a saída de um veiculo
3 - Exibir Faturamento
4 - Exibir todos os veículos estacionados
0 - Encerrar Programa
--------------------------------------------------------------------------------------------------
    ''')
    
    opcao = input('Opção...')
    print(opcao)
    if opcao == '1':
        # registrar entrada
        os.system('cls')
        print('Registro de entrada de veículo!')
        proprietario = input('Informe o nome do proprietário: ')
        placa = input('Informe a placa do carro (AAA-1234): ')
        cor = input('Informe a cor do carro: ')
        tipo_veiculo = input('Informe o tipo do veículo: ')
        veiculo = Veiculo(placa, proprietario, tipo_veiculo, cor)
        estacionamento.registrar_veiculo(veiculo)

    elif opcao == '2':
        # registrar saida
        os.system('cls')
        print('Registro de saída!')
        placa = input('Informe a placa do veículo: ')
        estacionamento.registar_saida(placa)
    elif opcao == '3':
        # exibir faturamento
        os.system('cls')
        estacionamento.exibir_faturamento()
        
    elif opcao == '4':
        estacionamento.listar_veiculos()
        # exibir todos os veiculos estacionandos
        ...
    elif opcao == '0':
        print('Programa encerrado!')
        os.system('exit')
        # encerrar
    else:
        print('Opção inválida!')
        
estacionamento = Estacionamento()
while True:       
    exibir_menu()