import random
from personagem import Jogador

def calcular_dano(atacante):
    if isinstance(atacante, Jogador):
        return 5 + (atacante.forca // 2)
    return atacante.dano

def batalha(jogador, inimigo):
    print(f"\nUm {inimigo.nome} apareceu!")

    while inimigo.esta_vivo() and jogador.vida > 0:
        print(f"\nSua vida: {jogador.vida}")
        print(f"\nVida do {inimigo.nome}: {inimigo.vida}")
        print("\nO que você quer fazer?")
        print("1 - Atacar")
        print("2 - Fugir")

        escolha = input("Escolha: ")

        if escolha == "1":
            dano = calcular_dano(jogador)
            inimigo.vida -= dano
            print(f"\nVocê causou {dano} de dano ao {inimigo.nome}!")

            if inimigo.esta_vivo():
                dano_inimigo = calcular_dano(inimigo)
                jogador.vida -= dano_inimigo
                print(f"O {inimigo.nome} causou {dano_inimigo} de dano a você!")

        elif escolha == "2":
            if random.random() < 0.5:
                print("Você fugiu com sucesso!")
                return False
            print("Você falhou em fugir!")
            dano_inimigo = calcular_dano(inimigo)
            jogador.vida -= dano_inimigo
            print(f"O {inimigo.nome} causou {dano_inimigo} de dano em você!")

    if jogador.vida <= 0:
        print("Você foi derrotado!")
        return False
    print(f"\nVocê derrorou o {inimigo.nome}!")
    jogador.ganhar_experiencia(inimigo.experiencia)
    return True