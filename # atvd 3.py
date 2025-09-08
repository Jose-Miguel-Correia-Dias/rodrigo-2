# atvd 3

pessoas = []

# Função para adicionar pessoa
def adicionar():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)
    print(f"{nome} foi adicionado com sucesso!\n")

# Função para listar pessoas
def listar():
    if not pessoas:  # se a lista estiver vazia
        print("Nenhuma pessoa cadastrada.\n")
    else:
        print("\n=== Lista de Pessoas ===")
        for i, p in enumerate(pessoas, start=1):
            print(f"{i}. Nome: {p['nome']}, Idade: {p['idade']}")
        print()

# Função principal com menu
def menu():
    while True:
        print("=== MENU ===")
        print("1 - Adicionar pessoa")
        print("2 - Listar pessoas")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            print("Saindo do programa...")
            break  # encerra o while
        else:
            print("Opção inválida! Tente novamente.\n")

# Executar o menu
menu()
