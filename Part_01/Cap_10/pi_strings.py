filename = 'pi_digits.txt'

with open(filename) as file_object: # with abri e fecha o arquivo de maneira apropriada, o proprio python faz esse trabalho por baixo dos panos
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string = pi_string + line.strip()

print(pi_string)
print(len(pi_string))
print(type(pi_string))

