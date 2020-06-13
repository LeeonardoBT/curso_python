# coding: utf-
from game import buscar_palavras_arquivo
from game import iteracao_forca

def recebe_jogador() -> str:
    """
    recebe o input do nome do jogador
    """
    nome = str(input("Digite o nome do jogador: "))

    return nome

def menu_principal():
    """
    menu principal
    """

    jogador = recebe_jogador()
    palavras = buscar_palavras_arquivo(filename='forca_python')
    pontuacao = 0
    opcao = 0

    while opcao != 9:
        print("\n-- JOGO DA FORCA --")
        print("1- Ver placar")
        print("2- Jogar")
        print("9- Sair")

        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            print("\nJogador: {jogador} - Pontos: {pontos}".format(jogador=jogador, pontos=pontuacao))
        elif opcao == 2:
            pontos = iteracao_forca(palavras)
            pontuacao += pontos

if __name__ == '__main__':
    menu_principal()