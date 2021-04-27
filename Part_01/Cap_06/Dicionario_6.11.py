cities = {
	'sao paulo': { 
		'country': 'brasil',
		'population': 12000000,
		'fact': 'the best place ever',		 
		},
	
	'francisco morato': { 
		'country': 'brasil',
		'population': 60,
		'fact': 'lugar de doido',		 
		},
		
	'fraco da rocha': { 
		'country': 'brasil',
		'population': 12000,
		'fact': 'a natureza é relevante nesse lugar',		 
		},	
	}
	
for cidade, informacoes in cities.items():
	print("\n A cidade de " + cidade.title() + 
		" apresenta as seguintes características: ")		
	print("\t Localização: " + informacoes['country'].title())		
	print("\t Sua população é de aproximadamente " 
		+ str(informacoes['population']))
	print("\t Um fato: " + informacoes['fact'])
