sandwich_orders = ['sanduíche de atum', 'sanduíche de goiaba', 
'sanduíche de presunto', 'sanduíche de pastrami', 'sanduíche de queijo', 
'sanduíche de especial', 'sanduíche da casa', 'sanduíche de pastrami',
 'sanduíche de ketchup', 'sanduíche de pastrami','sanduíche do viralata']
finished_sandwichs = []

print("\nA lanchonete está sem sanduíche de pastrami, pedimos que colabore.\n")

while 'sanduíche de pastrami' in sandwich_orders:
	sandwich_orders.remove('sanduíche de pastrami')

while sandwich_orders:
	preparado = sandwich_orders.pop()
	print("Preparei seu " + preparado.title())
	finished_sandwichs.append(preparado)
	
print("\n--- Lista dos sanduíches preparados ---\n")	
for finished_sandwich in finished_sandwichs:
	print(finished_sandwich.title())
