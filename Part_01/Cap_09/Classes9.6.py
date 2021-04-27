class Restaurant():   # Classe pai
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
		
class IceCreamStand(Restaurant):  # Classe filha
	def __init__(self, restaurant_name,  cuisine_type):  
		super().__init__(restaurant_name,  cuisine_type)  # Herdando tudo da classe pai
		
		self.flavors = ['flocos', 'creme', 'napolitano', 'chocolate', 
						'morango', 'açaí']
						
	def printa_sorvete(self):
		print("\n Nossa restaurante tem somente esses sabores de sorvete: ")
		for sabor in self.flavors:
			print("\n Sorvete de " + sabor)
	
# Mexendo na classe pai com a classe filha
instancia = IceCreamStand('mc donalds', 'cozinha larga')
instancia.describe_restaurant()

instancia.set_number_served(22)
instancia.exibe_numero_cliente()

instancia.increment_number_served(36)
instancia.exibe_numero_cliente()

# Printando método criado na classe filha
instancia.printa_sorvete()
		
	
