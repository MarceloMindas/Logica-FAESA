valorHoraAula = int(input("Digite o quanto vale a hora da aula: "))
quantAulas = int(input("Digite a quantidade de aulas que o professor deu no mês: "))
descontInss = float(input("Digite o percentual de desconto do INSS: "))
salarioMininmo = 1412

salarioBruto = (valorHoraAula * quantAulas)
salarioLiquido = salarioBruto - (salarioBruto * descontInss)

print (salarioLiquido)

if salarioLiquido >= 10*salarioMininmo:
    print("Parabéns pelo seu esforço!")
elif salarioLiquido >= 6*salarioMininmo and salarioLiquido <= 9*salarioMininmo:
    print("Um dia você chega lá!")
else:
    print("Ah! Precisa se esforçar!")