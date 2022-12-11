r1 = float(input('Insira o comprimento da reta 1: '))
r2 = float(input('Insira o comprimento da reta 2: '))
r3 = float(input('Insira o comprimento da reta 3: '))
a = (sorted((r1, r2, r3)))
if ((a[0] + a[1]) >= a[2]):
    print('É possível formar um triângulo com estas 3 retas')
else:
    print('Não é possível formar um triângulo com estas 3 retas')
