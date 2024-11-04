ant = 0
ult = 1
penul = 0

numero = int(input("Digite um número: "))

for i in range (numero):
    print(ant)
    ant  = penul
    penul = ult
    ult += ant
    