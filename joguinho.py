#!/usr/bin/env python

JOGADORES = {
    'X': 1,
    'O': 2
}

COMBINACOES_VITORIA = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


def mostrar_quadro(quadro):
    linhas = [
        [quadro[0], quadro[1], quadro[2]],
        [quadro[3], quadro[4], quadro[5]],
        [quadro[6], quadro[7], quadro[8]]
    ]

    linhas = map(lambda linha: "|{}|{}|{}|".format(*linha), linhas)

    print()
    print("\n".join(linhas))
    print()


def validar_escolha(escolha):
    try:
        escolha = int(escolha)
    except ValueError:
        return False

    if escolha not in list(range(1, 10)):
        return False

    return True


def ler_escolha():
    while True:
        escolha = input(
            "Digite um numero para marcar o quadro (1-9): "
        ).strip()

        if validar_escolha(escolha):
            return int(escolha)

        print("Valor inválido! Tente novamente.")


def movimento_jogador(quadro, icone):
    print("A vez do jogador {}.".format(JOGADORES[icone]))

    escolha = ler_escolha()

    if quadro[escolha - 1] == " ":
        quadro[escolha - 1] = icone
    else:
        print()
        print("Esse ja foi marcado!")
        mostrar_quadro(quadro)
        movimento_jogador(quadro, icone)


def vitoria(quadro, icone):
    for combinacao in COMBINACOES_VITORIA:
        venceu = True
        for posicao in combinacao:
            if quadro[posicao] != icone:
                venceu = False

        if venceu:
            return True

    return False


def fim(quadro):
    return " " not in quadro


def inicializa_quadro():
    return [" "] * 9


def fazer_jogada(quadro, icone):
    movimento_jogador(quadro, icone)
    mostrar_quadro(quadro)
    if vitoria(quadro, icone):
        print("{} venceu! Parabens!".format(icone))
        exit()
    elif fim(quadro):
        print("Jogo EMPATADO!")
        exit()


def main():
    quadro = inicializa_quadro()

    mostrar_quadro(quadro)

    while True:
        fazer_jogada(quadro, "X")
        fazer_jogada(quadro, "O")


main()
