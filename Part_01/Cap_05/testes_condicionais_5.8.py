	# Olá admin
	
nomes_usuarios = ['Ricardo', 'Davi', 'Rafael', 'Adriana', 'Joelma', 
'Francisco', 'Regina', 'Eduardo', 'Melissa', 'Larissa', 'Lucas', 'Joel']

for nome_usuario in nomes_usuarios:
	if nome_usuario.lower() == 'davi':
		print('Olá admin, gostaria de ver um relatório de status?') 
	else:
		print('Olá ' + nome_usuario + ', obrigado por fazer login novamente')
		
