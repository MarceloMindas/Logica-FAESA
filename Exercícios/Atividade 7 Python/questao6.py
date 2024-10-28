fatorial = 1
cont = 1
numero = int(input("Digite o valor de um número: "))

while cont <= numero: 
    fatorial *= cont
    cont += 1
print(fatorial)