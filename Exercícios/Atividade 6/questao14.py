
nome = str(input("Digite o nome do pasciente: "))
peso = float(input("Digite o peso do pasciente: "))
altura = float(input("Digite a altura do pasciente: "))

indiceMassaCorporal =  peso / (altura*altura)

print(indiceMassaCorporal)

if indiceMassaCorporal < 20:
    print("Abaixo do peso!")
elif indiceMassaCorporal >= 20 and indiceMassaCorporal <= 25:
    print("Normal!")
elif indiceMassaCorporal <= 25 and indiceMassaCorporal <= 35:
    print("Excesso de peso!")
elif indiceMassaCorporal <= 35 and indiceMassaCorporal <= 50:
    print("Obesidade!")
elif indiceMassaCorporal >= 50:
    print("Obesidade mórbida!")
                   