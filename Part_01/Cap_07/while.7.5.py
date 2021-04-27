idade = int(input(" Defina a idade da pessoa: "))
while idade != 0:
	if idade < 3:
		print("\n\t O ingresso é gratuito!")
	elif idade <= 12:
		print("\n\t O ingresso custará 10 dólares!")
	elif idade > 12:
		print("\n\t O ingresso custará 15 dólares!")
	idade = int(input(" \n Defina a idade da pessoa: "))
