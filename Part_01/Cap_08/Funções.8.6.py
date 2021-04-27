def city_country(nome_cidade, pais_cidade):
	string = "\n " + nome_cidade.title() + ", " + pais_cidade.title()
	return string

string_formatada = city_country('santiago', 'chile')
print(string_formatada)

string_formatada = city_country('new york', 'usa')
print(string_formatada)
	
string_formatada = city_country('são paulo', 'brasil')
print(string_formatada)
