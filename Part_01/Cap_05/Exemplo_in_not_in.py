# Usando o IN ou o NOT IN
alimentos = ['pizza', 'esfirra', 'miojo', 'macarrão', 'estrogonofe']

N = input('Escreva um alimento: ')

if N in alimentos:
	print('Está na lista') 
else:
	print('Não está na lista')

# Usando Algoritmo

N = input('Escreva um alimento: ')

i = 0
flag = 0
while i < len(alimentos):
	if N == alimentos[i]:
		flag = 1
	i = i + 1

if flag == 0:
	print('Não está na lista')		
else:
	print('Está na lista') 
