text = "Forneça uma série de engredientes para usarmos na pizza"
text = text + "\nQuando terminar, digite <quit>: "
print(text)
text02 = "Digite o ingrediente a ser usado: "
flag = True
while flag:
	ingredientes = input(text02)
	if ingredientes == 'quit':
		flag = False
	else:
		print(ingredientes + " foi acrescentado na pizza!")
	
	
