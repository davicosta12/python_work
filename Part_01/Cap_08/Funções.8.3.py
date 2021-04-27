def make_shirt(tamanho_camiseta, mensagem_estampada):
	print("\n O tamanho da camiseta é " + tamanho_camiseta)
	print(" Aqui está a mensagem estampada: " + mensagem_estampada.title())
	
make_shirt('M', 'seja feliz sempre') # argumento poosicional
make_shirt(mensagem_estampada = 'seja feliz sempre', tamanho_camiseta = 'M') # argumento nomeado
