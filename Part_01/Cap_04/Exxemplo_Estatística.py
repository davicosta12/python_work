              # Usando funções

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# MIN
print(min(digits))
# MAX
print(max(digits))
# SUM
print(sum(digits))

              # Usando algoritmos

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Achando o mínimo e o máximo dentro da lista digits
i = 0
while i < len(digits):
	if i == 0:
		x = miN = maX = digits[i]
	else:
		if digits[i] > x:
			maX = digits[i]
			x = maX 
		if digits[i] < x:
			miN = digits[i]
			x = miN
	i = i + 1
	
print('O valor máximo da lista é ' + str(maX))
print('O valor mínimo da lista é ' + str(miN))

              # Fazendo a soma dos elementos da lista

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]            
i = 0
soma = 0
while i < len(digits):
	soma = soma + digits[i]
	i = i + 1
print('A soma dos elementos da lista é ' + str(soma))
