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
        print(f"Vida: {self.vida}")
        print(f"Nível: {self.nivel}")
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
        self.vida += 10
        self.forca += 2
        self.destreza += 2
        self.inteligencia += 2
