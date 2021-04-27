# printando chaves-valores, somente chaves e somente valores

Rios_importantes = {
	'nilo': 'egito',
	'tigre': 'iraque',
	'eufrates': 'síria',
}

for rio, pais in Rios_importantes.items():
	print("O rio " + rio.title() + " corre pelo " + pais)
	
print("\nNome dos rios")
for rio in Rios_importantes.keys():
	print(rio)

print("\nNome de cada país")
for pais in Rios_importantes.values():
	print(pais)
