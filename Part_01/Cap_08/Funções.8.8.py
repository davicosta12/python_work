def make_album(artist_name, title):
	album_musical = {'name': artist_name, 'album_title': title}	
	return album_musical

print("\n Digite o que está sendo pedido, caso deseje sair, digite 'q'")
while True:
	name = input("\n Escreva o nome do artista: ")
	if name == 'q':
		break
	album = input(" Informe o nome do album desse artista: ")
	if album == 'q':
		break
		
	album_information = make_album(name, album)
	print("\n --- Aqui está o dicionario com as informações ---\n")
	print(album_information)
