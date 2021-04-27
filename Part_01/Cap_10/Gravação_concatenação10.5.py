active = True
sair = 'n'
nao_sair = 's'
informacoes = []
while active:
	opiniao = input("\n Por qual motivo você gosta de programação? (Somente strings) ")
	informacoes.append(opiniao)
	
	print("\n Seja bem vindo(a). Obrigado por compartilhar sua ideia.")
	
	continuar = input("\n Deseja continuar com a pesquisa? Sim(S) / Não(N) ").lower()
	while continuar != nao_sair and continuar != sair:
		continuar = input("\n Deseja continuar com a pesquisa? Sim(S) / Não(N) ---> Digite somente (S) ou (N) ").lower()		
			
	if continuar == sair:
		active = False
	elif continuar == nao_sair:
		active = True

with open("guest_book.txt", "a") as file_object: # concatenação
	for informacao in informacoes:
		file_object.write(informacao + "\n")
