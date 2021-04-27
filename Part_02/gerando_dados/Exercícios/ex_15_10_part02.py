import pygal

from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo


# Cria um passeio aleatório e plota os pontos
rw = RandomWalk()
rw.fill_walk()

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Passeio aleatório."
hist.x_labels = rw.x_values
hist.x_title = "Valores de x"
hist.y_title = "Valores de y"

hist.add('Escolha', rw.y_values)
hist.render_to_file('dice_passeio_visual.svg')

    