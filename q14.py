def valor(param1):
    print(f'param1 antes é: {param1}')
    param1 = 20
    print(f'param1 agora é: {param1}')

x = 10
valor(x)
print(f'O (x) ainda contiuna sendo: {x}')

def referencia(lista):
    print(f'A lista antes é: {lista}')
    lista = [1, 2, 3]
    print(f'A lista depois é: {lista}')

y = [4, 5, 6]
referencia(y)
print(f'O (y) continou sendo: {y}')