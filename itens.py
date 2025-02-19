from inventario import item

def curar_vida(jogador):
    cura = 20
    jogador.vida = min(jogador.vida + cura, jogador.vida_maxima)
    print(f"{jogador.nome} recuperou {cura} pontos de vida!")

POCAO_VIDA = item("Poção de Vida", "Recupera 20 pontos de vida", curar_vida)