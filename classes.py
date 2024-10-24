class Avaliacao:
    def __init__(self, cliente, nota):
        self.cliente = cliente
        self.nota = nota
        
    def __str__(self):
        return f'Cliente: {self.cliente} | Nota: {self.nota}'

class Restaurante:
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome.capitalize()
        self.categoria = categoria.capitalize()
        self._ativacao = False
        self.avaliacao = []
        Restaurante.lista_restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome.ljust(25)} | {self.categoria.ljust(25)} | {self.media_avaliacoes.ljust(25)} | {self.ativacao}'
    
    def sel_nome(self):
        self.nome = input('Digite o nome do restuarante: \n')
        self.nome = self.nome.capitalize()
        return f'Restaurante registrado como {self.nome}'

    def sel_categoria(self):
        self.categoria = input('Digite a categoria do restaurante: \n')
        self.categoria = self.categoria.upper()
        return f'Restaurante registrado como {self.categoria}'

    def ativar(self):
        if self._ativacao == False:
            a = input('Ativar restaurante? [S][N] \n')
            if a == 's':
                self._ativacao = True
        else:
            a = input('Desativar restaurante? [S][N] \n')
            if a == 's':
                self._ativacao = False

    @property
    def ativacao(self):
        return 'Ativo' if self._ativacao else 'Desativado'
    
    @classmethod    
    def listar_restaurantes(cls):
        print('')
        print('NOME '.ljust(25), '| CATEGORIA '.ljust(27), '| AVALIACAO '.ljust(25), '  | STATUS')
        for restaurante in cls.lista_restaurantes:
            print(restaurante)
            
    def receber_avaliacao(self, cliente, nota):
        ava = Avaliacao(cliente, nota)
        self.avaliacao.append(ava)
    
    @property
    def media_avaliacoes(self):
        if not self.avaliacao:
            return 'N/A'
        soma = 0
        total = len(self.avaliacao)
        for item in self.avaliacao:
            soma += item.nota
        media = round(soma / total, 1)
        return str(media)
        



            
            
            

