# Parâmetro opcional, usando um valor default.

def make_album(artist_name, title, numero_faixas = ''):
	album_musical = {'name': artist_name, 'album_title': title}	
	if numero_faixas:
		album_musical['faixas'] = numero_faixas
	return album_musical

album_information = make_album('kiko loreiro', 'dystopia')
print(album_information)

album_information = make_album('dave mustaine', 'peace sells')
print(album_information)

album_information = make_album('james hetfield', 'and justice for all')
print(album_information)

album_information = make_album('james hetfield', 'and justice for all', 11)
print(album_information)
