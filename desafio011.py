lar = float(input('Qual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
area = float(lar * alt)
tinta = float(area / 2)
print('Sua parede tem dimensão de {}m x {}m, área de {} m2 e serão necessárias {} litro(s) para pintá-la.'.format( lar , alt , area, tinta))
