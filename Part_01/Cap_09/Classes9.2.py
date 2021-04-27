class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " é o nome do restaurante")
		print("O tipo de cozinha: " + self.cuisine_type.title())
	
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open!")
	
restaurant01 = Restaurant('hamburguer king', 'cozinha tradicional')
restaurant02 = Restaurant('mc donalds', 'cozinha grande')
restaurant03 = Restaurant('johns burguer', 'cozinha tradicional')

restaurant01.describe_restaurant()
print("\n")
restaurant02.describe_restaurant()
print("\n")
restaurant03.describe_restaurant()
