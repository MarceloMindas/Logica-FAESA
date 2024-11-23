# Cadastro de influenciadores
usuarios = []

for i in range(2):
    usuario = str(input("Digite os influenciadores: ")).capitalize()
    usuarios.append(usuario)
print(usuarios)

# Cadastro de redes sociais
redes = [] 
for j in range(2):
    rede = str(input("Digite as redes sociais selecionadas: ")).capitalize()
    redes.append(rede)
print(redes)

# Matriz para armazenar o número de seguidores (2 usuários x 2 redes sociais)
matriz = []
for i in range(len(usuarios)):
    linha = []
    print("Usuário:", usuarios[i])  # Exibe o nome do usuário
    for j in range(len(redes)):
        seguidores = int(input("Digite os seguidores de " + usuarios[i] +  " em " + redes[j] + ": "))
        linha.append(seguidores)
    matriz.append(linha)

# Menu inicial
print("=== Gerenciamento de Seguidores ===")
print("Grupo:", ', '.join(usuarios))

while True:
    print("\n1. Exibir Dados")
    print("2. Alterar Dados")
    print("3. Pesquisar Dados")
    print("4. Cadastrar Usuario")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:  # Exibir dados
        coluna_largura = 12  # Largura de cada coluna

        # Cabeçalho da tabela
        print("=== Controle de Seguidores ===")
        print("Usuário".ljust(coluna_largura), end="| ")
        for rede in redes:
            print(rede.ljust(coluna_largura), end="| ")
        print("Total".ljust(coluna_largura))  # Coluna para o total
        print("-" * (coluna_largura * (len(redes) + 2) + 3 * (len(redes) + 1)))

        # Dados da tabela
        for i, usuario in enumerate(usuarios):
            print(usuario.ljust(coluna_largura), end="| ")
            total = 0
            for seguidores in matriz[i]:
                total += seguidores
                print(str(seguidores).ljust(coluna_largura), end="| ")
            print(str(total).ljust(coluna_largura))

    elif opcao == 2:  # Alterar dados
        print("\n=== Alterar Dados ===")
        usuario = input("Digite o nome do usuário: ").capitalize()
        if usuario not in usuarios:
            print("Usuário não encontrado!")
            continue
        index = usuarios.index(usuario)
        print("Redes sociais:", ', '.join(redes))
        for i in range(len(redes)):
            novo_valor = int(input("Digite os seguidores para " + redes[i] + ": "))
            matriz[index][i] = novo_valor
        print("Dados atualizados com sucesso!")

    elif opcao == 3:  # Pesquisar dados
        print("\n=== Pesquisar Dados ===")
        print("1. Pesquisar por usuário")
        print("2. Pesquisar por rede social")
        pesquisa_opcao = int(input("Escolha uma opção: "))
        if pesquisa_opcao == 1:
            usuario = input("Digite o nome do usuário: ").capitalize()
            if usuario not in usuarios:
                print("Usuário não encontrado!")
                continue
            index = usuarios.index(usuario)
            print("Dados de", usuario, ":", matriz[index])
        elif pesquisa_opcao == 2:
            rede = input("Digite o nome da rede social: ").capitalize()
            if rede not in redes:
                print("Rede social não encontrada!")
                continue
            index = redes.index(rede)
            dados_rede = [matriz[i][index] for i in range(len(usuarios))]
            print("Dados para", rede, ":", dados_rede)

        else:
            print("Opção inválida!")

    elif opcao == 4:  # Cadastrar novo usuário
        print("\n=== Cadastro de Novo Usuário ===")
        novoUsuario = str(input("Digite o novo usuário: ")).capitalize()
        if novoUsuario in usuarios:
            print("Usuário já cadastrado!")
        else:
            usuarios.append(novoUsuario)  # Adiciona o usuário à lista de usuários
            novaLinha = []
            for rede in redes:
                seguidores = int(input("Digite os seguidores de " + novoUsuario + " na rede " + rede + ": "))
                novaLinha.append(seguidores)
            matriz.append(novaLinha)  # Adiciona a nova linha de seguidores à matriz
            print("Usuário cadastrado com sucesso!")

    elif opcao == 5:  # Sair
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")
