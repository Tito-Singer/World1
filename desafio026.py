plv = str(input('Digite uma frase bem bonita: '))
print('A letra "a" aparece {} vezes em sua bela frase'.format((plv.lower()).count('a')))
print('A Primeira vez que a letra "a" em sua frase é no {}º caractere'.format((plv.lower()).find('a')+1))
print('A Ultima vez que a letra "a" em sua frase é no {}º caractere'.format((plv.lower()).rfind('a')+1))