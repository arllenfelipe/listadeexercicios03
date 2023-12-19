def contem_item(lista, item):
    return item in lista

def unir_listas_sem_repeticao(lista1, lista2):
    resultado = []

    for item in lista1 + lista2:
        if not contem_item(resultado, item):
            resultado.append(item)

    return resultado


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

lista_resultante = unir_listas_sem_repeticao(lista1, lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista resultante sem repetição:", lista_resultante)