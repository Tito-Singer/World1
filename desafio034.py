s = float(input('Qual o salário do funcionário em R$: '))
if s >= 1250:
    print('O salário deste funcionário será R$ {:.2f}'.format(s * 1.1))
else:
    print('O salário deste funcionário será R$ {:.2f}'.format(s * 1.15))