class Settings():

    def __init__(self):
        # Configurações da tela
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (125, 125, 125)

        # Configurações da espaço nave
        self.ship_speed_factor = 1

        # Configurações da bala
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 0, 0, 0
        self.bullet_speed_factor = 2
        self.bullet_limit_error = 3
        self.bullet_limited = 1

        # Configurações do alvo
        self.alvo_width = 15
        self.alvo_height = 52
        self.alvo_color = 228, 0 , 0
        self.alvo_speed_factor = 0.5
        self.alvo_direction = 1

        self.increase_speed = 1.1


    def inicializa_com_a_direction_correta(self):
        self.alvo_direction = 1


    def inicializa_config(self):
        self.alvo_speed_factor = 0.5
        self.alvo_direction = 1


    def incrementa_novas_configs(self):
        self.alvo_speed_factor = self.alvo_speed_factor * self.increase_speed
