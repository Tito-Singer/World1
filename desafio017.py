import math
c1 = float(input('Digite o valor do Cateto 1: '))
c2 = float(input('Digite o valor do Cateto 2: '))
h = math.hypot(c1, c2)
print('A hipotenusa dos catetos {} e {} é {:.2f}'.format(c1, c2, h))
