import make_sandwich     # ---> importa todas as funçoes, mas precisamos chamar cada uma usando o '.'

print("\n --- Ingregientes a ser usados no sanduíche --- ")
make_sandwich.make_sandwich('queijo', 'picles', 'ovo', 'cheedar', 'alface', 'pepino')

from make_sandwich import make_sandwich # ---> importa uma função específica
	
print("\n --- Ingregientes a ser usados no sanduíche --- ")
make_sandwich('queijo', 'picles', 'ovo', 'cheedar', 'alface', 'pepino')

from make_sandwich import make_sandwich as ms # 'as' é um aliás, determina um nome qualquer

print("\n --- Ingregientes a ser usados no sanduíche --- ")
ms('queijo', 'picles', 'ovo', 'cheedar', 'alface', 'pepino')

import make_sandwich as ms #importa todas as funçoes, mas precisamos chamar cada uma usando o '.', com um aliás dado por nos

print("\n --- Ingregientes a ser usados no sanduíche --- ")
ms.make_sandwich('queijo', 'picles', 'ovo', 'cheedar', 'alface', 'pepino')

from make_sandwich import *  # o asterísco quer dizer que tudo tem que ser importado para nosso programa (método menos eficiente)

print("\n --- Ingregientes a ser usados no sanduíche --- ")
make_sandwich('queijo', 'picles', 'ovo', 'cheedar', 'alface', 'pepino')
