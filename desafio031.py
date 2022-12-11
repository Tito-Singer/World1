v = float(input('Qual a distância, em KM, de sua viagem? '))
if v <= 200:
    print('O valor de sua passagem será R$ {:.2f}'.format(v * 0.5))
else:
    print('O valor de sua passagem será R$ {:.2f}'.format(v * 0.45))