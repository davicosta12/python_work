num = int(input("Digite um numero inteiro qualquer: "))
if num % 10 == 0:
	if num == 0:
		print("\n" + str(num) + " não é múltiplo de 10")
	else:
		print("\n" + str(num) + " é múltiplo de 10")
else:
	print("\n" + str(num) + " não é múltiplo de 10")

