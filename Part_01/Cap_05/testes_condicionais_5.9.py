	# Sem usuários --> Verificando se a lista de usuários está vazia ou não
	# Pelo fato de não conter nenhum item na lista, o if se torna false, executando a condição seguinte(else)
	
nomes_usuarios = []

if nomes_usuarios:
	for nome_usuario in nomes_usuarios:
		if nome_usuario.lower() == 'davi':
			print('Olá admin, gostaria de ver um relatório de status?') 
		else:
			print('Olá ' + nome_usuario + ', obrigado por fazer login novamente')
else:
	print('Precisamos encontrar alguns usuários')
