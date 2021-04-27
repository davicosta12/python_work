from name_function import retorna_nome_formatado

print("Enter 'q' se em algum momento você quiser sair.")
while True:
	first = input("\nPorfavor, digite o seu nome: ")
	if first == 'q':
		break
	last = input("Porfavor, digite o sobrenome: ")
	if last == 'q':
		break
	
	nome_formatado = retorna_nome_formatado(first, last)
	print("\tAqui está o nome formatado: " + nome_formatado + ".")
