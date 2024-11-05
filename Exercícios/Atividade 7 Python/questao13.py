cont  = 0
totAlunoAprovado = 0
totAlunoReprovado = 0
mediaTotal = 0
mediaDamedia = 0

for i in range (5):
    matricula = int(input("Digite a matricula do aluno: "))
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    media = (nota1+nota1)/2
    cont += 1
    mediaTotal += media
    mediaDamedia = mediaTotal / cont
    if media <= 5:
        print("Aluno com matrícula",matricula, "está reprovado com a média de", media, "pontos")
        totAlunoReprovado += 1
    elif media > 5:
        print("Aluno com matrícula",matricula, "está aprovado com a média de", media, "pontos")
        totAlunoAprovado += 1
print(totAlunoAprovado)
print(totAlunoReprovado)
print(mediaDamedia)
