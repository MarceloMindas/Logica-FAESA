salario = float(input("Digite o salario do funcionario: ")) 

if salario < 500:
    reajuste = (15/100) * salario
elif salario >= 500 and  salario <= 1000:
    reajuste = (10/100) * salario
elif salario > 1000:
    reajuste = (5/100) * salario

salario = salario + reajuste

print("O novo saláirio é: ", salario)