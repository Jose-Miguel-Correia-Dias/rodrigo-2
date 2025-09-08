# atvd 2

def tem_prioridade(idade, gestante, pcd):
    return idade > 60 or gestante == "sim" or pcd == "sim"

# Programa principal
pessoas = []  # lista que vai guardar os dicionários

n = int(input("Quantas pessoas deseja cadastrar? "))

# Cadastro de N pessoas
for i in range(n):
    print(f"\n=== Cadastro da pessoa {i+1} ===")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    gestante = input("É gestante? (sim/não): ").strip().lower()
    pcd = input("É PCD? (sim/não): ").strip().lower()

    # Cria dicionário com os dados da pessoa
    pessoa = {
        "nome": nome,
        "idade": idade,
        "gestante": gestante,
        "pcd": pcd,
        "prioridade": tem_prioridade(idade, gestante, pcd)
    }

    # Coloca dentro da lista
    pessoas.append(pessoa)

# Contagem
prioritarios = sum(1 for p in pessoas if p["prioridade"])
nao_prioritarios = len(pessoas) - prioritarios

print("\n=== Resultado ===")
print(f"Total de pessoas: {len(pessoas)}")
print(f"Prioritários: {prioritarios}")
print(f"Não prioritários: {nao_prioritarios}")

# Remover a primeira pessoa não prioritária (se existir)
for i, p in enumerate(pessoas):
    if not p["prioridade"]:
        print(f"\nRemovendo a primeira pessoa não prioritária: {p['nome']}")
        pessoas.pop(i)  # remove pelo índice
        break

# Mostrar lista final
print("\n=== Lista Final de Pessoas ===")
for p in pessoas:
    print(p)
