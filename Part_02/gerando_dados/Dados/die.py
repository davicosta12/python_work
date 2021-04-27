from random import randint

class Die():
    """Uma classe que representa um único dado."""

    def __init__(self, num_sides=6):
        """Supõe que seja um dado de seis lados."""
        self.num_sides = num_sides


    def roll(self):
        """Devolve um valor aleatório entre 1 e o número de lados."""
        return randint(1, self.num_sides)


    def gera_list_labels_x(self, min_result, max_result):
        list_x_labels = []
        for number in range(min_result, max_result + 1):
            list_x_labels.append(number)
        return list_x_labels
