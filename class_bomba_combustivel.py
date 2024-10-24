import os

class bomba_combustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        
        
    def abastecer_por_valor(self):
        '''recebe um valor em reais e retorna a quantidade de litros adicionadas ao veiculo
        e o restante de litros na bomba''' 
        
        valor = float(input('\nQuantos reais? R$'))
        abst = round((valor / self.valor_litro), 2)
        
        if self.quantidade_combustivel - abst < 0:
            print('Nao ha combustivel o suficiente na bomba!')
        else: 
            print(f'Foram abastecidos {abst} Litros')
            self.quantidade_combustivel -= abst 
            print(f'\nRestam {self.quantidade_combustivel} litros de combustivel na bomba')
    
    
    def abastecer_por_litro(self):
        valor = float(input('\nQuantos litros? '))
        abst = round((valor * self.valor_litro), 2)
        
        if self.quantidade_combustivel - valor < 0:
            print('Nao ha combustivel o suficiente na bomba!')
        else:
            print(f'Total a ser pago: R${abst}')        
            self.quantidade_combustivel -= valor
            print(f'\nRestam {self.quantidade_combustivel} litros de combustivel na bomba')
            
        
    def alterar_valor(self):
        novo = float(input('\nQual o valor do litro do combustivel? '))
        self.valor_litro = round(novo, 2)
        print(f'O valor do combustivel foi alterado para {self.valor_litro}')
        
        
    def alterar_combustivel(self):
        self.tipo_combustivel = (input('\nQual tipo de combustivel?'))
        print(f'O combustivel foi alterado para {self.tipo_combustivel}')
        
    
    def alterar_qtd_combustivel(self):
        qtd = float(input('\nQuantidade de combustivel na bomba? '))
        self.quantidade_combustivel = round(qtd, 2)
        print(f'\nRestam {self.quantidade_combustivel} litros de combustivel na bomba')
        


def menu():
    bomba = bomba_combustivel('Gasolina', 5.0, 1000)
    
    while True:
        print("\n----- Menu Bomba de Combustível -----")
        print("[1] Abastecer por valor")
        print("[2] Abastecer por litro")
        print("[3] Alterar valor do combustível")
        print("[4] Alterar tipo de combustível")
        print("[5] Alterar quantidade de combustível na bomba")
        print("[6] Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            bomba.abastecer_por_valor()
        elif opcao == '2':
            bomba.abastecer_por_litro()
        elif opcao == '3':
            bomba.alterar_valor()
        elif opcao == '4':
            bomba.alterar_combustivel()
        elif opcao == '5':
            bomba.alterar_qtd_combustivel()
        elif opcao == '6':
            os.system('cls')
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        