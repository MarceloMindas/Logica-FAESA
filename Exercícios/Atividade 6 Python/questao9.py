nome = str(input("Digite o nome do  aluno: "))
prova = float(input("Digite a nota da prova: "))
trabalho = float(input("Digite a nota do trabalho: "))

media =  (prova + trabalho) / 2

if media > 7:
    print("Parábens", nome," você foi aprovado!")
else:
    print("Infelizmente", nome," você foi reprovado!")
