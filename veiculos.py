class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
        
    @property
    def ligado(self):
        return 'Ligado' if self._ligado else 'Desligado'
    
    def __str__(self):
        return f'marca: {self.marca}  |  modelo: {self.modelo}  |  {self.ligado}'
    


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
        
    def __str__(self):
        return f'marca: {self.marca}  |  modelo: {self.modelo}  |  qtd portas: {self.portas}  |  {self.ligado}'
    
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
        
    def __str__(self):
        return f'marca: {self.marca}  |  modelo: {self.modelo}  |  tipo: {self.tipo}  |  {self.ligado}'
    
    

carro1 = Carro('Toyota', 'Corolla', 4)    
carro2 = Carro('Volkswagen', 'Fusca', 2) 
carro3 = Carro('Mini', 'Cooper', 2)

moto1 = Moto('Mitsubishi', 'FOdase', 'esportiva')
moto2 = Moto('Yamaha', 'isso', 'casual')
moto3 = Moto('BMW', 'boa', 'casual')            
    
print(carro1)
print(carro2)
print(carro3)
print(moto1)
print(moto2)
print(moto3)






