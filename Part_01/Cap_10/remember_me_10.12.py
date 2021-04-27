# Lembrando o número favorito
# Juntando os dois programas do exercício 10.11 em um só, usando o try-except
import json

filename = 'Numero_favorito.json'
try:
	with open(filename, 'r') as f_objct:
		number = json.load(f_objct)

except FileNotFoundError:
	number = int(input("\n Escreva o seu número favorito: "))
	
	with open(filename, 'w') as f_objct:
		json.dump(number, f_objct)
else:
	print("\n Eu sei qual é seu número favorito! É " + str(number))
