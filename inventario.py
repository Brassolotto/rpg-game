class item:
    def __init__(self, nome, descricao, efeito):
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito

    def usar(self, jogador):
        self.efeito(jogador)
        