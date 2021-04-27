	#USANDO O MÉTODO DEL --> Exclui o elemento da lista, sem se preocupar com a reutilização dele na lógica seguinte. Nos precisamos saber a posição do elemento, quando usasmos del

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print('\n' + str(motorcycles))

#del motorcycles[0]
#print(motorcycles)

#del motorcycles[1]
#print(motorcycles)

	#USANDO O MÉTODO POP --> Exclui o elemento da lista, se preocupando com a reutilização dele na lógica seguinte. Não precisamos saber necessariamente a posição do elemento na lista.

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)

#Utilidade do método pop -- podemos definirar com o índice que queremos trabalhar

#motorcycles = ['honda', 'yamaha', 'suzuki']

#last_owned = motorcycles.pop()
#print("The last motorcycle I owned was a " + last_owned.title() + ".")

	# USANDO O MÉTODO REMOVE --> Exclui o elemento da lista, se preocupando com a reutilização dele na lógica seguinte. Precisamos saber somente o conteúdo e não o indice.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive for me.")
	



