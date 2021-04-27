filename = 'pi_digits.txt'

with open(filename) as file_object: # with abri e fecha o arquivo de maneira apropriada
	for line in file_object:        # não precisa usar o close() no final
		print(line.rstrip())
