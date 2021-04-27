# Mesmo exemplo com funções, usando como argumento uma lista
def imprime_design(print_design, complet_design):
	while print_design:
		preparando = print_design.pop()
		print("\n Preparando e printando: " + preparando.title())
		complet_design.append(preparando)

def mostra_modelos_concluidos(complet_design):
	for modelo in complet_design:
		print(" " + modelo.title())

printando_design = ['iphone case', 'robot pendant', 'dodecahedron']
design_completos = []

imprime_design(printando_design[:], design_completos)
print("\n --- Lista dos design que foram completados --- \n")
mostra_modelos_concluidos(design_completos)
