#Letra A
lista = list(range(1, 100))
print(lista)
#Letra B
lista2 = list(range(50, 102, 2))
print(lista2)
#Letra C
x = 10
while x >= 1:
    print(x)
    x = x -1   
print("E fogo!")
#Letra D
numero = int(input('Digite um número:'))
par_ou_impar = input("Você quer ver os nummeros 'par' ou 'impar'?")
if par_ou_impar == 'par':
    for i in range(2, numero + 1,2):
        print(i)
elif par_ou_impar == 'impar':
    for i in range(1, numero + 1,2):
        print(i)
else:
    print('escolha "par" ou "impar" !')