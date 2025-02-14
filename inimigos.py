class Inimigo:
    def __init__(self, nome, vida, dano, experiencia):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.experiencia = experiencia

    def esta_vivo(self):
        return self.vida > 0
    
TEMPLATES_INIMIGOS = [
   {"nome": "Goblin", "vida": 30, "dano": 5, "experiencia": 20},
   {"nome": "Lobo", "vida": 25, "dano": 7, "experiencia": 15},
   {"nome": "Bandido", "vida": 40, "dano": 8, "experiencia": 25}
]

def criar_inimigo(template):
    return Inimigo(
        template["nome"],
        template["vida"],
        template["dano"],
        template["experiencia"]
    )