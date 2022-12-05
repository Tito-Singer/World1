n = int(input('Digite um número entre 0 a 9999: '))
if n in range(0, 9999):
    print ("{} está no intervalo!".format(n))
else:
    print ("{} não consta no intervalo!".format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analizando o numero {}....'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
