ladoA = int(input("Digite o valor do lado A don triangulo: "))
ladoB = int(input("Digite o valor do lado B do triangulo: "))
ladoC = int(input("Digite o valor do lado C do tringulo: "))

if (ladoA + ladoB < ladoC) or (ladoA + ladoC < ladoB) or (ladoB + ladoC < ladoA):
     print('Nao é um triangulo')
elif (ladoA == 0) or (ladoB == 0) or (ladoC == 0):
    print("Nenhum dos lados pode ser igual a zero")
elif (ladoA == ladoB) and (ladoA == ladoC) :
    print('Equilatero')
elif (ladoA==ladoB) or (ladoA==ladoC) or (ladoB==ladoC):
    print('Isósceles')
else:
    print('Escaleno')