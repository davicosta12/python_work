print("Digite dois números, e eu irei dividir eles.")
print("Enter 'q' para sair.")

while True:
	primeiro_numero = input("\nPrimeiro número: ")
	if primeiro_numero == 'q':
		break
	segundo_numero = input("Segundo número: ")
	if segundo_numero == 'q':
		break
		
	try:
		resposta = int(primeiro_numero) / int(segundo_numero)
		
	except ZeroDivisionError:
		print("Você não pode dividir por 0!")
		
	else:
		print(resposta)
	
