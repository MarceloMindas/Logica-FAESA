cont = 0
voto = 0
votoNulo = 0
votoBranco = 0
candidato1 = 0
candidato2 = 0 
candidato3 = 0

while voto != -1:
    voto = int(input("Digite o número do seu voto: "))
    if voto == 1:
        candidato1 +=1
        cont += 1
    elif voto == 2:
        candidato2 += 1
        cont += 1
    elif voto == 3: 
        candidato3 += 1
        cont += 1
    elif voto == 4:
        votoNulo += 1
        cont += 1
    elif voto == 0:
        votoBranco += 1
        cont += 1
    elif voto == -1:
         print("Fim da eleição!")
    else: 
         print("ERR0R!")
##a)
        
if candidato1 > candidato2 and candidato1> candidato3:
    print("Candidato1 GANHOU!")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("Candidato2 GANHOU!")
elif candidato3 > candidato2 and candidato3 > candidato1:
    print("Candidato3 GANHOU!")
else:
    ("EMPATE!") 

##b), c) e d)

print ("A eleição teve um total de: ", votoBranco, "votos em branco!")
print ("A eleição teve um total de: ", votoNulo, "votos em nulo!")
print ("A eleição teve um total de: ", cont, "votos!")