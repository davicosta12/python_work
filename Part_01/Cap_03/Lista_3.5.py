# Alterando a lista e os convites para o jantar

Lista_convidados = ['Arthur', 'Joelma', 'Rafael', 'Gabriel', 'Vitor', 'João']
a = Lista_convidados[0]
b = Lista_convidados[1]
c = Lista_convidados[2]
d = Lista_convidados[3]
e = Lista_convidados[4]
f = Lista_convidados[5]

# Printando os convites para os convidados

print('\n' + a + ' você está convidado para o jantar')
print(b + ' você está convidado para o jantar')
print(c + ' você está convidado para o jantar')
print(d + ' você está convidado para o jantar')
print(e + ' você está convidado para o jantar')
print(f + ' você está convidado para o jantar')

# Usando o método pop e armazenando o elemento apagado na variável Convidado_alterado

Convidado_alterado = Lista_convidados.pop(3)
print('\n' + Convidado_alterado + ' não irá comparecer no jantar')

# Usando o método insert, com intuiro de inserir o novo convidado no lugar do outro que não irá comparecer, armazenando na variável d o convidado novo, chamado Daniel

Lista_convidados.insert(3, 'Daniel')
d = Lista_convidados[3]

# Printando os convites para os novos convidados

print('\n' + a + ' você está convidado para o jantar')
print(b + ' você está convidado para o jantar')
print(c + ' você está convidado para o jantar')
print(d + ' você está convidado para o jantar')
print(e + ' você está convidado para o jantar')
print(f + ' você está convidado para o jantar')
