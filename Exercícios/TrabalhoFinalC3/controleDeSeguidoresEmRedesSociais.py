# Nomes dos integrantes do grupo
integrantes = ["Marcelo", "Vanderson", "Estevao", "Poubs", "Nat"]

# Vetores para os nomes dos usuários e redes sociais
usuarios = []
for i in range (5):
    usuario = str(input("Digite o nome dos usuários: ")).capitalize()
    usuarios.append(usuario)
print(usuarios)

redes = []
for j in range(5):
    rede = str(input("Digite as redes sociais selecionadas: ")).capitalize()
    redes.append(rede)
print(redes) 

def exibir_dados_formatados(usuarios, redes, matriz):
    print("\n=== Controle de Seguidores ===")
    
    # Cabeçalho
    print("Usuário".ljust(12), end="|")
    for rede in redes:
        print(rede.ljust(10), end="|")
    print("Total")  # Coluna de total
    
    # Separador
    print("-" * (12 + 10 * len(redes) + 7))
    
    # Linhas com os dados
    for i in range(len(usuarios)):
        total = sum(matriz[i])  # Calcula o total de seguidores para cada influenciador
        print(usuarios[i].ljust(12), end="|")
        for seguidores in matriz[i]:
            print(str(seguidores).ljust(10), end="|")
        print(total)
          # Exibe o total na última coluna
# Matriz para armazenar o número de seguidores (5 usuários x 4 redes sociais)
''''matriz = []  # Lista para representar a matriz
print("\n=== Registro da quantidade de seguidores ===")
for i in range(len(usuarios)):
    linha = []  # Uma linha da matriz (para um influenciador)
    for j in range(len(redes)):
        seguidores = int(input("Digite a quantidade de seguidores de " + usuarios[i] + " na " + redes[j] + ": "))
        linha.append(seguidores)
    matriz.append(linha)  # Adiciona a linha à matriz
print("\nMatriz inicial criada com sucesso!")'''


