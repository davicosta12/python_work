# Número favorito
# Load
import json

filename = 'Numero_favorito.json'
with open(filename, 'r') as f_objct:
	number = json.load(f_objct)

print("\n Eu sei qual é seu número favorito! É " + str(number))
