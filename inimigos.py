class Inimigo:
    def __init__(self, nome, vida, dano, experiencia):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.experiencia = experiencia

    def esta_vivo(self):
        return self.vida > 0
    
INIMIGOS = [
    Inimigo("Goblin", 30, 5, 20),
    Inimigo("Lobo", 25, 7, 15),
    Inimigo("Bandido", 40, 8, 25)
]