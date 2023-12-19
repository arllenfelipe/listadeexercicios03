lista_de_tarefas = []

def adicionar_tarefa(tarefa):
    lista_de_tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso.')

def exibir_tarefa():
    if lista_de_tarefas:
        print('Lista de Tarefas:')
        for tarefa in lista_de_tarefas:
            print(f' - {tarefa}')
    else:
        print('A lista de tarefas está vazia.')

adicionar_tarefa('lavar a louça')
adicionar_tarefa("fazer exercícios")
adicionar_tarefa("estudar pra prova")

exibir_tarefa()