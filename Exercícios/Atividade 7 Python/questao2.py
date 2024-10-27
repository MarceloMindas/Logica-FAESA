numero =  int(input("Digite um número para o loop: "))

soma = 0
cont = 1

while cont <= numero: 
    soma += cont
    cont += 1
print ("A soma dos valores em um contador de 1 até o", numero, "é de:", soma)
