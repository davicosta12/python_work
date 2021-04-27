def construindo_perfil(primeiro, last, **user_info): # dois asterísco fazem python criar um dicionário vazio e colocar quaisquer pares nome-valor recebidos nesse dicionário.
	perfil = {}
	perfil['primeiro_nome'] = primeiro
	perfil['last_name'] = last
	
	for key, value in user_info.items():
		perfil[key] = value 
	return perfil


perfil_usuario = construindo_perfil('davi', 'silva',
									location = 'fatec',
									ocupacao = 'análise e desenvolvimento de sistemas',
									status = 'felicidade pura')
print(perfil_usuario)
