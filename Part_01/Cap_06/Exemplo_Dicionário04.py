# Dicionários dentro de listas

aliens_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
aliens_1 = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
aliens_2 = {'color': 'red', 'points': 15, 'speed': 'fast'}

#aliens = [aliens_0, aliens_1, aliens_2]
#for alien in aliens:
	#print(alien)
	
#print("\n\n")


# armazenando 250 aliens iguais em uma lista, usando dicionários
aliens = []
for alien_number in range(0, 250):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# modficando somente os aliens do nosso interesse, por meio de fatias da lista	
for alien in aliens[0:10]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
		
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'

# printando os aliens para notar a modificação nessa fatia				
for alien in aliens[0:20]:
	print(alien)	
print("...")


print("Total number of aliens: " + str(len(aliens)))
	
	
