# Número favorito
# Writer
import json

number = int(input("\n Escreva o seu número favorito: "))

filename = 'Numero_favorito.json'
with open(filename, 'w') as f_objct:
	json.dump(number, f_objct)
	
