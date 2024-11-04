limiteTotalPescaKg = float(input("Digite o limite diário de Kg de pesca/dia: "))
mediaPeixe = 0
soma = 0
pesoPeixe = -1

while pesoPeixe != 0 and soma <= limiteTotalPescaKg:
    pesoPeixe = float(input("Digite o peso da quantidade de peixes coletados no dia (OBS: |0| PARA PARAR O CÓDIGO): "))
    soma += pesoPeixe
    if soma > limiteTotalPescaKg:
        print("O limite de Kg's/p peixe foi exedida!")
if pesoPeixe == 0:
    print("O total de de Kg's de peixe coletada no dia foi de: ", soma)
