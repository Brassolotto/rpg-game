import random
from personagem import Jogador
from mundo import AREAS
from inimigos import TEMPLATES_INIMIGOS, criar_inimigo
from combate import batalha
from itens import POCAO_VIDA

def escolher_area():
    print("\nEscolha uma área para explorar:")
    for i, area in enumerate(AREAS, start=1):
        print(f"{i} - {area.nome}: {area.descricao}")
    escolha = input("Escolha o número da área (0 para cancelar): ")
    try:
        indice = int(escolha)
        if indice == 0:
            return None
        elif 1 <= indice <= len(AREAS):
            return AREAS[indice - 1]
        else:
            print("Opção inválida!")
            return None
    except ValueError:
        print("Opção inválida!")
        return None

def explorar(jogador):
    print("\nVocê saiu para explorar...")
    if random.random() < 0.7:
        template = random.choice(TEMPLATES_INIMIGOS)
        inimigo = criar_inimigo(template)
        return batalha(jogador, inimigo)
    print("Você não encontrou nada interessante...")
    return True

def loop_jogo(jogador):
    area_atual = AREAS[0]
    while True:
        print(f"\nVocê está atualmente na área:  {area_atual.nome}.")
        print("\nO que deseja fazer?")
        print("1 - Ver status")
        print("2 - Explorar área")
        print("3 - Mudar de área")
        print("4 - Descansar")
        print("5 - Usar item")
        print("6 - Salvar jogo")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogador.mostrar_status()
        elif opcao == "2":
            if not explorar(jogador):
                print("Fim de jogo!")
                break

        elif opcao == "3":
            nova_area = escolher_area()
            if nova_area:
                area_atual = nova_area
                print(f"Você se moveu para a área: {area_atual.nome}")        
        elif opcao == "4":
            jogador.vida = jogador.vida_maxima
            print("Você descansou e recuperou toda sua vida!")
        elif opcao == "5":
            jogador.usar_item()
        elif opcao == "6":
            jogador.salvar_jogo()
        elif opcao == "7":
            print("Até a próxima aventura!")
            break

def main():
    print("=== Bem-vindo ao RPG ===")
    print("1 - Novo Jogo")
    print("2 - Carregar Jogo")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        jogador = Jogador.criar_personagem()
    elif escolha == "2":
        jogador = Jogador.carregar_jogo()
        if not jogador:
            print("Iniciando um novo jogo...")
            jogador = Jogador.criar_personagem()
    else:
        print("Opção inválida!")
        return
    
    jogador.mostrar_status()
    jogador.adicionar_item(POCAO_VIDA)
    loop_jogo(jogador)

if __name__ == "__main__":
    main()