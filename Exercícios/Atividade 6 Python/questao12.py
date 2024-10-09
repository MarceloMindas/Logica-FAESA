idade = int(input("Digite a idade do nadador(a): "))

if idade >= 5 and idade <= 7:
    print("Nadador(a), é da classificação: Infantil A")
elif idade >= 8 and idade <= 11:
    print("Nadador(a), é da classificação: Infantil B")
elif idade >= 12 and idade <= 13:
    print("Nadador(a), é da classificação: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Nadador(a), é da classificação: Juvenil B")
elif idade >= 18:
    print("Nadador(a), é da classificação: Adulto")
else: 
    print("Menorers que 5 anos, não podem ser classificados!")