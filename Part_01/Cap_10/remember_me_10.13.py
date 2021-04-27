import json

def pergunta_se_e_a_pessoa(username):
	"""Pergunta se é o usuário que declarou seu username antes"""
	print("\nSeu nome de usuario é " + username.title() + "?")
	escolha = input("Digite Sim[s] ou Não[n]: ").lower()
	while escolha != 's' and escolha != 'n':
		escolha = input("Digite Sim[s] ou Não[n] (Digite somente <s> ou <n>): ").lower()
		
	if escolha == 's':
		return username
	elif escolha == 'n':
		return None
		

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
	username = input("\nQual o seu nome? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

			
def greet_user():
	"""Saúda o usuário pelo nome."""
	username = get_stored_username()
	username = pergunta_se_e_a_pessoa(username)
	
	if username:
		print("\nBem vindo novamente, " + username.title() + "!")
	else:
		username = get_new_username()
		print("\nNos lembraremos o seu nome quando você voltar, " + username.title() + "!")
		
	
greet_user()
