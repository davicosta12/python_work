def construindo_perfil(primeiro, last, **user_info): 
	perfil = {}
	perfil['primeiro_nome'] = primeiro
	perfil['last_name'] = last
	
	for key, value in user_info.items():
		perfil[key] = value 
	return perfil


perfil_usuario = construindo_perfil('davi', 'silva',
									location = 'fatec',
									ocupacao = 'análise e desenvolvimento de sistemas',
									status = 'felicidade pura',
									jogo_favorito = 'league of legends',
									sonho = 'sempre ser feliz e ter saude')
print(perfil_usuario)
