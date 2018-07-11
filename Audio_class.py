import pygame
import random
import time


class Audio:
    def __init__(self, num):
        self.length = num
        self.song_len = -100
        self.counter = time.time()
        self.all_music = None
        self.now_playing = None
        self.load_some_music()
        self.changer = False
        self.sounds = {'apple': pygame.mixer.Sound('sounds/apple.ogg'),
                       'turn': pygame.mixer.Sound('sounds/turn.ogg'),
                       }

    def load_some_music(self):
        self.all_music = [pygame.mixer.Sound('music/track_{}.ogg'.format(i)) for i in range(self.length)]

    def play_something_bro(self):
        try:

            if not time.time() - self.counter < self.song_len or self.changer:
                self.now_playing = self.all_music[random.randint(0, self.length-1)]
                self.now_playing.play()
                self.song_len = self.now_playing.get_length()
                self.counter = time.time()
                self.changer = False

        except IndexError:
            self.load_some_music()

    def play_a_sound(self, sound):
        self.sounds[sound].play()

    def stop_it_man(self):
        self.now_playing.stop()

    def play_again(self):
        self.now_playing.play()

    def play_another_one(self):
        self.stop_it_man()
        self.changer = True


def play_an_apple():
    pygame.mixer.Sound('sounds/eat.ogg').play()


def play_a_scream():
    pygame.mixer.Sound('sounds/turn.ogg').play()


def play_death():
    pygame.mixer.Sound('sounds/death.ogg').play()


def money_sound():
    pygame.mixer.Sound('sounds/money.ogg').play()