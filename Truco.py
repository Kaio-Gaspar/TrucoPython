import random
from truco_modulo import *
import colorama as cl

cl.init() 

# Inicialização das variáveis de pontos fora do loop
seus_pontos = 0
enemy_pontos = 0
enemy_pontos_de_jogo = 0
seus_pontos_de_jogo = 0
jogar = str(input(cl.Fore.LIGHTRED_EX + 'Bem-vindo, deseja jogar? Sim(s) Não(n): '))

if jogar.lower() == 's':
    while True:
        print(cl.Fore.RED + '==========================================================')
        naipes = ['Paus', 'Ouros', 'Espadas', 'Copas']
        cartas = ['A', 2, 3, 4, 5, 6, 7, 'Q', 'J', 'K']
        

        while seus_pontos < 12 and enemy_pontos < 12:
            truco = 0
            
            
            cartas_valores = {'A:Paus': 11, 'A:Ouros': 11, 'A:Espadas': 11, 'A:Copas': 11,
                          '2:Paus': 12, '2:Ouros': 12, '2:Espadas': 12, '2:Copas': 12,
                          '3:Paus': 13, '3:Ouros': 13, '3:Espadas': 13, '3:Copas': 13,
                          '4:Paus': 4, '4:Ouros': 4, '4:Espadas': 4, '4:Copas': 4,
                          '5:Paus': 5, '5:Ouros': 5, '5:Espadas': 5, '5:Copas': 5,
                          '6:Paus': 6, '6:Ouros': 6, '6:Espadas': 6, '6:Copas': 6,
                          '7:Paus': 7, '7:Ouros': 7, '7:Espadas': 7, '7:Copas': 7,
                          'Q:Paus': 8, 'Q:Ouros': 8, 'Q:Espadas': 8, 'Q:Copas': 8,
                          'J:Paus': 9, 'J:Ouros': 9, 'J:Espadas': 9, 'J:Copas': 9,
                          'K:Paus': 10, 'K:Ouros': 10, 'K:Espadas': 10, 'K:Copas': 10}
            # Escolha aleatória da "vira"
            vira = random.choice(cartas)
            print(f'A vira é {vira}')
            # Get the index of vira
            indice = cartas.index(vira)
            # Calculate the index of manilha (one position after vira, circular)
            indice_manilha = (indice + 1) % len(cartas)
            manilha = cartas[indice_manilha]
            # Print the manilha
            print(cl.Fore.YELLOW + cl.Back.RED + f'A manilha é: {manilha}' + cl.Style.RESET_ALL)
            cartas_valores[f'{manilha}:Ouros'] = 14
            cartas_valores[f'{manilha}:Espadas'] = 15
            cartas_valores[f'{manilha}:Copas'] = 16
            cartas_valores[f'{manilha}:Paus'] = 17

        
            # create a list of all cards and types
            lista = []
            for carta in cartas:
                for naipe in naipes:
                    lista.append(f'{carta}:{naipe}')
            # shuffle the cards
            random.shuffle(lista)
            # create your hand cards
            hand = random.sample(lista, k=3)
            # print('Suas cartas são', f'{hand}')
            # enemy cards
            enemy_hand = [card for card in lista if card not in hand]
            enemy_hand = random.sample(enemy_hand, k=3)
            print(cl.Fore.LIGHTCYAN_EX + '-------------------------------------------')
            print('Suas cartas são', f'{hand}')
            truco = trucar(truco)
            jogada = mostrar_cartas(hand)
            # jogada = tornar(hand)
            print(cl.Fore.RED + '+==========================================+')

            if jogada == 1:
                print('||Você jogou: ', hand[0])
                jogada_indice = 0
            elif jogada == 2:
                print('||Você jogou: ', hand[1])
                jogada_indice = 1
            elif jogada == 3:
                print('||Você jogou: ', hand[2])
                jogada_indice = 2
            else:
                print('||Informe uma carta válida')
                jogada_indice = None

            print(f'||O adversário jogou: {enemy_hand[0]}')
            print('||')
            if cartas_valores[hand[jogada_indice]] > cartas_valores[enemy_hand[0]]:
                print('||'+ cl.Fore.LIGHTMAGENTA_EX + cl.Back.GREEN + '+++++++++++++++Você ganhou!!!+++++++++++++' + cl.Style.RESET_ALL)
                seus_pontos += 1
            elif cartas_valores[hand[jogada_indice]] < cartas_valores[enemy_hand[0]]:
                print('||' + cl.Back.RED+ '+++++++++++++++Você perdeu.+++++++++++++++' + cl.Style.RESET_ALL)
                enemy_pontos += 1
            else:
                print(cl.Back.BLUE +'||Empate!' + cl.Style.RESET_ALL)
            hand.pop(jogada_indice)
            mostrar_pontos(seus_pontos, enemy_pontos)
            print(cl.Back.YELLOW+'~~~~~~~~~~~~~~~~SEGUNDA RODADA~~~~~~~~~~~~~~'+ cl.Style.RESET_ALL)
            print(cl.Fore.LIGHTCYAN_EX + 'Suas cartas são', f'{hand}')
            truco = trucar(truco)
            jogada = mostrar_cartas(hand)
            print(cl.Fore.RED+'+==========================================+')
            jogada_indice = segunda_rodada(jogada, hand)

            print(f'||O adversário jogou: {enemy_hand[0]}')
            print('||')
            if cartas_valores[hand[jogada_indice]] > cartas_valores[enemy_hand[0]]:
                print('||'+ cl.Fore.LIGHTMAGENTA_EX + cl.Back.GREEN + '+++++++++++++++Você ganhou!!!+++++++++++++' + cl.Style.RESET_ALL)
                seus_pontos += 1
            elif cartas_valores[hand[jogada_indice]] < cartas_valores[enemy_hand[0]]:
                print('||' + cl.Back.RED+ cl.Fore.LIGHTMAGENTA_EX + '+++++++++++++++Você perdeu.+++++++++++++++' + cl.Style.RESET_ALL)
                enemy_pontos += 1
            else:
                print(cl.Back.BLUE +'||Empate!' + cl.Style.RESET_ALL)

            mostrar_pontos(seus_pontos, enemy_pontos)
            if seus_pontos and enemy_pontos >= 2:
                seus_pontos = 0
                seus_pontos_de_jogo += 1 + truco
                enemy_pontos = 0
                enemy_pontos_de_jogo += 1 + truco
                print('-Rodada empatada-')
            elif seus_pontos == 2:
                seus_pontos = 0
                enemy_pontos = 0
                seus_pontos_de_jogo += 1 + truco
                print('-Você venceu a rodada.-')
            elif enemy_pontos == 2:
                enemy_pontos = 0
                seus_pontos = 0
                enemy_pontos_de_jogo += 1 + truco
                print('-O adversário venceu a rodada.-')
            else:
                enemy_hand.pop(0)
                hand.pop(jogada_indice)
                print(cl.Back.YELLOW +'~~~~~~~~~~~~~~~~TERCEIRA RODADA~~~~~~~~~~~~~~' + cl.Style.RESET_ALL)
                print(cl.Fore.LIGHTCYAN_EX +'Suas cartas são', f'{hand}')
                truco = trucar(truco)
                jogada = mostrar_cartas(hand)
                print(cl.Fore.RED + '+==========================================+')

                jogada_indice = terceira_rodada(jogada, hand)
                print(f'||O adversário jogou: {enemy_hand[0]}')
                print('||')
                if cartas_valores[hand[0]] > cartas_valores[enemy_hand[0]]:
                    print('||'+ cl.Fore.BLACK + cl.Back.GREEN + '+++++++++++++++Você ganhou!!!+++++++++++++' + cl.Style.RESET_ALL)
                    seus_pontos_de_jogo += 1 + truco
                    seus_pontos = 0
                    enemy_pontos = 0
                elif cartas_valores[hand[0]] < cartas_valores[enemy_hand[0]]:
                    print('||' + cl.Back.RED+ '+++++++++++++++Você perdeu.+++++++++++++++' + cl.Style.RESET_ALL)
                    enemy_pontos_de_jogo += 1 + truco
                    enemy_pontos = 0
                    seus_pontos = 0
                else:
                    print(cl.Back.BLUE +'||Empate!' + cl.Style.RESET_ALL)
                    enemy_pontos_de_jogo += 1 
                    seus_pontos_de_jogo += 1 
                    seus_pontos = 0
                    enemy_pontos = 0
                print(cl.Fore.RED+'||')
                print('+==========================================+')
            print(cl.Fore.CYAN + '+*****************************************************+')
            print(f'||Você venceu {seus_pontos_de_jogo} rodadas.')
            print(f'||O adversário venceu {enemy_pontos_de_jogo} rodadas.')
            print('+*****************************************************+')
            if seus_pontos_de_jogo >= 12:
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                print('Parabéns, você ganhou!!!')
                seus_pontos_de_jogo = 0
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            elif enemy_pontos_de_jogo >= 12:
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                print('Você perdeu!!!')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                enemy_pontos_de_jogo = 0
            
            jogar_novamente = input(cl.Fore.RED + 'Deseja jogar continuar? Sim(s) Não(n): ')
            if jogar_novamente.lower() != 's':
                print('Desligando o jogo...')
                break
else:
    print('Desligando o jogo...')
    # 
