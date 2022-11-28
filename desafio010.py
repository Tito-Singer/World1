a: float = float(input('Qual seu saldo na carteira? R$'))
b: float = float(a / 3.27)
print("Com R$ {} você pode comprar {:.2f} Dólares".format( a , b))
