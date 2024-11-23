# Cadastro dos influenciadores e redes sociais
usuarios = []  # Lista para guardar os influenciadores
redes = []     # Lista para guardar as redes sociais

# Cadastro dos influenciadores
print("=== Cadastro dos influenciadores ===")
for i in range(2):
    usuario = input("Digite o nome do influenciador " + str(i + 1) + ": ").capitalize()
    usuarios.append(usuario)
print("Usuários cadastrados: ", usuarios)

# Cadastro das redes sociais
print("\n=== Cadastro das redes sociais ===")
for j in range(2):  # Supondo 3 redes sociais
    rede = input("Digite o nome da rede social " + str(j + 1) + ": ").capitalize()
    redes.append(rede)
print("Redes sociais cadastradas: ", redes)

# Criação da matriz para armazenar os seguidores
matriz = []  # Lista para representar a matriz
print("\n=== Registro da quantidade de seguidores ===")
for i in range(len(usuarios)):
    linha = []  # Uma linha da matriz (para um influenciador)
    for j in range(len(redes)):
        seguidores = int(input("Digite a quantidade de seguidores de " + usuarios[i] + " na " + redes[j] + ": "))
        linha.append(seguidores)
    matriz.append(linha)  # Adiciona a linha à matriz
print("\nMatriz inicial criada com sucesso!")
print(matriz)

# Exibição inicial dos dados
print("\n=== Matriz de Seguidores ===")
print(" ", redes)  # Cabeçalho com os nomes das redes sociais
for i in range(len(usuarios)):
    print(usuarios[i], matriz[i])  # Nome do influenciador e dados da matriz

# Funções para manipulação dos dados
def exibir_dados(usuarios, redes, matriz):
    print("\n=== Exibição da Matriz de Seguidores ===")
    print(" ", redes)  # Cabeçalho
    for i in range(len(usuarios)):
        print(usuarios[i], matriz[i])

def editar_seguidores(usuarios, redes, matriz):
    print("\n=== Editar Seguidores ===")
    nome_usuario = input("Digite o nome do influenciador: ").capitalize()
    if nome_usuario in usuarios:
        index_usuario = usuarios.index(nome_usuario)
        nome_rede = input("Digite o nome da rede social: ").capitalize()
        if nome_rede in redes:
            index_rede = redes.index(nome_rede)
            novo_valor = int(input("Digite o novo número de seguidores de " + nome_usuario + " na " + nome_rede + ": "))
            matriz[index_usuario][index_rede] = novo_valor
            print("Valor atualizado com sucesso!")
        else:
            print("Rede social não encontrada.")
    else:
        print("Usuário não encontrado.")

def total_seguidores_por_influenciador(usuarios, matriz):
    print("\n=== Total de Seguidores por Influenciador ===")
    for i in range(len(usuarios)):
        total = sum(matriz[i])
        print("Total de seguidores de", usuarios[i], ":", total)

def total_seguidores_por_rede(redes, matriz):
    print("\n=== Total de Seguidores por Rede Social ===")
    for j in range(len(redes)):
        total = sum(matriz[i][j] for i in range(len(matriz)))
        print("Total de seguidores na rede", redes[j], ":", total)

# Menu principal
while True:
    print("\n=== Menu ===")
    print("1 - Exibir dados")
    print("2 - Editar número de seguidores")
    print("3 - Total de seguidores por influenciador")
    print("4 - Total de seguidores por rede social")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        exibir_dados(usuarios, redes, matriz)
    elif opcao == 2:
        editar_seguidores(usuarios, redes, matriz)
    elif opcao == 3:
        total_seguidores_por_influenciador(usuarios, matriz)
    elif opcao == 4:
        total_seguidores_por_rede(redes, matriz)
    elif opcao == 0:
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")
