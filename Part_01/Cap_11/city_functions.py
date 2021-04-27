def devolve_city_country(cidade, pais, population=''):
	if population:
		string_formatada = cidade + ", " + pais + " - população " + str(population)
	else:
		string_formatada = cidade + ", " + pais 
	return string_formatada.title() 

print(devolve_city_country("são paulo", "brasil", 500000
))
