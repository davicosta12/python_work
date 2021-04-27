import pygame.font
from pygame.sprite import Group
from ship import EspacoNave

class Scoreboard():
    """"Uma classe para mostrar informações sobre pontuação."""

    def __init__(self, ai_settings, superficie, stats):
        """"Inicializa os atributos da pontuação."""
        self.superficie = superficie
        self.superficie_rect = superficie.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (0, 220 ,0)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuação inicial
        self.prep_images()


    def prep_images(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_ships(self):
        """"Mostra quantas espaçonaves restam."""
        self.espaconaves = Group()
        for espaconave_number in range(self.stats.espaconave_left):
            espaconave = EspacoNave(self.ai_settings, self.superficie)
            espaconave.rect.x = 15 + espaconave_number * 1.5 * espaconave.rect.width
            espaconave.rect.y = 15
            self.espaconaves.add(espaconave)


    def prep_level(self):
        """"Transforma o nível em uma imagem renderizada."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            None)

        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_high_score(self):
        """"Transforma a pontuação máxima em uma imagem renderizada."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                      None)

        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.superficie_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_score(self):
        """"Transforma a pontuação em uma imagem renderizada."""
        roundes_score = round(self.stats.score, -1)
        score_str = "{:,}".format(roundes_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                        None)

        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.superficie_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        """"Desenha a pontuação na tela."""
        self.superficie.blit(self.score_image, self.score_rect)
        self.superficie.blit(self.high_score_image, self.high_score_rect)
        self.superficie.blit(self.level_image, self.level_rect)
        # Desenha as espaçonaves
        self.espaconaves.draw(self.superficie)