maiorAltura = 0
mulherAlta = 0
mediaAltura = 0
totalAltura = 0
altura = 0

for i in range (4):
    altura = float(input("Digite a altura: "))
    sexo = str(input("Digite o sexo F ou M: ")).upper()
    idade = int(input("Digite a idade: "))

    if altura > maiorAltura:
       maiorAltura = altura
    if sexo == "F" and altura >= 1.70:  
        mulherAlta += 1
    if sexo == "F" and idade > 30:
        mediaAltura += 1
        totalAltura += altura 
        
    mediaAltura = totalAltura / mediaAltura
    

print("A maior altura é de: ", maiorAltura)
print("O total de mulheres que tem altura maior ou igual a 1.70 é de: ", mulherAlta)
print("A média de altura de mulheres com 30 anos é de: ", mediaAltura)