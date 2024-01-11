import random
import colorama as cl
cl.init()
def mostrar_cartas(hand):
    
    if len(hand) == 3:
        tornar_input = int(input(cl.Fore.YELLOW + 'Qual carta deseja jogar? Primeira(1), Segunda(2), Terceira(3): ' + cl.Style.RESET_ALL))
        return tornar_input
    elif len(hand) == 2:
        tornar_input2 = int(input(cl.Fore.YELLOW + 'Qual carta deseja jogar? Primeira(1), Segunda(2): ' + cl.Style.RESET_ALL))
        return tornar_input2
    elif len(hand) == 1:
        tornar_input3 = int(input(cl.Fore.YELLOW + 'Qual carta deseja jogar? Primeira(1): '+ cl.Style.RESET_ALL))
        return tornar_input3


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

def trucar(truco):
    if truco > 1:
        pass
    else:
        pedir_truco = input(cl.Fore.YELLOW + 'Vôce deseja pedir TRUCO?  (s)sim (n)não: ' + cl.Style.RESET_ALL)
        if pedir_truco.lower() == 's':
            truco = 2
        elif pedir_truco.lower() == 'n':
            truco = 0
        else:
            print(cl.Fore.MAGENTA + 'Insira uma resposta válida.' + cl.Style.RESET_ALL)
            return trucar(truco)
            
    return truco
