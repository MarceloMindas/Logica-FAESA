#1) Faça um programa que escreve na tela a mesma frase 10 vezes. E depois faça com que oprograma mostre o número de cada linha no início e no final da linha, conforme exemplo:1 Sou um programa Python! 12 Sou um programa Python! 23 Sou um programa Python! 3

for cont in range(1,11):
    print(cont, "Sou um programa em  Python!", cont)
    cont  += 1

#Também teria como usar a estrutura de repetição (while cont < 4:), porém com a anotação: Se existe um número fixo de vezes que o(s) comando(s) tem que repetir, usa-se o For. Se não sabe quantas vezes tem que repetir, usa-se o While.


