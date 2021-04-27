users_information = {}

print("\n--- REALIZAÇÃO DE ENQUETES ---\n")
active = True
while active:
	name = input(" \n Qual o seu nome? ")
	prompt = input(" Se pudesse visitar um lugar do mundo, para onde você iria? ")
	users_information[name] = prompt
	
	repeat = input(" Deja realizar uma nova enquete? (s / n)")
	if repeat == 'n':
		active = False
		
print("\nA enquete foi concluida, mostre-me os resultados\n")
for name, lugar in users_information.items():
	print(name.title() + " gostaria de visitar " + lugar.title())
	
