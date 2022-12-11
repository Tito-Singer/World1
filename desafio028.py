import random
nome = str(input('Olá! Sou o mini-game. Qual seu nome? ')).strip().capitalize().split()
ola = str(input('{}, vamos jogar um jogo? (Digite S ou N):'.format(nome[0]))).upper()
n = random.randint(0 , 5)
if ola == 'S':
    num = int(input('Eu pensei num número! Digite um número inteiro entre 0 e 5 e veja se descobre. Digite seu numero:'))
    if num == n:
        print('Parabéns, {}! Você é um Gênio! Me venceu!'.format(nome[0]))
    else:
        print('Tente novamente, {}! Ainda não foi dessa vez!'.format(nome[0]))
else:
    print('Que pena, {}. Eu gostaria de jogar contigo.'.format(nome[0]))

