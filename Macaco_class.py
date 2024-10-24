#Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
#E pelo menos os métodos comer(), verBucho() e digerir().
#Faça um programa ou teste interativamente, criando pelo menos dois macacos, 
#alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.

class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
        
    
    def comer(self):
        comida = input(f'Qual comida para {self.nome}? ')
        self.bucho.append(comida)
        print(f'Voce deu {comida} para {self.nome}!\n')
                      
    def verBucho(self):
        print(f'\nNo bucho de {self.nome} tem: ')
        if len(self.bucho) == 0:
            print(f'O bucho de {self.nome} esta vazio!\n')
        else:
            for item in self.bucho:
                print(item, end=' \n')
            print('\n')
            
    def digerir(self):
        self.bucho.clear()
        print(f'\n{self.nome} digeriu tudo!')
        
    
def main():
    Caio = Macaco('Caio', [])
    Pedro = Macaco('Pedro', [])
    while True:
        escolha = input('Pressione \n[A] para alimentar\n[V] para ver o bucho\n[D] para digerir\nOU qualquer outra tecla para encerrar\n')
        escolha = escolha.lower()
        if escolha == 'a':
            masqueico = input('[1] para alimentar Caio\n'
                              '[2] para alimentar Pedro')
            if masqueico == '1':
                Caio.comer()
            else: 
                Pedro.comer()
        
        elif escolha == 'v':
            masqueico = input('[1] para ver o bucho de Caio\n'
                              '[2] para ver o bucho de Pedro')
            if masqueico == '1':
                if 'Pedro' in Caio.bucho:
                    for item in Pedro.bucho:
                        Caio.bucho.append(item)
                Caio.verBucho()
            else:
                if 'Caio' in Pedro.bucho:
                    for item2 in Pedro.bucho:
                        Caio.bucho.append(item2)
                Pedro.verBucho()
            
        elif escolha == 'd':
            masqueico = input('[1] para fazer Caio digerir\n'
                              '[2] para fazer Pedro digerir')
            if masqueico == '1':
                Caio.digerir()
            else: 
                Pedro.digerir()
                
        else:
            break
        

main()
        
            
            
        
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        