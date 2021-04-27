# conta quantos 'the' tem dentro do livro alice

filename = 'alice.txt'
with open(filename) as f_objects:
	conteudo = f_objects.read()

conteudo = conteudo.rstrip()
palavras = conteudo.split()

lines = ''
for palavra in palavras:
	lines = lines + " " + palavra
	
print(lines.lower().count('the'))
