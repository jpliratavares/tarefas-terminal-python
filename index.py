import json

# --- Persistência ---

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            conteudo = f.read()
            if conteudo.strip() == "":
                return []
            return json.loads(conteudo)
    except FileNotFoundError:
        return []

def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

# --- Funções do sistema ---

def adicionar_tarefa():
    tarefa = input("Que tarefa deseja adicionar? ")
    nova = {"Tarefa": tarefa, "Status": "Pendente"}
    tarefas.append(nova)
    salvar_tarefas()

def listar_tarefas():
    if tarefas:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa['Tarefa']} [{tarefa['Status']}]")
    else:
        print("Nenhuma tarefa cadastrada.")

def marcar_concluida():
    listar_tarefas()
    try:
        num = int(input("Qual tarefa deseja marcar como concluída? "))
        tarefas[num - 1]["Status"] = "Concluído"
        salvar_tarefas()
    except:
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()
    try:
        num = int(input("Qual tarefa deseja remover? "))
        tarefas.pop(num - 1)
        salvar_tarefas()
        print("Tarefa removida.")
    except:
        print("Número inválido.")

# --- Início do programa
tarefas = carregar_tarefas()

while True:
    print("\n[1] Adicionar tarefa\n[2] Ver tarefas\n[3] Marcar como feita\n[4] Remover tarefa\n[5] Sair")
    opcao = input("→ ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida.")
