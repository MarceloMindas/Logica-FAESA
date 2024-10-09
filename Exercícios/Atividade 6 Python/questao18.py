salario = float(input("Digite o salario do funcionario: ")) 
financiamento = float(input("Digite o valor do financiamento pretendido: "))

if financiamento <= salario * 5:
    print("Financiamaento concedido!")
else:
    print("Financiamento Negado!")

print("Obrigado por nos consultar! :D")