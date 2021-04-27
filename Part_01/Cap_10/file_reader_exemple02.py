filename = 'pi_digits.txt'

with open(filename) as file_object: # with abri e fecha o arquivo de maneira apropriada, o proprio python faz esse trabalho por baixo dos panos
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
