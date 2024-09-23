aluno = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a nota do primeiro trimestre: "))
nota2 =  float(input("Digite a nota do segundo trimestre: "))
nota3 =  float(input("Digite a nota do terceiro trimestre: "))

mediaFinal = (nota1+nota2+nota3) / 3

if mediaFinal >= 6: 
    print ("Parabéns!",  aluno, "Voce passou com a média total de: ", mediaFinal, "Assim então concluindo o ano!")
else:
     print("Infelizmente voce não conseguiu a media nescessária para passar de ano, com sua média final sendo: ", mediaFinal)