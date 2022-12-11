cidade = str(input('Digite o nome de uma cidade: ')).strip()
n = (cidade.upper().split())
if 'SANTO' in (n[0]):
    print('Esta cidade começa com nome de Santo!')
else:
    print('Esta cidade não começa com Santo :,/')
