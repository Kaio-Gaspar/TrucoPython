import random
import sys, time
import colorama as cl
import numpy as np
cl.init()
def mostrar_cartas(hand):
    if len(hand) == 3:
        while True:
            try:
                tornar_input1 = int(input(cl.Fore.YELLOW + 'Qual carta deseja jogar? Primeira(1), Segunda(2), Terceira(3): ' + cl.Style.RESET_ALL))
                if tornar_input1 not in [1, 2, 3]:
                    print(cl.Fore.MAGENTA + 'Insira uma resposta válida.' + cl.Style.RESET_ALL)
                else:
                    return tornar_input1
            except ValueError:
                print(cl.Fore.MAGENTA + 'Insira um número inteiro válido.' + cl.Style.RESET_ALL)

    elif len(hand) == 2:
        while True:
            try:
                tornar_input2 = int(input(cl.Fore.YELLOW + 'Qual carta deseja jogar? Primeira(1), Segunda(2): ' + cl.Style.RESET_ALL))
                if tornar_input2 not in [1, 2]:
                    print(cl.Fore.MAGENTA + 'Insira uma resposta válida.' + cl.Style.RESET_ALL)
                else:
                    return tornar_input2
            except ValueError:
                print(cl.Fore.MAGENTA + 'Insira um número inteiro válido.' + cl.Style.RESET_ALL)

    elif len(hand) == 1:
        while True:
            try:
                tornar_input3 = int(input(cl.Fore.YELLOW + 'Qual carta deseja jogar? Primeira(1): '+ cl.Style.RESET_ALL))
                if tornar_input3 != 1:
                    print(cl.Fore.MAGENTA + 'Insira uma resposta válida.' + cl.Style.RESET_ALL)
                else:
                    return tornar_input3
            except ValueError:
                print(cl.Fore.MAGENTA + 'Insira um número inteiro válido.' + cl.Style.RESET_ALL)

    else:
        print(cl.Fore.MAGENTA + 'Insira uma resposta válida.' + cl.Style.RESET_ALL)
        return mostrar_cartas(hand)


# def tornar(hand):
#     print('Suas cartas são', f'{hand}')
#     tornar_input = int(input('Qual carta deseja jogar? Primeira(1), Segunda(2), Terceira(3): '))
#     return tornar_input

# def segundo_tornar(hand):
#     print('Suas cartas são', f'{hand}')
#     tornar_input2 = int(input('Qual carta deseja jogar? Primeira(1), Segunda(2): '))
#     return tornar_input2

# def terceiro_tornar(hand):
#     print('Suas cartas são', f'{hand}')
#     tornar_input3 = int(input('Qual carta deseja jogar? Primeira(1): '))
#     return tornar_input3


def segunda_rodada(jogada, hand):
    if jogada == 1:
        print('||Você jogou: ', hand[0])
        jogada_indice = 0
    elif jogada == 2:
        print('||Você jogou: ', hand[1])
        jogada_indice = 1
    else:
        print('||Informe uma carta válida')
        jogada_indice = None
        return segunda_rodada()
    return jogada_indice


def terceira_rodada(jogada, hand):
    if jogada == 1:
        print('||Você jogou: ', hand[0])
        jogada_indice = 0
    else:
        print('||Informe uma carta válida')
        jogada_indice = None
    return jogada_indice

def mostrar_pontos(seus_pontos, enemy_pontos):
    print(cl.Fore.RED +'||')
    print('||')
    print(f'||Você tem {seus_pontos} pontos')
    print(f'||O adversário tem {enemy_pontos} pontos')
    print('+==========================================+')

def trucar(truco, truco_enemy):
    if truco > 1 or truco_enemy > 1:
        pass
    else:
        pedir_truco = input(cl.Fore.YELLOW + 'Vôce deseja pedir TRUCO?  (s)sim (n)não: ' + cl.Style.RESET_ALL)
        if pedir_truco.lower() == 's':
            truco = 2
            print_slow(cl.Fore.LIGHTYELLOW_EX + 'T R U C O !' + cl.Style.RESET_ALL )
        elif pedir_truco.lower() == 'n':
            truco = 0
        else:
            print(cl.Fore.MAGENTA + 'Insira uma resposta válida.' + cl.Style.RESET_ALL)
            return trucar(truco)
            
    return truco

def print_slow(str):
    for letra in str + '\n':
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.05)

#def checar_jogada(jogada, hand):
    #if jogada > 3 or  jogada < 1:
      #  return mostrar_cartas(hand)
        
        
#------------------PROB----------------------

import numpy as np

def truco_inimigo(truco, truco_enemy):
    prob_7prc = list(np.arange(1, 3))
    if truco < 1 and truco_enemy < 1:
        prob_choice = np.random.choice(prob_7prc)
        if prob_choice == 2:
            print_slow('\033[91m' + 'Adversário pediu T R U C O !\n' + '\033[0m')
            resposta = input(cl.Fore.YELLOW + 'Você deseja pedir TRUCO? (s) Sim / (n) Não: ' + cl.Style.RESET_ALL)
            if resposta.lower() == 's':
                truco_enemy = 2
                print(cl.Fore.LIGHTYELLOW_EX + 'T R U C O !' + cl.Style.RESET_ALL)
            else:
                print(cl.Fore.YELLOW + 'Você correu!' + cl.Style.RESET_ALL)
                truco_enemy = -1  # Marcador para indicar que o jogador perdeu o round
    return truco_enemy


