T = [-10, -8, 0, 1, 2, 5, -2, -4]


menor_temperatura = T[0]
maior_temperatura = T[0]
soma_temperaturas = T[0]


for temperatura in T[1:]:

    if temperatura < menor_temperatura:
        menor_temperatura = temperatura

   
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

    
    soma_temperaturas += temperatura


media_temperaturas = soma_temperaturas / len(T)

print("Menor temperatura:", menor_temperatura)
print("Maior temperatura:", maior_temperatura)
print("Temperatura média:", media_temperaturas)