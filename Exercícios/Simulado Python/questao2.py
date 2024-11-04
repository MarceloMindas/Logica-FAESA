numero = -1
totNumero = 0
naoDigitado = 0 

while numero != 0:
    numero = int(input("Digite a quantidade de números que deseja: [Se desejar parar digite: 0]: "))
    if numero == 5:
        totNumero += 1
    if numero != 0 and numero != 5:
        naoDigitado += 1
print("O total de vezes que o número 5 foi digitado foi de: ", totNumero, "vezes! e o tanto de vezes que o número 5 não foi digitado é de: ", naoDigitado)




