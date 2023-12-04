import random

def tornar():
    tornar_input = int(input('Qual carta deseja jogar? Primeira(1), Segunda(2), Terceira(3): '))
    return tornar_input

jogar = str(input('Bem vindo, deseja jogar? Sim(s) Não(n): '))

if jogar.lower() == 's':
    print('==========================================================')
    naipes = ['bebo', 'zap', 'espadas', 'copas']
    cartas = ['As', 2, 3, 4, 5, 6, 7, 'Rainha', 'Valete', 'Rei']
    
    # Escolha aleatória da "vira"
    vira = random.choice(cartas)
    print(f'A vira é {vira}')

    # Get the index of vira
    indice = cartas.index(vira)

    # Calculate the index of manilha (one position after vira, circular)
    indice_manilha = (indice + 1) % len(cartas)
    
    # Print the manilha
    print(f'A manilha é: {cartas[indice_manilha]}')

    # create a list of all cards and types
    lista = []
    for carta in cartas:
        for naipe in naipes:
            lista.append(f'{carta}:{naipe}')

    # shuffle the cards
    random.shuffle(lista)

    # create your hand cards
    hand = random.sample(lista, k=3)
    print('Suas cartas são', f'{hand}')

    # enemy cards
    enemy_hand = [card for card in lista if card not in hand]
    enemy_hand = random.sample(enemy_hand, k=3)


    print('-------------------------')
    jogada = tornar()
    print('-------------------------')

    if jogada == 1:
        print('Você jogou: ', hand[0])
    elif jogada == 2:
        print('Você jogou: ', hand[1])
    elif jogada == 3:
        print('Você jogou: ', hand[2])
    else:
        print('Informe uma carta válida')

    print(f'O adversário jogou: {enemy_hand[0]}')

else:
    print('Desligando o jogo...')
