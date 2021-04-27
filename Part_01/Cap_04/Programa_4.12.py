	# Printando a lista

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friends_foods)

	# Printando os itends da lista com o FOR
	
print('\n')	
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are: ")
for food in my_foods:
	print(food)
	
print("\nMy friend's favorite foods are: ")
for food in friends_foods:
	print(food)
