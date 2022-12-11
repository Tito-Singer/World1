from datetime import date
data = int(input('Digite o ano que quer analisar. Se quiser analisar o ano atual, digite 0: '))
if data == 0:
    data = date.today().year
if (data % 4 == 0 and data % 100 != 0) or data % 400 ==0:
    print('Este ano é Bissexto')
else:
    print('Este não é um ano bissexto')
