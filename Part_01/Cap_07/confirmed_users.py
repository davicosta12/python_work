unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:        # ficou vazio, retorna false
	current_user = unconfirmed_users.pop()
	print("Verificando usuário: " + current_user.title())
	confirmed_users.append(current_user)
	

print("\nAqui estão os usuários que foram confirmados")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
