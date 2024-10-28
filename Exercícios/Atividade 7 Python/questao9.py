cont = 0
value = -1
soma = 0

positivos = 0
negativos = 0

while value != 0:
    value = int(input("Digite um valor: "))
    if value != 0:
        soma += value
        cont += 1
    #media
        if value > 0:
            positivos += 1
        elif value < 0:
            negativos += 1	
    #pos e negativo
        media = soma / cont
        porcentagem = (negativos/cont)*100

print("A soma total dos números é de: ", soma, "o total de somas é de: ", cont, "ficando com a média artmética de: ", media)
print("A porcetagem de números negativos é de: %", porcentagem)
print("A quantidade de números positivos é de:", positivos)
