# coding: utf-
import random

def buscar_palavras_arquivo(filename:str) -> list:
    """
    recebe como parâmetro a localização o arquivo \n
    retorna uma lista de palavras
    """
    try:
        with open(filename, 'rt') as file:
            lista = file.read()
    except:
        print("Não foi possível abrir o arquivo.")

    lista = lista.split('\n')

    return lista

def iteracao_forca(palavras: list) -> int:
    palavra = random.choice(palavras).upper()
    codificada = list('_' * len(palavra))

    print('\nA Palavra é:', ' '.join(codificada))

    pontos = 0
    tentativas = 0
    while True:
        letra = input('\ndigite uma letra ').upper()

        if letra in palavra:
        
            for index, l in enumerate(palavra):
                if letra == l:
                    codificada[index] = letra
                    pontos += 10
        
            print('A Palavra é:', ' '.join(codificada))

            if ''.join(codificada) == palavra:
                print('\nGanhou :)')
                pontos += 20
                break
        
        else:
            tentativas += 1
            print('\nVoce errou pela {} vez'.format(tentativas))
            pontos -= 5
    
            if tentativas >=6:
                print('\nMorreu')
            break

    return pontos