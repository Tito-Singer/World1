a = float(input('Digite o valor em metros:'))
dm = a * 10
cm = a * 100
mm = a * 1000
dam = a / 10
hm = a / 100
km = a / 1000
print('O valor de {}m convertido em cada unidade é:\n{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm'.format(a , km , hm , dam , dm , cm , mm))
