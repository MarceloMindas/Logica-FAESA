altura = 0
maiorAltura = 0
menorAltura = 0
mediaAltura = 0
totalAlturas = 0
alturaSix = 0
alturaTri = 0
cont = 0

for i in range (3):
    altura = float(input("Digite a altura: "))

    if altura > maiorAltura:
        maiorAltura = altura
    if altura < maiorAltura:
        menorAltura = altura
    if altura > 1.60:
        alturaSix += 1
    if altura < 1.30: 
        alturaTri += 1
    totalAlturas += altura
    cont += 1
    mediaAltura = totalAlturas/ cont

print(maiorAltura)
print(menorAltura)
print(mediaAltura)
print(alturaSix)
print(alturaTri)