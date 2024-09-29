media =  float(input("Digite a media do aluno: "))
falta = float(input("Digite a quantidade de faltas: "))

if media >= 7 and falta < 32:
    print("Aprovado!")
elif media < 7 and falta >= 32:
    print("Reprovado por média e por falta!")
else: 
    print("Reprovado por média ou por falta!")