class User():
	def __init__(self, first_name, last_name, age, sex, situacao, login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.situacao = situacao
		self.login_attempts = login_attempts
		
	def describe_user(self):
		print("\n Informações sobre o usuário: " + self.first_name.title())
		print("\n Nome: " + self.first_name.title())
		print(" Sobrenome: " + self.last_name.title())
		print(" Sexo: " + self.sex.title())
		print(" Idade: " + str(self.age))
		print(" Situação: " + self.situacao.title())
	
	def greet_user(self):
		print("\n Boa noite, " + self.first_name.title())
	
	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0
	
usuario01 = User('davi', 'silva', 21, 'masculino', 'solteiro', 2)
usuario02 = User('diogo', 'afonso', 48, 'masculino', 'casado', 5)
usuario03 = User('maria fernanda', 'damaseno', 21, 'feminino', 'viuva', 6)

# Incrementando o  atributo com um método

# começa com dois
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
usuario01.increment_login_attempts() # +1
print(usuario01.login_attempts) # resultado = 2 + 9 = 11

# Chamando o outro método para resetar o atributo
usuario01.reset_login_attempts()
print(usuario01.login_attempts)



		




