from classes import GUERREIRO, MAGO, ARQUEIRO
from habilidades import (
    GOLPE_PESADO, GRITO_DE_GUERRA, BOLA_DE_FOGO, RAIO_DE_GELO, FLECHA_PRECISA, CHUVA_DE_FLECHAS
)

class Jogador:

    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100 + classe.bonus_vida
        self.vida_maxima = self.vida
        self.nivel = 1
        self.experiencia = 0
        self.forca = 10 + classe.bonus_forca
        self.destreza = 10 + classe.bonus_destreza
        self.inteligencia = 10 + classe.bonus_inteligencia
        self.energia = 100
        self.energia_maxima = 100
        self.habilidades = []
        self.definir_habilidades()

    def definir_habilidades(self):
        if self.classe.nome == "Guerreiro":
            self.habilidades = [GOLPE_PESADO, GRITO_DE_GUERRA]
        elif self.classe.nome == "Mago":
            self.habilidades = [BOLA_DE_FOGO, RAIO_DE_GELO]
        elif self.classe.nome == "Arqueiro":
            self.habilidades = [FLECHA_PRECISA, CHUVA_DE_FLECHAS]

    def usar_habilidade(self, habilidade, alvo):
        if self.energia < habilidade.custo_energia:
            print("Energia insuficiente")
            return False
        
        self.energia -= habilidade.custo_energia
        dano_base = habilidade.dano

        # Bônus baseado no atributo principal da classe
        if self.classe.nome == "Guerreiro":
            dano_total = dano_base + (self.forca // 2)
        elif self.classe.nome == "Mago":
            dano_total = dano_base + (self.inteligencia // 2)
        else: # Arqueiro
            dano_total = dano_base + (self.destreza // 2)

        alvo.vida -= dano_total
        print(f"Você usou {habilidade.nome} e causou {dano_total} de dano!")
        return True
        
    @classmethod
    def criar_personagem(cls):
        print("=== Criação de Personagem ===")
        nome = input("Digite o nome do seu personagem: ")
        print("\nEscolha sua classe: ")
        print("1 - Guerreiro (Mais vida e força)")
        print("2 - Mago (Mais inteligência)")
        print("3 - Arqueiro (Mais destreza)")

        while True:
            escolha = input("Escolha (1-3): ")
            if escolha == "1":
                classe = GUERREIRO
                break
            elif escolha == "2":
                classe = MAGO
                break
            elif escolha == "3":
                classe = ARQUEIRO
                break
            print("Opção inválida!")

        return cls(nome, classe)
        
    def mostrar_status(self):
        print(f"\nStatus de {self.nome}")
        print(f"Classe: {self.classe.nome}")
        print(f"Nível: {self.nivel}")
        print(f"Experiência: {self.experiencia}/{self.nivel * 100}")
        print(f"Vida: {self.vida}/{self.vida_maxima}")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Inteligência: {self.inteligencia}")

    def ganhar_experiencia(self, quantidade):
        self.experiencia += quantidade
        self.verificar_level_up()

    def verificar_level_up(self):
        experiencia_necessaria = self.nivel * 100
        if self.experiencia >= experiencia_necessaria:
            self.nivel += 1
            self.experiencia -= experiencia_necessaria
            print(f"Parabéns! Você subiu para o nível {self.nivel}!")
            self.aumentar_atributos()

    def aumentar_atributos(self):
        self.vida_maxima += 10
        self.vida = self.vida_maxima
        self.forca += 2
        self.destreza += 2
        self.inteligencia += 2
