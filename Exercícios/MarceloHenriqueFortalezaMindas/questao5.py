salarioMensal = float(input("Digite o seu sálario mensal: "))
reajuste =  float(input("Digite a porcetagem de reajuste do seu salário: "))

valorReajuste = reajuste / 100
reajuste_Salarial =  (valorReajuste * salarioMensal) + salarioMensal

print("O reajuste salarial foi para : R$", reajuste_Salarial)