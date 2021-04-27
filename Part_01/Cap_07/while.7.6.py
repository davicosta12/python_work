# Primeira maneira - condicional

idade = int(input(" Defina a idade da pessoa: "))
while idade != 0:
	if idade < 0:
		while idade < 0:
			idade = int(input(" \n Defina a idade da pessoa(Maior do que zero): "))
		continue
		
	if idade < 3:
		print("\n\t O ingresso é gratuito!")
	elif idade <= 12:
		print("\n\t O ingresso custará 10 dólares!")
	elif idade > 12:
		print("\n\t O ingresso custará 15 dólares!")
	idade = int(input(" \n Defina a idade da pessoa: "))
	
# Segunda maneira maneira - FLAG

active = True
while active:
	idade = int(input(" Defina a idade da pessoa: "))
		
	if idade > 0 and idade < 3:
		print("\n\t O ingresso é gratuito!")
	elif idade >= 3 and idade <= 12:
		print("\n\t O ingresso custará 10 dólares!")
	elif idade > 12:
		print("\n\t O ingresso custará 15 dólares!")
	else:
		active = False
	
# Terceira maneira maneira - break

prompt = ''
while prompt != 'quit':
	prompt = input(" \n Defina a idade da pessoa: ")
	
	if prompt == 'quit':
		break
	else:
		idade = int(prompt)	
		if idade <= 0:
			while idade <= 0:
				idade = int(input(" \n Defina a idade da pessoa(Maior do que zero): "))		
			if idade < 3:
				print("\n\t O ingresso é gratuito!")
			elif idade <= 12:
				print("\n\t O ingresso custará 10 dólares!")
			elif idade > 12:
				print("\n\t O ingresso custará 15 dólares!")	
		else:
			if idade < 3:
				print("\n\t O ingresso é gratuito!")
			elif idade <= 12:
				print("\n\t O ingresso custará 10 dólares!")
			elif idade > 12:
				print("\n\t O ingresso custará 15 dólares!")
		
