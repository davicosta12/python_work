import json

# carrega o dado numbers novamente usando a função load()
filename = 'numbers.json'
with open(filename, 'r') as f_obj:
	numbers = json.load(f_obj)

print(numbers)
	
