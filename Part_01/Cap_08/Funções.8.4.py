def make_shirt(tamanho_camiseta = 'G', mensagem_estampada = 'Eu amo Python'):
	print("\n O tamanho da camiseta é " + tamanho_camiseta)
	print(" Aqui está a mensagem estampada: " + mensagem_estampada.title())

make_shirt('G')
make_shirt('M')
make_shirt('P', 'Eu amo sorvete')
print("\n --------------------------------------------------------- \n")
make_shirt() # Se não passarmos nenhum argumento, os valores usados são os defaults.
