import random
from personagem import Jogador
from inimigos import TEMPLATES_INIMIGOS, criar_inimigo
from combate import batalha
from itens import POCAO_VIDA

def explorar(jogador):
    print("\nVocê saiu para explorar...")
    if random.random() < 0.7:
        template = random.choice(TEMPLATES_INIMIGOS)
        inimigo = criar_inimigo(template)
        return batalha(jogador, inimigo)
    print("Você não encontrou nada interessante...")
    return True

def loop_jogo(jogador):
    while True:
        print("\nO que deseja fazer?")
        print("1 - Ver status")
        print("2 - Explorar")
        print("3 - Descansar")
        print("4 - Usar item")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogador.mostrar_status()
        elif opcao == "2":
            if not explorar(jogador):
                print("Fim de jogo!")
                break
        elif opcao == "3":
            jogador.vida = jogador.vida_maxima
            print("Você descansou e recuperou toda sua vida!")
        elif opcao == "4":
            jogador.usar_item()
        elif opcao == "5":
            print("Até a próxima aventura!")
            break

def main():

    jogador = Jogador.criar_personagem()
    jogador.mostrar_status()
    jogador.adicionar_item(POCAO_VIDA)
    loop_jogo(jogador)

if __name__ == "__main__":
    main()