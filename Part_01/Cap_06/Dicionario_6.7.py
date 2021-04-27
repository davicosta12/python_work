pai = {
	'first_name': 'andre',
	'last_name': 'floriano',
	'age': 44,
	'city': 'são paulo',	 
	}

mae = {
	'first_name': 'adriana',
	'last_name': 'sousa',
	'age': 42,
	'city': 'são paulo',
	}

arthur = {
	'first_name': 'arthur',
	'last_name': 'silva',
	'age': 2,
	'city': 'são paulo',
	}
		
people = [pai, mae, arthur]	


for pessoa in people:
	print("\n" + pessoa['first_name'].title() + " " + pessoa['last_name'].title() + ":")
	print("\tIdade: " + str(pessoa['age']))
	print("\tcidade: " + pessoa['city'].title())
	
