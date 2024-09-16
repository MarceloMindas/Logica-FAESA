quantidadeBolo2 = int(input("Selecione a quantidade de bolos de 2Kg (R$90): "))
quantidadeBolo4 = int(input("Selecione a quantidade de bolos de 4Kg (R$120): "))
quantidadeBolo6 = int(input("Selecione a quantidade de bolos de 6Kg (R$150): "))

precoBolo2 = (quantidadeBolo2 * 90) 
precoBolo4 = (quantidadeBolo4 * 120)
precoBolo6 =  (quantidadeBolo6 * 150)

print("A quantidade de bolos de 2Kg foi: ", quantidadeBolo2, "assim então no total em R$ sendo: R$", precoBolo2)
print("A quantidade de bolos de 4Kg foi: ", quantidadeBolo4, "assim então no total em R$ sendo: R$", precoBolo4)
print("A quantidade de bolos de 6Kg foi: ", quantidadeBolo6, "assim então no total em R$ sendo: R$", precoBolo6)

precoTotal = precoBolo2 + precoBolo4 + precoBolo6

print("Ficando assim então o valor total sendo: R$", precoTotal)




