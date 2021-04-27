from user02 import User

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

