filename = 'pi_20000.txt'

with open(filename) as file_object: # with abri e fecha o arquivo de maneira apropriada, o proprio python faz esse trabalho por baixo dos panos
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string = pi_string + line.strip()
	
birthday = input("Enter you birhday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your bithday appears in the firts 20000 digits of pi!")
else:
	print("Your bithday does not appears in the firts 20000 digits of pi!")
