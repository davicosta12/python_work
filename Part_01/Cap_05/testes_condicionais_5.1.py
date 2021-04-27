#Exemplo 1

jogo = 'call of duty'
print("\nSerá que jogo == 'call of duty?' Eu acredito que sim")
print(jogo == 'call of duty')

print("Será que jogo == 'Warzone?' Eu acredito que não")
print(jogo == 'Warzone')

print('\n')

#Exemplo 2

jogo = 'warZ'
print("Será que jogo == 'call of duty' or jogo == 'warZ' ? Eu acredito que sim")
print(jogo == 'call of duty' or jogo == 'warZ')

print("Será que jogo == 'call of duty' or jogo == 'Darkplanet' ? Eu acredito que não")
print(jogo == 'call of duty' or jogo == 'Darkplanet')

print('\n')

#Exemplo 3

alimento = 'Estrogonofe'
print("Será que o alimento.lower() == 'estrogonofe', Eu acredito que sim")
print(alimento.lower() == 'estrogonofe')

print("Será que o alimento.lower() == 'pizza', Eu acredito que não")
print(alimento.lower() == 'pizza')

print('\n')

#Exemplo 4

age_01 = 23
age_02 = 21
print("Será que age_01 == 23 and age_02 == 21, Eu acredito que sim")
print(age_01 == 23 and age_02 == 21)

print("Será que age_01 == 42 and age_02 == 21, Eu acredito que não")
print(age_01 == 42 and age_02 == 21)

print('\n')

#Exemplo 5

usuarios_banidos = ['Davi', 'Francisco', 'Cleber']
nome = input('Digite um nome: ')
print('Será que ' + nome + ' está banido?')
if nome not in usuarios_banidos:
	print(usuarios_banidos[0] == 'Manuel' and usuarios_banidos[0] == 'Joaquim') #False
else:
	print(usuarios_banidos[0].lower() == 'davi' or usuarios_banidos[2] == 'Marcos') #True





