v = int(input('Digite a velocidade do carro: '))
if v >= 80.0:
    print('Você foi Multado!')
    print('O valor da sua multa é R$ {:.2f}'.format((v-80)*7))
else:
    print('Você está dentro do limite de velocidade.')