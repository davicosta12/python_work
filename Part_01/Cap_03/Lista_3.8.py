# Importante reparar, quando usamos o método sort, a lista é modificada permanentemente, diferentemente se usarmos
# a função externa sorted, que no caso não altera a lista principal.
# podemos usar dentro da sort ou sorted o reverse = true, para definirmos a ordem alfabética inversa
# Outra coisa, podemos usar o método reverse, com intuito de inverter a ordem dos elementos da lista


lugares = ['Suiça', 'Canada', 'Estados Unidos', 'Dublin', 'Inglaterra']

print('\n')
print('Printando a lista')
print(lugares)
print('\n')

print('Lista em ordem alfabética')
print(sorted(lugares))
print('\n')
print('Printando a lista')
print(lugares)
print('\n')
print('Lista em ordem alfabética inversa')
print(sorted(lugares, reverse = True))
print('\n')
print('Printando a lista')
print(lugares)
print('\n')

print('Usando o método reverse')
lugares.reverse()
print('\n')
print('Printando a lista')
print(lugares)
print('\n')

print('Usando o método reverse novamente')
lugares.reverse()
print('\n')
print('Printando a lista')
print(lugares)
print('\n')

print('Usando o método sort')
lugares.sort()
print('\n')
print('Printando a lista')
print(lugares)
print('\n')

print('Usando o método sort usando o reverse')
lugares.sort(reverse = True)
print('\n')
print('Printando a lista')
print(lugares)
