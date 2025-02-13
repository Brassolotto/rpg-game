class Classe:
    def __init__(self, nome, bonus_vida, bonus_forca, bonus_destreza, bonus_inteligencia):
        self.nome = nome
        self.bonus_vida = bonus_vida
        self.bonus_forca = bonus_forca
        self.bonus_destreza = bonus_destreza
        self.bonus_inteligencia = bonus_inteligencia

GUERREIRO = Classe("Guerreiro", 50, 5, 2, 0)
MAGO = Classe("Mago", 20, 0, 2, 5)
ARQUEIRO = Classe("Arqueiro", 30, 2, 5, 1)
        