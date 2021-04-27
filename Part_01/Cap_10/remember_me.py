import json
filename = 'username.json'

try:
	with open(filename, 'r') as f_obj:
		username = json.load(f_obj)

except FileNotFoundError:
	username = input("Qual o seu nome? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("Nos lembraremos o seu nome quando você voltar, " + username + "!")
else:
	print("Bem vindo novamente, " + username + "!")
