class Jogador:
    jogadores = []

    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
        type(self).jogadores.append(self)

    @classmethod
    def buscar_jogadores(cls, filename):
        '''
        Método para buscar todos os jogadores do arquivo
        '''
        try:
            with open(filename, 'rt') as file:
                dados = file.read()
        except IOError:
            print("Não foi possível abrir o arquivo.")

        jogadores = dados.split('\n')

        for i in jogadores:
            nome, pontuacao = i.split('=')
            novo = Jogador(nome, int(pontuacao))

    @classmethod
    def buscar_jogador_nome(cls, nome):
        for obj in cls.jogadores:
            if obj.nome == nome:
                return obj