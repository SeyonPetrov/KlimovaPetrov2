from pygame import *
import pygame
import sys
import os
import menu


init()
screen = display.set_mode((1080, 540), NOFRAME)
clock = time.Clock()
flag_for_move = []
from_start_time = 0
menu.menu()
mouse.set_visible(False)



def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert_alpha()
    return image


class Hero(sprite.Sprite):
    def __init__(self, xp, pp, x, y):
        super().__init__(group_for_hero)
        self.rect = Rect(x, y, 100, 74)
        self.xp = xp
        self.punch_power = pp
        self.spr = []
        self.num_of_spr = 0
        self.move()
        self.image = self.spr[self.num_of_spr]
        self.n = self.rect.y
        self.last_move = ''
        self.mask = mask.from_surface(self.image)

    def take_damage(self, punch_power):
        self.xp = self.xp - punch_power

    def my_damage(self):
        return self.punch_power

    def my_health(self):
        return self.xp

    def move(self, fly=False, up=False):
        if fly:
            self.spr.clear()
            for i in range(len(os.listdir('data/jump'))):
                if 'l' in flag_for_move:
                    im = transform.scale(load_image(f'jump/3.png'), (100, 74))
                    self.spr.append(transform.flip(im, True, False))
                else:
                    self.spr.append(transform.scale(load_image(f'jump/3.png'), (100, 74)))
                self.rect.y += 5
                self.n = self.rect.y

        if not flag_for_move and not fly:
            self.spr.clear()
            for i in range(len(os.listdir('data\idle'))):
                self.spr.append(load_image(f'idle\{i}.png'))

        if 'r' in flag_for_move and not fly:
            self.spr.clear()
            for i in range(len(os.listdir('data/run'))):
                self.spr.append(load_image(f'run/{i}.png'))
                self.rect.x += 1

        if 'u' in flag_for_move:
            self.spr.clear()
            for i in range(len(os.listdir('data/jump'))):
                self.n += 1
                if self.n >= 300:
                    if 'l' in flag_for_move:
                        im = transform.scale(load_image(f'jump/2.png'), (100, 74))
                        self.spr.append(transform.flip(im, True, False))
                    else:
                        self.spr.append(transform.scale(load_image(f'jump/2.png'), (100, 74)))
                    self.rect.y -= 5
                else:
                    if 'u' in flag_for_move:
                        flag_for_move.remove('u')

        if 'l' in flag_for_move and not fly:
            self.spr.clear()
            for i in range(len(os.listdir('data/run'))):
                self.spr.append(transform.flip(load_image(f'run/{i}.png'), True, False))
                self.rect.x -= 1

        if 'a1' in flag_for_move and not fly:
            self.spr.clear()
            for i in range(len(os.listdir('data/attack_1'))):
                self.spr.append(transform.scale(load_image(f'attack_1/{i}.png'), (100, 74)))

        if 'a2' in flag_for_move and not fly:
            self.spr.clear()
            for i in range(len(os.listdir('data/attack_2'))):
                self.spr.append(transform.scale(load_image(f'attack_2/{i}.png'), (100, 74)))

        for i in range(len(self.spr)):
            self.num_of_spr += 1
            if self.num_of_spr >= 4:
                self.num_of_spr = 0
            self.image = self.spr[self.num_of_spr]
            self.mask = mask.from_surface(self.image)
        if flag_for_move:
            self.last_move = flag_for_move[-1]


class Line(sprite.Sprite):
    def __init__(self):
        super().__init__(line)
        scrn = Surface([1080, 2])
        draw.rect(scrn, Color(0, 0, 0, 0), (0, 0, 1080, 2))
        self.image = scrn
        self.rect = Rect(0, 480, 1080, 2)


line = sprite.Group()
li = Line()
group_for_hero = sprite.Group()
hero = Hero(1000, 10, 300, 300)


while True:
    screen.fill('black')
    from_start_time = time.get_ticks()
    for e in event.get():
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            quit()
            sys.exit()

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                flag_for_move.append('a2')
            if e.button == 3:
                flag_for_move.append('a1')

        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                if 'a2' in flag_for_move:
                    flag_for_move.remove('a2')

            if e.button == 3:
                if 'a1' in flag_for_move:
                    flag_for_move.remove('a1')

        if e.type == KEYDOWN:

            if e.key == K_RIGHT or e.key == K_d:
                flag_for_move.append('r')

            if e.key == K_LEFT or e.key == K_a:
                flag_for_move.append('l')

            if e.key == K_UP or e.key == K_w:
                flag_for_move.append('u')

            if e.key == K_DOWN or e.key == K_s:
                flag_for_move.append('d')

        if e.type == KEYUP:

            if e.key == K_RIGHT or e.key == K_d:
                if 'r' in flag_for_move:
                    flag_for_move.remove('r')

            if e.key == K_LEFT or e.key == K_a:
                if 'l' in flag_for_move:
                    flag_for_move.remove('l')

            if e.key == K_UP or e.key == K_w:
                if 'u' in flag_for_move:
                    flag_for_move.remove('u')

            if e.key == K_DOWN or e.key == K_s:
                if 'd' in flag_for_move:
                    flag_for_move.remove('d')
    for s in group_for_hero:
        if not sprite.collide_mask(s, li):
            hero.move(fly=True)
    line.draw(screen)
    group_for_hero.draw(screen)
    hero.move()
    display.flip()
    clock.tick(10)
