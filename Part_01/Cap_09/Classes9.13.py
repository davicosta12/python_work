# Glossário 2
from collections import OrderedDict

glossario = OrderedDict()

glossario['chave_valor'] = 'Está presente no dicionário python, toda chave aponte para o seu respectivo valor'
glossario['list'] = 'Uma lista é um conjunto de itens em uma ordem, não necessária. Toda lista é mutável'
glossario['tuple'] = 'Uma tupla é um conjunto de itens em uma ordem em particular. Toda tupla é imutável'
glossario['variavel'] = 'Uma variavel é um espaço alocado da memória, que armazena um determinado valor'
glossario['float'] = 'Float é uma atribuição dada a variavel, o campo float gera somente valores reais'
glossario['ativista'] = 'Quem atua e trabalha por uma ideologia política ou social; militante.'
glossario['pretensioso'] = 'Característica de quem tem presunção, vaidade ou aquele que deseja ser bem mais do que é realmente: os pretensiosos nunca entendem a rejeição.'
glossario['Desdenhar'] = 'Demonstrar falta de consideração por algo ou por alguém; tratar com falta de amor e desprezo; apresentar desdém por; desprezar: desdenhar a boa-fé das pessoas; desdenhar de sua própria família.'
glossario['Rechaçar'] = 'Possuir uma posição contrária a algo ou alguém; opor-se: rechaçar a oferta.'
glossario['Conveniência'] = 'Característica de conveniente, do que convém, é apropriado ou oportuno ou favorável: aceitei seu convite por conveniência.'

for algo, significado in glossario.items():
	print(algo + ": " + significado + "\n")
