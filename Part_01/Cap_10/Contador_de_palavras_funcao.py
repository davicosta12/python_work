def contador_de_palavras(nome_arq):
	"""Conta o número aproximado de palavras em um arquivo qualquer"""
	try:   # Se esse bloco funcionar com sucesso, a condição else será executada, caso contrário a condição except será executada.
		with open(nome_arq) as f_obj:
			conteudo = f_obj.read()
	except FileNotFoundError:
		msg = "Desculpe, o arquivo " + nome_arq + " não exite."
		print(msg)
	else:
		palavras = conteudo.split()
		numero_palavras = len(palavras)
		print("O arquivo " + nome_arq + " tem cerca de " + str(numero_palavras) + " palavras.")
	
