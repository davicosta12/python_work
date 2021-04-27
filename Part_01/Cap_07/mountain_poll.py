responsaveis = {}
active_while = True

while active_while:
	name = input("\n Qual o seu nome? ")
	favorite_thing = input(" Qual montanha você gostaria de subir algum dia? ")
	
	responsaveis[name] = favorite_thing
	repeat = input(" Você gostaria de fazer uma outra enquete? (s / n) ")
	
	if repeat == 'n':
		active_while = False
	
print("\n--- Resultados das enquetes ---")
for name, response in responsaveis.items():
	print(name.title() + " gostaria de subir na montanha chamada " + response.title())
