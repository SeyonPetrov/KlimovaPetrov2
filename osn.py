import pygame.image
from pygame import *
import sys
import random
import os


def spisok_pol(rez):
    a = random.randint(1, 2)
    if a == 1:
        p1 = pygame.image.load(f'sprites_Back/Пол{rez}/{a}.png').convert_alpha()
    else:
        p1 = 0
    return pygame.image.load(f'sprites_Back/Пол{rez}/End.png').convert_alpha()


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert_alpha()
    return image


class Mountain(pygame.sprite.Sprite):
    def __init__(self, x, y, rez, firts=False):
        super().__init__()
        im = spisok_pol(rez)
        if firts:
            im = pygame.image.load(f'sprites_Back/Пол{rez}/End.png')
        self.image = im
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = mask.from_surface(self.image)
