from collections import deque

# Filas
fila_prioritaria = deque()
fila_normal = deque()

# Contadores de atendimento
atendidos_total = 0
atendidos_prioritarios = 0
atendidos_normais = 0

# Função para verificar prioridade
def tem_prioridade(idade, gestante, pcd):
    return idade >= 60 or gestante == "sim" or pcd == "sim"

# Adicionar cliente
def adicionar():
    global fila_prioritaria, fila_normal
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    gestante = input("É gestante? (sim/não): ").strip().lower()
    pcd = input("É PCD? (sim/não): ").strip().lower()

    cliente = {
        "nome": nome,
        "idade": idade,
        "gestante": gestante,
        "pcd": pcd,
        "prioridade": tem_prioridade(idade, gestante, pcd)
    }

    if cliente["prioridade"]:
        fila_prioritaria.append(cliente)
        print(f"{nome} foi adicionado à fila PRIORITÁRIA.\n")
    else:
        fila_normal.append(cliente)
        print(f"{nome} foi adicionado à fila NORMAL.\n")

# Atender próximo cliente
def atender():
    global atendidos_total, atendidos_prioritarios, atendidos_normais

    if fila_prioritaria:
        cliente = fila_prioritaria.popleft()
        atendidos_prioritarios += 1
        print(f"Atendendo prioritário: {cliente['nome']}")
    elif fila_normal:
        cliente = fila_normal.popleft()
        atendidos_normais += 1
        print(f"Atendendo normal: {cliente['nome']}")
    else:
        print("Nenhum cliente na fila.\n")
        return
    
    atendidos_total += 1
    print()

# Listar filas
def listar():
    print("\n=== Fila PRIORITÁRIA ===")
    if not fila_prioritaria:
        print("Vazia")
    else:
        for i, c in enumerate(fila_prioritaria, start=1):
            print(f"{i}. {c['nome']} (Idade: {c['idade']}, Gestante: {c['gestante']}, PCD: {c['pcd']})")

    print("\n=== Fila NORMAL ===")
    if not fila_normal:
        print("Vazia")
    else:
        for i, c in enumerate(fila_normal, start=1):
            print(f"{i}. {c['nome']} (Idade: {c['idade']}, Gestante: {c['gestante']}, PCD: {c['pcd']})")
    print()

# Relatório
def relatorio():
    total_fila = len(fila_prioritaria) + len(fila_normal)
    total_prioritarios = len(fila_prioritaria)
    total_normais = len(fila_normal)

    print("\n=== RELATÓRIO ===")
    print(f"Total atendidos: {atendidos_total}")
    print(f" - Prioritários atendidos: {atendidos_prioritarios}")
    print(f" - Normais atendidos: {atendidos_normais}")
    print(f"Na fila agora: {total_fila} pessoas")
    print(f" - Prioritários: {total_prioritarios}")
    print(f" - Normais: {total_normais}")

    if atendidos_total > 0:
        perc = (atendidos_prioritarios / atendidos_total) * 100
        print(f"% de prioritários atendidos: {perc:.2f}%")
    print()

# Menu principal
def menu():
    while True:
        print("=== MENU ===")
        print("1 - Adicionar cliente")
        print("2 - Atender próximo")
        print("3 - Listar filas")
        print("4 - Relatório")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            atender()
        elif opcao == "3":
            listar()
        elif opcao == "4":
            relatorio()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Executar programa
menu()
