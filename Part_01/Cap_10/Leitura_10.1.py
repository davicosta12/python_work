# primeiro modo usando read() ---> lê todos as linhas de uma vez
arq_learning = 'learning_python.txt'
with open(arq_learning) as file_reader:
	leitura_completa = file_reader.read()
	print(leitura_completa.rstrip())

print("\n")	

# segundo modo usando o for ---> percorre as linhas do arquivos texto
arq_learning = 'learning_python.txt'
with open(arq_learning) as file_reader:
	for line in file_reader:
		print(line.rstrip())
	
print("\n")		
# terceiro modo usando o readlines() ---> armazena em uma lista todas as linhas
arq_learning = 'learning_python.txt'
with open(arq_learning) as file_reader:
	lines = file_reader.readlines()
	print(lines)
	
print("\n")	

for line in lines:
	print(line.rstrip())
	
print("\n")		
# quarto modo usando o readline() ---> lê linha por linha do arquivo
		
arq_learning = 'learning_python.txt'

with open(arq_learning) as file_reader:
	line = file_reader.readline()
	while line != '':
		line = line.rstrip()
		print(line)
		line = file_reader.readline()
	

	
	
