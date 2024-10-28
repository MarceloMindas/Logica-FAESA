cont = -1
soma = 0

while len (letra) != 0: 
        letra = (input("Digite a letra desejada: "))
        if cont != 0:
            if letra == ("a"):
                soma += 1
                continue
            elif letra != ("a"):
                print("Letra A não foi digitada!")
                continue
            print("A letra a, foi digitada: ", soma, "vez")
            
##nao terrminado e mal feito