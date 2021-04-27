import json

def get_stored_username():
	"""Obtém o nome do usuário já armazenado se estiver disponível."""
	filename = 'username.json'
	try:
		with open(filename, 'r') as f_obj:
			username = json.load(f_obj)
			
	except FileNotFoundError:
		return None
	else:
		return username
		

def get_new_username():
	"""Pede um novo nome de usuário"""
	username = input("Qual o seu nome? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

			
def greet_user():
	"""Saúda o usuário pelo nome."""
	username = get_stored_username()
	if username:
		print("Bem vindo novamente, " + username + "!")
	else:
		username = get_new_username()
		print("Nos lembraremos o seu nome quando você voltar, " + username + "!")
		
	
greet_user()
	


