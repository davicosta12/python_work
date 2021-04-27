	# Usando funções

numeros = []
for numero in range(1, 1000001):
	numeros.append(numero)
	
print(min(numeros))
print(max(numeros))
print(sum(numeros))

	# Usando algoritmos

numeros = []
for numero in range(1, 1000001):
	numeros.append(numero)

		# Achando o mínimo e o máximo dentro da lista digits
i = 0
while i < len(numeros):
	if i == 0:
		x = miN = maX = numeros[i]
	else:
		if numeros[i] > x:
			x = numeros[i] 
			maX = x
			 
		if numeros[i] < x:
			x = numeros[i]
			miN = x
			
	i = i + 1
	
print('O valor máximo da lista é ' + str(maX))
print('O valor mínimo da lista é ' + str(miN))

		# Fazendo a soma dos elementos da lista

numeros = []
for numero in range(1, 1000001):
	numeros.append(numero)
	            
i = 0
soma = 0
while i < len(numeros):
	soma = soma + numeros[i]
	i = i + 1
print('A soma dos elementos da lista é ' + str(soma))
