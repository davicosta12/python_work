# COPIANDO OS DADOS DO EX 4.1
# Copiando itens de uma lista para a outro, sendo que uma é 
# independente da outra.

pizzas = ['mussarela', 'catupiry', 'pepperone']
# Nunca fazer isso ---> pizzas = friend_pizzas, pois as duas variaveis 
# estarão apontando para a mesma lista, isto é, são completamente iguais

friend_pizzas = pizzas[:]

pizzas.append('calabresa')
friend_pizzas.append('4 queijos')

print('Minhas pizzas favoritas são: ')
for pizza in pizzas:
	print(pizza)

print('\nAs pizzas favoritas do meu amigo são: ')
for pizza in friend_pizzas:
	print(pizza)
