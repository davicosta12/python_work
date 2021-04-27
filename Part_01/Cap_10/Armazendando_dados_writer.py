import json

numbers = [2, 3, 5, 7, 11, 13]

# json.dump() aceita dois argumentos: um dado para armazenar e um objeto arquivo que pode ser usado para armazenar o dado.
# Armazena o dado numbers dentro da numbers.json

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)
	
