soma = 0
numero = 0
cont = 0

while numero != -1:
    numero = int(input("Digite um número inteiro: "))
    if numero != -1:
        soma += numero
        cont += 1
if cont == 0:
    print("Nenhum número foi introduzido!")
else: 
    media = soma / cont
print(media)

