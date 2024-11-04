curtiu = 0
descurtiu = 0
escolha = 0
totEscolhas = 0

for i in range (15):
    escolha = int(input("Você gostou do filme? [1.S|2.N]: "))
    if escolha == 1:
        curtiu += 1
    elif escolha == 2:
         descurtiu += 1
    totEscolhas = curtiu + descurtiu

print("O total de pessoas que curtiram o filme foi de: ", curtiu)
print("O total de pessoas que  não curtiram o filme foi de: ", descurtiu)
