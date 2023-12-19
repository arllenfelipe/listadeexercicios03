def grito_de_natal_animado(N):
    if N <= 1:
        return "“Feliz Nataal!!”)"
    elif N <= 5:
        return "“Feliz Nataaaaal!!”"
    elif N <= 10:
        return '“Feliz Nataaaaaaaaaal!!”'
    


felicidade = 2
print(grito_de_natal_animado(felicidade))

felicidade = 5
print(grito_de_natal_animado(felicidade))

felicidade = 10
print(grito_de_natal_animado(felicidade))