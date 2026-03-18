#Criando uma lista vazia
tarefas = []

def main():
    print("Bem vindo ao Sistema de Gerenciamento de Tarefas!")
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        escolha = input("Digite o número que corresponde a opção desejada: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif escolha == '2':
            visualizar_tarefas()
        elif escolha == '3':
            visualizar_tarefas()
            try: 
              indice = int(input("Digite o número da tarefa que você deseja marcar como concluída: ")) -1
              concluir_tarefa(indice)
            except ValueError:
              print("Entrada inválida! Por favor digite um número: ")  
        elif escolha == '4':
            visualizar_tarefas()
            try:
              indice = int(input("Digite o número da tarefa que você deseja remover: ")) -1
            except ValueError:
              print("Entrada inválida! Por favor digite um número: ")
            remover_tarefa(indice)
        elif escolha == '5':
            print("Saindo do sistema! Até breve!")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

#Criando a função de adicionar tarefa
def adicionar_tarefa(descricao):
    tarefas.append({"descricao" : descricao, "concluída" : False})
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

#Criando a função de visualizar tarefas. Precisa percorrer toda a lista, caso haja algo.
def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa foi encontrada.")
        return
    print("\nLista de Tarefas: ")
    for i, tarefa in enumerate(tarefas):
        status = '[X]' if tarefa["concluída"] else "[ ]"
        print(f"{i + 1}. {status} {tarefa['descricao']}")


#Criando a função de marcar tarefa como concluída
def concluir_tarefa(indice):
    if 0 <= indice <= len(tarefas):
        tarefas[indice]["concluída"] = True
        print(f"Tarefa '{tarefas[indice]['descricao']} foi marcada como concluída!")
    else:
        print("Índice de tarefa inválido!")
    
#Criando a função de remover a tarefa
def remover_tarefa(indice):
    if 0 <= indice <= len(tarefas):
        descricao = tarefas.pop(indice)["descricao"]
        print(f"Tarefa '{descricao}' foi removida com sucesso!")
    else:
        print("Índice de tarefa inválido!")
