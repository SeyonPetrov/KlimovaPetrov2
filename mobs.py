from pygame import *
from pygame import image
from random import randint
import os
import sys


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    im = image.load(fullname).convert_alpha()
    return im


class Mobs(sprite.Sprite):
    def __init__(self, x, y, lvl, hero):
        super().__init__()
        self.mob = randint(0, 1)
        self.n = 0
        self.hero = hero
        self.rect = Rect(x, y, 140, 93)
        self.index = 0
        if lvl == 1:
            self.index = 1

        elif lvl == 2:
            self.index = 2

        elif lvl == 3:
            self.index = 4

        elif lvl == 4:
            self.index = 6
        self.normal_xp = 500 * self.index
        self.xp = 0
        self.xp += self.normal_xp
        self.damage = randint(20 * self.index, 50 * self.index)
        self.h_move = []
        self.spr = []
        self.current = 0
        self.mob = randint(1, 2)
        self.flag = True
        self.move()
        self.image = self.spr[self.current]
        self.mask = mask.from_surface(self.image)

    def take_damage(self, punch_power):
        self.xp = self.xp - punch_power

    def mob_damage(self):
        return self.damage

    def mob_health(self):
        return self.xp

    def on_place(self):
        if self.rect.y > 550:
            self.xp -= 10000

    def hero_moves(self, spisok):
        self.h_move = spisok

    def hit_box(self, sur):
        xp_proz = self.xp / self.normal_xp
        draw.rect(sur, 'red', (720, 20, int(340 * xp_proz), 15))
        draw.rect(sur, 'white', (713, 18, 357, 19), 3)
        text = font.Font('sprites_Back/Fifaks10Dev1.ttf', 40).render('МОНСТР', True, 'red')
        sur.blit(text, (1070 - (357 - ((357 - text.get_width()) // 2)), 35))

    def move(self, fly=False):
        orientation = randint(0, 2)
        jump = randint(0, 1)
        attack = randint(0, 4)
        if attack % 2 != 0:
            attack = 1
        else:
            attack = 0

        if attack and not fly:
            self.spr.clear()
            for i in range(len(os.listdir(f'data/mobs/{self.mob}/attack'))):
                if self.hero.rect.x > self.rect.x:
                    im = load_image(f'mobs/{self.mob}/attack/{i}.png')
                    im2 = transform.scale(im, (im.get_width() * 2, im.get_height() * 2))
                    self.spr.append(transform.flip(im2, True, False))
                else:
                    im = load_image(f'mobs/{self.mob}/attack/{i}.png')
                    im2 = transform.scale(im, (im.get_width() * 2, im.get_height() * 2))
                    self.spr.append(im2)
            if not self.flag:
                if sprite.collide_mask(self, self.hero):
                    self.hero.take_damage(self.damage)

        elif orientation == 1 and not fly and not attack:
            self.spr.clear()
            for i in range(len(os.listdir(f'data/mobs/{self.mob}/run'))):
                im = load_image(f'mobs/{self.mob}/run/{i}.png')
                im2 = transform.scale(im, (im.get_width() * 2, im.get_height() * 2))
                self.spr.append(im2)
                self.rect.x += self.index

        elif not orientation and not fly and not attack:
            self.spr.clear()
            for i in range(len(os.listdir(f'data/mobs/{self.mob}/run'))):
                im = load_image(f'mobs/{self.mob}/run/{i}.png')
                im2 = transform.scale(im, (im.get_width() * 2, im.get_height() * 2))
                self.spr.append(transform.flip(im2, True, False))
                self.rect.x -= self.index

        elif orientation == 2 and not fly and not attack:
            self.spr.clear()
            for i in range(len(os.listdir(f'data/mobs/{self.mob}/idle'))):
                im = load_image(f'mobs/{self.mob}/idle/{i}.png')
                im2 = transform.scale(im, (im.get_width() * 2, im.get_height() * 2))
                self.spr.append(im2)

        elif fly:
            self.spr.clear()
            for i in range(len(os.listdir(f'data/mobs/{self.mob}/idle'))):
                im = load_image(f'mobs/{self.mob}/idle/2.png')
                im2 = transform.scale(im, (im.get_width() * 2, im.get_height() * 2))
                self.spr.append(im2)
                self.rect.y += 1

        elif jump and not attack:
            self.spr.clear()
            for i in range(len(os.listdir(f'data/mobs/{self.mob}/idle'))):
                im = load_image(f'mobs/{self.mob}/idle/3.png')
                im2 = transform.scale(im, (im.get_width() * 2, im.get_height() * 2))
                self.spr.append(im2)
                self.rect.y -= 1

        for i in range(len(self.spr)):
            self.current += 1
            if self.current >= 8:
                self.current = 0
            self.image = self.spr[self.current]
            self.mask = mask.from_surface(self.image)
        self.flag = False
        self.on_place()
        if self.hero_moves:
            if 'a1' in self.h_move or 'a2' in self.h_move:
                if sprite.collide_mask(self, self.hero):
                    self.take_damage(self.hero.my_damage())
