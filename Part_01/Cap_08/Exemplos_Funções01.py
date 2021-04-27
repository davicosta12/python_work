# Argumentos posicionais
def describe_pet(pet_name, animal_type):
	print("\n Eu tenho um " + animal_type + ".")
	print(" O nome do meu " + animal_type + " é " + pet_name.title())


describe_pet('dudu', 'cachorro')
describe_pet('katia', 'gato')
describe_pet('fred', 'hamster')
print("\n --------------------------------------------------------- ")
# Argumentos nomeados
def describe_pet(pet_name, animal_type):
	print("\n Eu tenho um " + animal_type + ".")
	print(" O nome do meu " + animal_type + " é " + pet_name.title())
	
describe_pet(pet_name = 'dudu', animal_type = 'cachorro')
describe_pet(animal_type = 'gato', pet_name = 'katia')
describe_pet(pet_name = 'fred', animal_type = 'hamster')
print("\n --------------------------------------------------------- \n")
# Valores default
# Ao usar valores default, qualquer parâmetro com um valor desse tipo
#deverá ser listado após todos os parâmetros que não tenham valores default.
# Isso permite que Python continue a interpretar os argumentos posicionais corretamente.
def describe_pet(pet_name, animal_type = 'cachorro'): # Valor default
	print(" Eu tenho um " + animal_type + ".")
	print(" O nome do meu " + animal_type + " é " + pet_name.title())

describe_pet(pet_name = 'dudu')
describe_pet(pet_name = 'katia', animal_type = 'gato')
describe_pet(pet_name = 'fred')
describe_pet('patrick', 'camelo')
describe_pet('Francisco')
