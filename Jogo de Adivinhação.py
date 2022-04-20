from random import randint
from time import sleep

computador = randint(0, 10)
title = 'Jogo de Adivinha'
by = 'Eliandro  Sérgio'
sb = '-==-'

print('{}'.format(sb*14))
print('{}{}{}'.format(sb*5, title, sb*5))
print('{}'.format(sb*14))
print('{}{}{}'.format(sb*5, by, sb*5))
print('{}'.format(sb*14))

print('\nVou pensar num número entre 0 e 10. Tente adivinhar... ')
print('{}'.format(sb*14))

jogador = int(input('Em que número eu pensei? '))
print('POCESSANDO...')
sleep(2)

if jogador == computador:
    print('Parabéns, você me venceu!')
    sn = input('\nQuer jogar novamente (s/n)? ')
else:
    print('GANHEI! Eu pensei no múmero {} e não no número {}.'.format(computador, jogador))
    sn = input('\nQuer jogar novamente (s/n)? ')

while (sn == 's'):
    print('{}'.format(sb * 14))
    print('\nVou pensar num número entre 0 e 10. Tente adivinhar... ')
    print('{}'.format(sb * 14))

    jogador = int(input('Em que número eu pensei? '))
    print('POCESSANDO...')
    sleep(2)

    if jogador == computador:
        print('Parabéns, você me venceu!')
        sn = input('\nQuer jogar novamente (s/n)? ')
    else:
        print('GANHEI! Eu pensei no múmero {} e não no número {}.'.format(computador, jogador))
        sn = input('\nQuer jogar novamente (s/n)? ')

if sn == 'n':
    print('\nFim de jogo!')
