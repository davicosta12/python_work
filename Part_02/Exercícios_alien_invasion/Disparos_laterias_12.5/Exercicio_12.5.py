import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Bullet(Sprite):

    def __init__(self, configure, superficie, espaconave, bullets):
        super().__init__()
        self.superficie = superficie
        self.bullet_rect = pygame.Rect(0, 0, configure.bullet_largura, configure.bullet_altura)
        self.bullet_rect.centery = espaconave.rect.centery
        self.bullet_rect.right = espaconave.rect.right

        self.posicao_inicial_x = float(self.bullet_rect .x)

        self.bullet_color = configure.bullet_color
        self.bullet_speed_factor = configure.bullet_speed_factor


    def update(self):
        self.posicao_inicial_x = self.posicao_inicial_x + self.bullet_speed_factor
        self.bullet_rect.x = self.posicao_inicial_x

    def desenha_bala(self):
        pygame.draw.rect(self.superficie, self.bullet_color, self.bullet_rect)

class Espaconave():
    # classe que foca só na espaço nave
    def __init__(self, configure, superficie):
        # montando a espaço nave
        self.configure = configure
        self.superficie = superficie

        self.imagem = pygame.image.load('foguete.bmp')
        self.rect = self.imagem.get_rect()
        self.superficie_retangulo = self.superficie.get_rect()

        self.rect.centery = self.superficie_retangulo.centery
        self.rect.left = self.superficie_retangulo.left

        self.y = float(self.rect.bottom)

        # Flag de movimento
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # movimentação da espaçonave
        if self.moving_up and self.rect.top > 0:
            self.y = self.y - self.configure.velocidade_da_ship
        if self.moving_down and self.rect.bottom < self.superficie_retangulo.bottom:
            self.y = self.y + self.configure.velocidade_da_ship

        self.rect.bottom = self.y

    def desenha_imagem_para_mim(self):
        # desenhando a imagem na tela
        self.superficie.blit(self.imagem, self.rect)


class Settings():
    # Configurações do jogo
    def __init__(self):
        # Configurações da tela
        self.superficie_largura = 1200
        self.superficie_altura = 800
        self.bg_color = (0, 150, 230)
        self.velocidade_da_ship = 1.5

        # Configurações da tela
        self.bullet_largura = 15
        self.bullet_altura = 3
        self.bullet_color = 190, 190, 190
        self.bullet_speed_factor = 1
        self.bullet_permition = 60


def checa_eventos(configure, superficie, espaconave, bullets):
    # Pega eventos do teclado e mouse
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                espaconave.moving_up = True
            elif evento.key == pygame.K_DOWN:
                espaconave.moving_down = True
            elif evento.key == pygame.K_SPACE:
                if len(bullets) < configure.bullet_permition:
                    new_bullet = Bullet(configure, superficie, espaconave, bullets)
                    bullets.add(new_bullet)

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP:
                espaconave.moving_up = False
            elif evento.key == pygame.K_DOWN:
                espaconave.moving_down = False


def update_superficie(configure, superficie, espaconave, bullets):
    # Redesenha a tela a cada loop
    superficie.fill(configure.bg_color)

    # Desenha a imagem
    espaconave.desenha_imagem_para_mim()

    # Desenha os projéteis
    for bullet in bullets.sprites():
        bullet.desenha_bala()

    # Pega a tela mais recente
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.bullet_rect.x >= 1200:
            bullets.remove(bullet)
        print(len(bullets))


def run_game():
    pygame.init()

    configure = Settings()
    superficie = pygame.display.set_mode((configure.superficie_largura, configure.superficie_altura))
    pygame.display.set_caption("Foguete")

    # Criando uma espaço nave
    espaconave = Espaconave(configure, superficie)

    bullets = Group()

    while True:
        checa_eventos(configure, superficie, espaconave, bullets)
        espaconave.update()
        update_bullets(bullets)
        update_superficie(configure, superficie, espaconave, bullets)

run_game()
