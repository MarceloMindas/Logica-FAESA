#declara um vertor/lista vazia com o nome alunos
aluno = []

#declara uma lista já preenchida com dados
#exemplo1
alunos = ['paulo', 'maria', 'mario', 'ana', 'jose']

#exemplo2
aluno.append('paulo')
aluno.append('maria')
aluno.append('mario')
aluno.append('ana')
aluno.append('jose')

#declara uma lista e preenche os dados via teclado
'''alunos = []
for i in range(5):
    alunos.append(input("Digite um nome: "))
'''
#exetend = insere novos dadosem uma lista que já tem dados
alunos.extend(['beth', 'paulo'])

#comando para mostrar o conteudo da lista
print(alunos)

#sort = função para rordenar os dados dentro da lista
alunos.sort()
print("Ordenou a lista")
print(alunos)

#len = mostrar o tamanho da lista
print("tamanho da lsita")
print(len(alunos))

#pop = função para remover um elemento da lista pela sua posição
alunos.pop(2) #2 é a posição na lista
print("Depois do pop: ")
print(alunos)
#se não colocar nenhum número no parentises, remove o ultimo elemento
alunos.pop()
print(alunos)

#ou
#de1 = também apaga um elemento pela posição na lista
#se colocar assim "del aluno" exclui a lista inteira

#remove = exclui valores ou objeto da lista usando valor
#exemplo1: o usuário digita o valor que seria removido
alunos.remove(input("Digite um nome para remover: "))
print("Depois do remove\n",alunos)

#:  valor a ser removido está fixo no código
alunos.remove("paulo")
print(alunos)

#trexo para pesquisar se um nome está na lista
nome = input("Digite o nome a ser procurado: ")
achou = False
for i in alunos:
        if i == nome:
              print("o nome está na lista")
              achou = True
              break
if achou == False:
      print("o nome não está na lista")

#index = função para procurar o incidice de um dado na lista
indice = alunos.index('beth')
print(indice, " é o indice do dado procurado")

#try-except = tratamento de exceção
try:
       indice = alunos.index('nana')
except:
       print("O nome não está na lista")

#techo para remover dados repetidos na lista
print()
print("nova lista com letras")
lista = ['A', 'S', 'C', 'S', 'N', 'D', 'E', 'R', 'S']
print("Lista original: ", lista)
for i in lista:
       if i == 'S':
              lista.remove("S")
print("Removeu os elementos S: ", lista)

    