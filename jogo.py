from random import *
from time import sleep

valores = ['Pedra', 'Papel', 'Tesoura']
pc = choice(valores)

print('''Escolha um valor:
Pedra[0]
Papel[1]
Tesoura[2]''')
vp = input('>')

sleep(0.5)
print('Jo')
sleep(0.5)
print('Ken')
sleep(0.5)
print('Po')
print(pc)

if pc == 'Pedra' and vp == 0:
    print('Empate')

if pc =='Papel' and vp == 1:
    print('Empate')

if pc == 'Tesoura' and vp == 2:
    print('Empate')


if pc == 'Pedra' and vp == 1:
    print('Você ganhou')

if pc == 'Papel' and vp == 2:
    print('Você ganhou')

if pc == 'Tesoura' and vp == 0:
    print('Você ganhou')


if pc =='Pedra' and vp == 2:
    print('Você perdeu')

if pc == 'Papel' and vp == 0:
    print('Você perdeu')
if pc == 'Tesoura' and vp == 1:
    print('Você perdeu')
