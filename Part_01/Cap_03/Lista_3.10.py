numeros = [1, 30, 60, 50 , 100, 200]
print('Lista inicial')
print(numeros)
print('Insert')
numeros.insert(0, 55)
print(numeros)
print('Append')
numeros.append(88)
print(numeros)
print('Del')
del numeros[4]
print(numeros)
print('Pop')
numero_retirado = numeros.pop(1)
print(numeros)
print('O numero ' + str(numero_retirado) + ' foi retirado da lista')

print('Remove')
numero_remouvido = 100
numeros.remove(numero_remouvido)
print(numeros)
print('\nO numero ' + str(numero_remouvido) + ' foi retirado da lista')

