# atvd 1

def cadastro():
    print("=== Cadastro de Pessoa ===")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    gestante = input("É gestante? (sim/não): ").strip().lower()
    pcd = input("É PCD? (sim/não): ").strip().lower()

    # Verifica se tem prioridade
    prioridade = False
    if idade > 60 or gestante == "sim" or pcd == "sim":
        prioridade = True

    print("\n=== Resultado do Cadastro ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Gestante: {gestante}")
    print(f"PCD: {pcd}")
    print(f"Prioridade: {'SIM' if prioridade else 'NÃO'}")

# Executa o programa
cadastro()
