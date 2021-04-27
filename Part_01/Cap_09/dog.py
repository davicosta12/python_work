# Classes

class Dog():
	"""Uma tentativa simples de modelar um cachoroo"""
	
	def __init__(self, name, age):  # init é um método da classe
		"""Inicializa os atributos name e age"""
		self.name = name
		self.age = age
	
	def sit(self):   # sit() é um método criado pelo programador
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):  # roll_over() é um método criado pelo programador
		print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)  # my_dog refere-se a uma única instância criada a partir de uma classe


# chamando atributos da classe
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# chamando métodos da classe
my_dog.sit()
my_dog.roll_over()

