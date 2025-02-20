import random
from inimigos import TEMPLATES_INIMIGOS, criar_inimigo

class Area:
    def __init__(self, nome, descricao, chance_encontro, inimigos):
        self.nome = nome
        self.descricao = descricao
        self.chance_encontro = chance_encontro
        self.inimigos = inimigos

    def explorar(self, jogador):
        print("\nVocê está explorando {self.nome}...")
        print(self.descricao)
        if random.random() < self.chance_encontro:
            template = random.choice(self.inimigos)
            return criar_inimigo(template)
        else:
            print("Você não encontrou nenhum inimigo nesta área.")
            return None
        
AREA_FLORESTA = Area(
    "Floresta Encantada",
    "Uma densa floresta repleta de segredos e criaturas místricas.",
    0.8,
    TEMPLATES_INIMIGOS
)

AREA_CAVERNA = Area(
    "Caverna Sombria",
    "Uma caverna escura com perigos a cada esquina e ecos de combates passados.",
    0.9,
    TEMPLATES_INIMIGOS
)

AREA_VILA = Area(
    "Vila Tranquila",
    "Uma pequena vila onde os moradores vivem em paz, embora rumores de ameaças persistam.",
    0.3,
    TEMPLATES_INIMIGOS
)

AREAS = [AREA_FLORESTA, AREA_CAVERNA, AREA_VILA]