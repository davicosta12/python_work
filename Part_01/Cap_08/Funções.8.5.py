def describe_city(nome_cidade, pais_cidade = 'brasil'):
	print("\n " + nome_cidade.title() + " está localizada no " + pais_cidade.title()) 

describe_city('são paulo')
describe_city('rio de janeiro')	
describe_city(nome_cidade = 'toronto', pais_cidade = 'canada')
