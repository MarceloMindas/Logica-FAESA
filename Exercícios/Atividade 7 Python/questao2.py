#2) Implemente um programa que solicita ao usuário um número e calcula a soma dos números de 1 até o número inserido pelo usuário, utilizando while para realizar a soma.

numero =  int(input("Digite um número para o loop: "))

soma = 0
cont = 1

while cont <= numero: 
    soma += cont
    cont += 1
print ("A soma dos valores em um contador de 1 até o", numero, "é de:", soma)
