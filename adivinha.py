from random import randint
from emoji import emojize
from playsound import playsound
from time import sleep

#Cores
verde = '\033[1;34;32m'
vermelho = '\033[1;33;31m'
resete =  '\033[0;0m'

em = emojize(':smile:', language = 'alias')

e = int (input('O Computador pensou em um número entre 1 e 6...\N{thinking face}\nTente adivinhar qual número foi: '))

pc = randint(1,6)

print('\nCARREGANDO...\n')

sleep(3)
if e==pc:
    print("{}Acertou!{}{}".format(verde, resete, em))
    playsound('C:/Users/theod/OneDrive/Área de Trabalho/Projetos/Python/uma ideia que tive de madrugada/Acertou.mp3')
else: 
    print("{}Errou... \U0001F923 era o número {}{}".format(vermelho, pc, resete))
    playsound('C:/Users/theod/OneDrive/Área de Trabalho/Projetos/Python/uma ideia que tive de madrugada/Errou.mp3')