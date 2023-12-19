#Letra A
def area_quadrado(exibir):
    lado = int(input('Digite o lado do quadrado:'))
    area = (lado**2)
    print(area)

area_quadrado(exibir=True)
print('*'*20)

#Letra B
def area_triangulo(exibir):
    base = int(input('Qual é a base do triângulo:'))
    altura = int(input('Qual é a altura:'))
    area = int((base * altura)/2)
    print(area)

area_triangulo(exibir=True)