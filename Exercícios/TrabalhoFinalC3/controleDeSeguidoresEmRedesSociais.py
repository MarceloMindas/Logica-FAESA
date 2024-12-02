import numpy as np

valor_entradado = {}
valor_saído = {}

while True:
    entrada = float(input("\nDigite o valor que entrou:\n"))
    saída = float(input("\nDigite o valor que saiu:\n"))
    dia = input("\nDigite o dia que entrou ou saiu (SEJA ESPECÍFICO):\n")
    
    valor_entradado[dia] = entrada
    if saída > 0.0:
        valor_saído[dia] = saída
    
    continuar = input("\nDeseja inserir mais dados? (S/N):\n")
    if continuar.lower() == "n":
        break



print("\nDados armazenados:")
print("Valores de entrada:", valor_entradado)
print("Valores de saída:",valor_saído)