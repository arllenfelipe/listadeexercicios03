soma = 0
quantidade = 0

while True:
    numero = int(input('Digite um números(ou 0 para parar):'))
    if numero == 0:
        break

    soma += numero
    quantidade += 1

if quantidade >0:
    media = soma/quantidade
    print(f'\nQuantidade de números digitados foi:{quantidade}')
    print(f'Soma dos números digitados:{soma}')
    print(f'A média aritmética dos números digitados foi: {media}')
else:
    print('Nenhum número foi digitado')