# Restaurante

class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " é o nome do restaurante")
		print("O tipo de cozinha: " + self.cuisine_type.title())
	
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open!")
	
# Criando uma instância e armazenando na variavel restaurant		
restaurant = Restaurant('Hamburguer King', 'cozinha tradicional')

# Chamando atributos
print(restaurant.restaurant_name + " é o nome do restaurante")
print("O tipo de cozinha: " + restaurant.cuisine_type)

print("\n\n")
# Chamando métodos
restaurant.describe_restaurant()
print("\n\n")
restaurant.open_restaurant()
		
