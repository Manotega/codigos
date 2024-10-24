#Crie uma classe que modele um Tamagushi 
#Atributos: Nome, Fome, Saúde e Idade
#Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
#humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        
    
    def alterar_nome(self):
        alt = input('Alterar o nome? [s/n] ')
        alt.lower()
        if alt == 's':
            self.nome = input('Escolha o novo nome do bicho: ')
        
    def alterar_fome(self):
        comida = input('Alimentar o bicho? [s/n] ')
        comida.lower()
        if comida == 's':
            self.fome += 30
        else:
            self.fome = self.fome - 25
        
    def alterar_saude(self):
        remedio = input('Dar remedio para esse viado? [s/n] ')
        remedio.lower()
        if remedio == 's':
            self.saude += 30
        else:
            self.saude = self.saude - 25
        
    def alterar_idade(self):
        self.idade += int(input('Quantos anos se passaram? '))
        

def humor(fome, saude):
    if fome + saude >= 100:
        print('Essa porra ta feliz pra caralho')
    elif 100 > fome + saude >= 50:
        print('Ate que ele ta bem, vai')
    elif  0 < fome + saude < 50:
        print('Tadinho, ta borocoxo')
    elif fome + saude < 0:
        print('Seu tamagoshi acabou de se jogar da ponte')

def main():
    bicho = Tamagushi('Rogerio Ceni', 50, 60, 2)
    while True:    
        bicho.alterar_nome()
        bicho.alterar_idade()
        bicho.alterar_fome()
        bicho.alterar_saude()
        print(" ")
        humor(bicho.fome, bicho.saude)
        
        if bicho.idade > 20:
            print('Seu bicho morreu. RIP')
            break
        else:
            print("nome: %s   idade: %d   fome: %d   saude: %d" %(bicho.nome, bicho.idade, bicho.fome, bicho.saude))
            cont = input('continuar? [s/n] ')
            cont.lower()
            if cont != 's':
                break
            
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        