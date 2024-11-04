#versaoprova
idade = -1
totIdade = 0
profissional = ''
totProfissional = 0
media = 0
totNaoProfessor = 0

while idade != 0:
    profissional = str(input("Digite a profissão: ")).lower()
    idade = int(input("Digite a idade do profissional: [PARA PARAR DIGITE: O]"))
    if idade != 0 and profissional == "professor":
        totIdade += idade
        totProfissional += 1
    media = totIdade / totProfissional
if profissional != "professor":
    totNaoProfessor += 1
print("A média total entre a idade dos professores é de: ", media, "e o total que não são professores é de: ", totNaoProfessor)
