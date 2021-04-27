import pygame
from os import path

class Music():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings


    def music_intro(self):
        pygame.mixer.music.load("sounds/music_intro.ogg")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)


    def music_gameplay(self):
        pygame.mixer.music.load("sounds/music.ogg")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)


    def sound_list_explosions(self):
        sound_dir = path.join(path.dirname(__file__), 'sounds')
        explosion_sound = []
        for sound in ["Explosion01.wav", "Explosion02.wav", "Explosion03.wav"]:
            explosion_sound.append(pygame.mixer.Sound(path.join(sound_dir, sound)))

        return explosion_sound


    def stop_music(self):
        pygame.mixer.music.stop()