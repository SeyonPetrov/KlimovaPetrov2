from pygame import *
import pygame
import sys
import os
import menu
import camera
import osn
import mobs
import sqlite3


pygame.mixer.pre_init(44100, -16, 1, 512)
init()
screen = display.set_mode((1080, 540), NOFRAME)
clock = time.Clock()
flag_for_move = []
from_start_time = 0
name, lvl, non = menu.menu()


def load_image(nam):
    fullname = os.path.join('data', nam)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    im = pygame.image.load(fullname).convert_alpha()
    return im


def recording(p_name, level, record):
    pod = sqlite3.connect('рекорды.sqlite3')
    cu = pod.cursor()
    cu.execute(f'insert into record(name, level, score) values(?, ?, ?)', (p_name, level, record)).fetchall()
    pod.commit()
    pod.close()


class Hero(sprite.Sprite):
    def __init__(self, xp, pp, x, y):
        super().__init__()
        self.rect = Rect(x, y, 100, 74)
        normal_xp = xp
        self.xp = 0
        self.xp += normal_xp
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

    def get_coords(self):
        return self.rect.x, self.rect.y

    def on_place(self):
        if self.rect.y > 550:
            self.xp -= 10000

    def move(self, fly=False, st=False):
        if fly:
            self.spr.clear()
            for i in range(len(os.listdir('data/jump'))):
                if 'l' in flag_for_move:
                    im = transform.scale(load_image(f'jump/3.png'), (100, 74))
                    self.spr.append(transform.flip(im, True, False))
                else:
                    self.spr.append(transform.scale(load_image(f'jump/3.png'), (100, 74)))
                self.rect.y += 2
                self.n = self.rect.y

        if not flag_for_move and not fly:
            self.spr.clear()
            for i in range(len(os.listdir('data\idle'))):
                self.spr.append(load_image(f'idle\{i}.png'))

        if 'r' in flag_for_move and not fly:
            if 'a1' not in flag_for_move and 'a2' not in flag_for_move:
                self.spr.clear()
                for i in range(len(os.listdir('data/run'))):
                    self.spr.append(load_image(f'run/{i}.png'))
                    self.rect.x += 0

        if 'u' in flag_for_move:
            self.spr.clear()
            for i in range(len(os.listdir('data/jump'))):
                self.n += 1
                if self.n >= 250:
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
            if 'a1' not in flag_for_move and 'a2' not in flag_for_move and not st:
                self.spr.clear()
                for i in range(len(os.listdir('data/run'))):
                    self.spr.append(transform.flip(load_image(f'run/{i}.png'), True, False))
                    self.rect.x -= 0

        if 'a1' in flag_for_move:
            self.spr.clear()
            for i in range(len(os.listdir('data/attack_1'))):
                if 'l' in flag_for_move:
                    im = transform.scale(load_image(f'attack_1/{i}.png'), (100, 74))
                    self.spr.append(transform.flip(im, True, False))
                else:
                    self.spr.append(transform.scale(load_image(f'attack_1/{i}.png'), (100, 74)))

        elif 'a2' in flag_for_move:
            self.spr.clear()
            for i in range(len(os.listdir('data/attack_2'))):
                if 'l' in flag_for_move:
                    im = transform.scale(load_image(f'attack_2/{i}.png'), (100, 74))
                    self.spr.append(transform.flip(im, True, False))
                else:
                    self.spr.append(transform.scale(load_image(f'attack_2/{i}.png'), (100, 74)))

        for i in range(len(self.spr)):
            self.num_of_spr += 1
            if self.num_of_spr >= 4:
                self.num_of_spr = 0
            self.image = self.spr[self.num_of_spr]
            self.mask = mask.from_surface(self.image)
        self.on_place()


class StartBorder(sprite.Sprite):
    def __init__(self):
        super().__init__()
        line = Surface([2, 540])
        draw.rect(line, (0, 0, 0, 0), (0, 0, 2, 540))
        self.image = line
        self.rect = Rect(0, 0, 2, 540)


class Line(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface([12345, 2])
        self.rect = Rect(0, 440, 12345, 200)


def game():
    mix = mixer.music
    mix.load('data/mortal.mp3')
    mix.set_volume(0.09)
    mix.play(-1)
    mouse.set_visible(False)
    hero = Hero(1000, 10, 300, 300)
    group_for_hero = sprite.Group(hero)
    cam = camera.Camera()
    pol = osn.Mountain(0, 0, lvl, True)
    flag = False
    grass = [pol]
    grass_group = sprite.Group()
    grass_group.add(pol)
    mob = mobs.Mobs(400, 200, lvl, hero)
    mobs_group = sprite.Group(mob)
    start_line = StartBorder()
    st = sprite.Group(start_line)
    end = False
    line = Line()
    line_g = sprite.Group(line)
    score = 0
    time1 = 1

    while True:
        screen.blit(load_image(f'{lvl}.png'), (0, 0))
        from_start_time = time.get_ticks()
        for e in event.get():
            if e.type == KEYDOWN and e.key == K_ESCAPE and end:
                recording(name, lvl, score)
                mix.stop()
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
                    cam.target(hero, 1)
                    flag = True

                if e.key == K_LEFT or e.key == K_a:
                    flag_for_move.append('l')
                    cam.target(hero, -1)
                    flag = True

                if e.key == K_UP or e.key == K_w:
                    flag_for_move.append('u')

                if e.key == K_DOWN or e.key == K_s:
                    flag_for_move.append('d')

            if e.type == KEYUP:

                if e.key == K_RIGHT or e.key == K_d:
                    if 'r' in flag_for_move:
                        flag_for_move.remove('r')
                        flag = False

                if e.key == K_LEFT or e.key == K_a:
                    if 'l' in flag_for_move:
                        flag_for_move.remove('l')
                        flag = False

                if e.key == K_UP or e.key == K_w:
                    if 'u' in flag_for_move:
                        flag_for_move.remove('u')

                if e.key == K_DOWN or e.key == K_s:
                    if 'd' in flag_for_move:
                        flag_for_move.remove('d')
                if e.key == K_v:
                    end = True
                if e.key == K_SPACE and end:
                    mix.stop()
                    ending(score, men=True)

        for s in group_for_hero:
            if not sprite.collide_mask(s, line):
                hero.move(fly=True)
            if sprite.collide_mask(s, start_line):
                hero.move(st=True)
        draw.circle(screen, 'red', (2100, 200), 5)
        group_for_hero.draw(screen)
        hero.move()
        if flag:
            for s in grass:
                cam.shift(s)
            cam.shift(start_line)
            cam.shift(mob)

        grass_group.draw(screen)
        if grass[-1].rect.x < 0:
            t = osn.Mountain(grass[-1].rect.x + 1081, 0, lvl, False)
            grass_group.add(t)
            grass.append(t)
        mobs_group.draw(screen)
        for s in mobs_group:
            if not sprite.collide_mask(s, line):
                mob.move(True)
        mob.move()
        hit = mob.rect[0] - hero.rect[0]
        if (hit <= 30 and hit >= 0) or (hit < 0 and hit >= -100):
            time1 += 1
            if time1 % 50 > 45:
                at = transform.scale(load_image('Предупреждение.png'), (100, 100))
                screen.blit(at, (300, 320))
            if time1 % 50 == 0 and hero.rect[1] == 372:
                print(hero.my_health())
                mob.n = 0
            if 'a1' in flag_for_move:
                time1 += 7
                mob.take_damage(5)
            if 'a2' in flag_for_move:
                mob.take_damage(40)
        if hero.my_health() <= 0:
            end = True
        if mob.mob_health() <= 0:
            mobs_group.remove(mob)
            mob = mobs.Mobs(1090, 200, lvl, hero)
            mobs_group.add(mob)
            time1 = 1
            score += 10
        if end:
            ending(score)
        display.flip()
        clock.tick(10)


def ending(score, men=False):
    global name, lvl, non
    text = font.Font('sprites_Back/Fifaks10Dev1.ttf', 100).render(f'{score}', True, 'lightskyblue')
    text1 = font.Font('sprites_Back/Fifaks10Dev1.ttf', 40).render('ВАШ РЕЗУЛЬТАТ', True, 'green')
    text2 = font.Font('sprites_Back/Fifaks10Dev1.ttf', 20).render('НАЖМИТЕ "ПРОБЕЛ"'
                                                                  'ЧТОБЫ ВЫЙТИ В МЕНЮ', True, 'yellow')
    txt3 = font.Font('sprites_Back/Fifaks10Dev1.ttf', 20).render('ИЛИ "ESCAPE" ЧТОБЫ ЗАКРЫТЬ ИГРУ', True, 'yellow')
    draw.rect(screen, (0, 0, 0, 0), (270, 135, 540, 270))
    screen.blit(text, ((1080 - text.get_width()) / 2, 160))
    screen.blit(text1, ((1080 - text1.get_width()) / 2, 250))
    screen.blit(text2, ((1080 - text2.get_width()) / 2, 320))
    screen.blit(txt3, ((1080 - txt3.get_width()) / 2, 340))
    if men:
        recording(name, lvl, score)
        mouse.set_visible(True)
        name, lvl, non = menu.menu()
        game()


game()
