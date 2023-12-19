def exibir_tabuada(operacao):
    for i in range(1, 11):
        if operacao == 'adição':
            resultado = i + num
        elif operacao == 'subtração':
            resultado = i - num
        elif operacao == 'multiplicação':
            resultado = i * num
        elif operacao == 'divisão':
            resultado = i / num

        print(f"{num} {operacao} {i} = {resultado}")

while True:
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '5':
        print("Saindo do programa. Até logo!")
        break
    elif escolha in ('1', '2', '3', '4'):
        num = int(input("Digite um número para a tabuada: "))

        if escolha == '1':
            exibir_tabuada('+')
        elif escolha == '2':
            exibir_tabuada('-')
        elif escolha == '3':
            exibir_tabuada('*')
        elif escolha == '4':
            exibir_tabuada('/')
    else:
        print("Opção inválida. Escolha uma opção válida.")