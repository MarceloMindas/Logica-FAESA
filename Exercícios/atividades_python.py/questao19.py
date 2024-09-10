nomeVendedor = str(input("Digite o nome do vendedor: "))    
salario =  float(input("Digitite o salário total do vendedor: "))
valorTotal = float(input("Digite o total de vendas efetuadas por ele no mês: R$"))
comisao = 15/100

comisao =  valorTotal * 15/100 
totalSalario =  salario + comisao

print("O", nomeVendedor, "vendeu no total: R$", valorTotal, "então com seu salario sendo: R$ ", salario,
    "como recompensa com o bonus de 15% ele irá ganhar: R$ ", comisao,
    "de comisão com o valor total do seu salario sendo: ", totalSalario)