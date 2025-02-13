import random
from personagem import Jogador
from inimigos import INIMIGOS
from combate import batalha

def main():

    jogador = Jogador.criar_personagem()
    jogador.mostrar_status()

if __name__ == "__main__":
    main()