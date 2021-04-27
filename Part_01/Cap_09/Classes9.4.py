# Restaurante

class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0              # Valor default, não aparece método init
	
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " é o nome do restaurante")
		print("O tipo de cozinha: " + self.cuisine_type.title())
	
	def open_restaurant(self):   
		print(self.restaurant_name.title() + " is open!")
	
	def set_number_served(self, number_served):   # Alterando atributo através de um método
		self.number_served = number_served
		
	def increment_number_served(self, increment):
		self.number_served = self.number_served + increment
	
	def exibe_numero_cliente(self):
		print(" O número de clinetes servidos é: " + str(self.number_served))
		
			
restaurant = Restaurant('Hamburguer King', 'cozinha tradicional')

# Alterando valor de um atributo de maneira direta 

#print(restaurant.number_served)
#restaurant.number_served = 2
#print(restaurant.number_served)

# Alterando atributo através de um método

restaurant.set_number_served(25)
restaurant.exibe_numero_cliente()

# Chamando método que incrementa

restaurant.increment_number_served(10)


# Chamando método que printa

restaurant.exibe_numero_cliente()
