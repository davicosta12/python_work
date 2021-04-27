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
