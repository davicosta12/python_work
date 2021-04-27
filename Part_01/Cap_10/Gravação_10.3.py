active = True
sair = 'n'
nao_sair = 's'
nomes = []
while active:
	nome = input("\n Qual o seu nome? (Somente strings) ").title()
	nomes.append(nome)
	continuar = input("\n Deseja continuar? Sim(S) / Não(N) ").lower()
	while continuar != nao_sair and continuar != sair:
		continuar = input("\n Deseja continuar? Sim(S) / Não(N) ---> Digite somente (S) ou (N) ").lower()		
			
	if continuar == sair:
		active = False
	elif continuar == nao_sair:
		active = True

with open("guest.txt", "w") as file_object:
	for nome in nomes:
		file_object.write(nome + "\n")


	

