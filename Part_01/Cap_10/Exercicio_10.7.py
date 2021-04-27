# Adição com while sem deixar o programa parar quando fornecemos valores strings
print(" Programa que calcula a soma de dois números")
print(" Digite 0 para encerrar o programa.")
active = True
while active:	
	try:
		primeiro_numero = int(input("\n Digite o primeiro número: "))
		segundo_numero = int(input(" Digite o segundo número: "))
			
	except ValueError:
		msg = "\n Digite um valor inteiro."
		print(msg)
	else:		
		soma = primeiro_numero + segundo_numero
		print("\n " + str(primeiro_numero) + " + " + str(segundo_numero) + " = " + str(soma))
		
		try:
			Quit = int(input("\n Deseja continuar? <Sim(1)> // <Não(0)> + Enter: "))
		except ValueError:
			msg = "\n Digite um valor inteiro."
			print(msg)
		else:
			while Quit != 1 and Quit != 0:
				Quit = int(input("\n Deseja continuar? <Sim(1)> // <Não(0)> + Enter (escreva somente 1 ou 0): "))
		
			if Quit == 1:
				active = True
			elif Quit == 0:
				active = False
