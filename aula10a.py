print('Bem-vindo ao calculador de médias')
nome = str(input('Qual é seu nome? ')).strip().upper().split()
if nome[0] == 'TITO':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}! Vamos começar:'.format(nome[0]))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns! Você foi aprovado!')
else:
    print('Infelizmente você não foi aprovado dessa vez. Estude mais!')
