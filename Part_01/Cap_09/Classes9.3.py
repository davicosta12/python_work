class User():
	def __init__(self, first_name, last_name, age, sex, situacao):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.situacao = situacao
		
	def describe_user(self):
		print("\n Informações sobre o usuário: " + self.first_name.title())
		print("\n Nome: " + self.first_name.title())
		print(" Sobrenome: " + self.last_name.title())
		print(" Sexo: " + self.sex.title())
		print(" Idade: " + str(self.age))
		print(" Situação: " + self.situacao.title())
	
	def greet_user(self):
		print("\n Boa noite, " + self.first_name.title())
	
usuario01 = User('davi', 'silva', 21, 'masculino', 'solteiro')
usuario02 = User('diogo', 'afonso', 48, 'masculino', 'casado')
usuario03 = User('maria fernanda', 'damaseno', 21, 'feminino', 'viuva')

usuario01.describe_user()
usuario01.greet_user()

usuario02.describe_user()
usuario02.greet_user()

usuario03.describe_user()
usuario03.greet_user()
		
		
