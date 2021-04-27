# quarto modo usando o readline() ---> lê linha por linha do arquivo
		
arq_learning = 'learning_python.txt'

with open(arq_learning) as file_reader:
	line = file_reader.readline()
	while line != '':
		line = line.rstrip()
		line = line.replace('Python', 'C') # modifica uma palavra por outra
		print(line)
		line = file_reader.readline()
