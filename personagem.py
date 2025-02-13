class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.nivel = 1
        self.experiencia = 0
        self.forca = 10
        self.destreza = 10
        self.inteligencia = 10
        
    @classmethod
    def criar_personagem(cls):
        print("=== Criação de Personagem ===")
        nome = input("Digite o nome do seu personagem: ")
        return cls(nome)
        
    def mostrar_status(self):
        print(f"\nStatus de {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Nível: {self.nivel}")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Inteligência: {self.inteligencia}")
