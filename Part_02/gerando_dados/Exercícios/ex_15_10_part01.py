import matplotlib.pyplot as plt

from die import Die

# Cria um D6
die = Die()
die_00 = Die()
die_01 = Die()


# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000):
    result = die_00.roll() + die_01.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
min_result = 2
max_result = die_00.num_sides + die_01.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados

list_x_labels = die.gera_list_labels_x(min_result, max_result)

x_values = list_x_labels
y_values = frequencies

plt.plot(x_values, y_values, c='Red', linewidth=2)
plt.title("Results of rolling two D6 50,000 times.", fontsize=24)
plt.xlabel("Results", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.show()