class GameStats():
    """"Armazena dados estatísticos da Invasão Alienígena."""

    def __init__(self, ai_settings):
        """"Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Inicia a Invasão Alienígena em um estado ativo
        self.game_active = False

        # a pontuação máxima jamais deverá ser reiniciada
        self.high_score = self.read_high_score()


    def reset_stats(self):
        """"Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.espaconave_left = self.ai_settings.espaconave_limit
        self.score = 0
        self.level = 1


    def read_high_score(self):
        with open("write_high_score.txt", "r") as obj_function:
            line = obj_function.readline()
            line = line.rstrip()
            self.high_score = line
            return int(self.high_score)

