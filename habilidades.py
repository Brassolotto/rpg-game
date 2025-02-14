class Habilidade:
    def __init__(self, nome, dano, custo_energia, descricao):
        self.nome = nome
        self.dano = dano
        self.custo_energia = custo_energia
        self.descricao = descricao

#habilidades do guerreiro
GOLPE_PESADO = Habilidade(
    "Golpe pesado",
    15,
    20,
    "Um golpe poderoso que causa dano extra baseado na força"
)

GRITO_DE_GUERRA = Habilidade(
    "Grito de gerra",
    0,
    30,
    "Aumenta temporariamente a força do guerreiro"
)

#habilidades do mago
BOLA_DE_FOGO = Habilidade(
    "Bola de fogo",
    25,
    30,
    "Lança uma bola de fogo que causa dano baseado na inteligência"
)

RAIO_DE_GELO = Habilidade(
    "Raio de gelo",
    20,
    25,
    "Causa dano e tem chance de congelar o inimigo"
)

#habilidades do arqueiro
FLECHA_PRECISA = Habilidade(
    "Flecha precisa",
        30,
        35,
        "Um tiro certeiro que causa dano extra baseado na destreza"
)

CHUVA_DE_FLECHAS = Habilidade(
    "Chuva de flechas",
    30,
    35,
    "Dispara múltiplas flechas causando dano em área"
)