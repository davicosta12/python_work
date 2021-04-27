pai = 'andre'
print("\nSerá que pai == 'andre' Eu acredito que sim")
print (pai == 'andre')

print("\nSerá que pai == 'marcos' Eu acredito que não")
print(pai == 'marcos')

print("\n")

heroi = 'Batman'
print("\nSerá que heroi.lower() == 'batman' Eu acredito que sim")
print(heroi.lower() == 'batman')

print("\nSerá que heroi.lower() == 'Batman' Eu acredito que não")
print(heroi.lower() == 'Batman')

print("\n")

numero = 23
print("\nSerá que numero != 44 Eu acredito que sim")
print(numero != 44)

print("\nSerá que numero != 23 Eu acredito que não")
print(numero != 23)

print("\nSerá que numero < 44 Eu acredito que sim")
print(numero < 44)

print("\nSerá que numero > 44 Eu acredito que não")
print(numero > 44)

print("\nSerá que numero <= 23 Eu acredito que sim")
print(numero <= 23)

print("\nSerá que numero >= 24 Eu acredito que não")
print(numero >= 24)

print("\n")

pais = 'alemanha'
print("Será que pais != 'brasil' and pais == 'alemanha' Eu acredito que sim")
print(pais != 'brasil' and pais == 'alemanha')

print("Será que pais != 'alemanha' or pais == 'inglaterra' Eu acredito que não")
print(pais != 'alemanha' or pais == 'inglaterra')

print("\n")

usuarios_banidos = ['Davi', 'Francisco', 'Cleber']
nome = input('Digite um nome: ')
print('Será que ' + nome + ' está banido?')
if nome not in usuarios_banidos:
	print(usuarios_banidos[0] == 'Manuel' and usuarios_banidos[0] == 'Joaquim') #False
else:
	print(usuarios_banidos[0].lower() == 'davi' or usuarios_banidos[2] == 'Marcos') #True


