mod = 0
altura = -1

while altura != 0:
    altura = float(input("Digite a altura das modelos: "))
    
    if altura > mod:
        mod = altura

print("A altura da modelo mais alta é de:", mod)