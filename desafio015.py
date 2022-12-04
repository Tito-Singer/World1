dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos KM foram percorridos com o carro?'))
vkm = (km * 0.15)
vdias = (dias * 60)
final =  vkm + vdias
print("O valor a pagar é de R${:.2f} \nR${:.2f} referente aos KM rodados \nR${:.2f} referente aos dias alugados".format(final , vkm , vdias))
