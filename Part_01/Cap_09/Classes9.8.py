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
		
class Admin(User):
	def __init__(self, first_name, last_name, age, sex, situacao, login_attempts):	
		super().__init__(first_name, last_name, age, sex, situacao, login_attempts)		
		
		self.admin_privileges = Privileges()  # Cria uma instância da classe Privileges como um atributo da classe Admin
	
class Privileges():
	def __init__(self):
		
		self.privileges = ['can add post', 'can delete post', 'can ban user',
							'can commit private messages', 'can active anything'] 
	
	def show_privileges(self):
		print(" Privilégios do Admin")
		i = 0
		for privilegio in self.privileges:
			if i == len(self.privileges) - 1:
				print("\n " + privilegio + ".")
			else:
				print("\n " + privilegio + ";")
			i = i + 1
	
instancia = Admin('davi', 'silva', 21, 'masculino', 'solteiro', 6)
instancia.admin_privileges.show_privileges()
