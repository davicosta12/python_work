	# Estágios da vida
	
age = int(input("Informe a idade da pessoa: "))
if age < 2:
	print("É um bebê!" )
elif age < 4:
	print("É uma criança!")
elif age < 13:
	print("É um(a) garoto(a)")
elif age < 20:
	print("É um(a) adolescente")
elif age < 65:
	print("É um adulto")
elif age >= 65:
	print("É um(a) idoso(a)") 
	
# OUTRO FORMA

age = int(input("Informe a idade da pessoa: "))
if age < 2:
	print("É um bebê!" )
elif age < 4:
	print("É uma criança!")
elif age < 13:
	print("É um(a) garoto(a)")
elif age < 20:
	print("É um(a) adolescente")
elif age < 65:
	print("É um adulto")
else:
	print("É um(a) idoso(a)") 
