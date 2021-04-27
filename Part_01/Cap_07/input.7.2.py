propt = "Quantas pessoas estão em seu grupo de jantar? "
propt = propt + "\nDiga o número exato: "
num_pessoas = int(input(propt))

if num_pessoas > 8:
	print("\n\tPor gentileza, esperem uma mesa ficar vaga.")
else:
	print("\n\tSiga-me, uma mesa já está disponivel.")

