def ordenacao_por_selecao(lista):
    n = len(lista)

    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


lista = [7, 4, 3, 12, 8]

print("Lista original:", lista)

ordenacao_por_selecao(lista)

print("Lista ordenada:", lista)