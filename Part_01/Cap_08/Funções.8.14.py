def make_car(car_name, nome_fabricante, **informacoes_carro):
	dicionario_car = {}
	dicionario_car['nome do carro'] = car_name
	dicionario_car['nome fabricante'] = nome_fabricante
	
	for key, value in informacoes_carro.items():
			dicionario_car[key] = value
	return dicionario_car
	
informacoes_do_carro = make_car('mercedes', 'Mercedes-Benz',
								cor = 'cinza',
								tow_package = True,
								largura = '2m')
print(informacoes_do_carro)
