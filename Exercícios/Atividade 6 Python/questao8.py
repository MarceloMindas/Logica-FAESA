nota1 = int(input("Digite a nota do primeiro atleta: "))
nota2 = int(input("Digite a nota do segundo atleta: "))
nota3 = int(input("Digite a nota do terceiro atleta: "))

if nota1 > nota2 and nota2 > nota3:
    print("Primero, Segundo e Terceiro!")
elif nota1 > nota3 and nota3 > nota2:
    print("Primeiro, Terceiro e Segundo!")
elif nota2 > nota1 and nota1 > nota3:
    print("Segundo, Primeiro e Teceiro!")
elif nota2 > nota3 and nota3 > nota1:
    print("Segundo, Terceiro e Primeiro!")
elif nota3 > nota1 and nota1 > nota2:
    print("Terceiro, Primeiro e Segundo!")
elif nota3 > nota2 and nota2 > nota1:
    print("Terceiro, Segundo e Teceiro!")
 
