class Stats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings

        self.game_active = False
        self.game_reset()

    def game_reset(self):
        self.bullet_limit = self.ai_settings.bullet_limit_error
