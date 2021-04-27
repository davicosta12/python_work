	# Verificando nomes de usuários
	
current_users = ['Ricardo', 'DAVI', 'RaFaEl', 'AdRIAna', 'JOelma', 
'FRAncisco']

new_users = ['Davi', 'Rafael', 'Regina', 'Eduardo', 'Melissa', 'Larissa'
, 'Lucas', 'Joel']

current_users_adjusted = []

for current_user in current_users:
	current_users_adjusted.append(current_user.lower())

for new_user in new_users:
	if new_user.lower() in current_users_adjusted:
		print('Forneça um nome novo!')
	else:
		print('O nome de usuário está disponível!')
	


