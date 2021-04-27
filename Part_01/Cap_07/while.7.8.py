sandwich_orders = ['sanduíche de atum', 'sanduíche de goiaba', 
'sanduíche de presunto', 'sanduíche de queijo', 'sanduíche de especial',
'sanduíche da casa', 'sanduíche de ketchup', 'sanduíche do viralata']
finished_sandwichs = []

while sandwich_orders:
	preparado = sandwich_orders.pop()
	print("Preparei seu " + preparado.title())
	finished_sandwichs.append(preparado)
	
print("\n--- Lista dos sanduíches preparados ---")	
for finished_sandwich in finished_sandwichs:
	print(finished_sandwich.title())
