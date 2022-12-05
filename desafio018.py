from math import radians, sin, cos, tan
n = float(input('Digite o valor do seu ângulo: '))
seno = sin(radians(n))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n, seno))
cosseno = cos(radians(n))
print('O ângulo de {} tem o COSSENO de {:.2}'.format(n, cosseno))
tangente = tan(radians(n))
print('O ângulo de {} tem a TANGENTE DE {:.2f}'.format(n, tangente))