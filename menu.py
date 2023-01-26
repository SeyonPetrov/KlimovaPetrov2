import pygame.image
from pygame import *
import sys
import layers_planets as lp
import recording as rec
import rocket as rok
import recorders as champ

mixer.pre_init(44100, -16, 1, 512)
init()

size = (1080, 540)
screen = display.set_mode(size, pygame.NOFRAME)
font = font.Font('sprites_Back/Fifaks10Dev1.ttf', 40)
objects = []


class Button:
    def __init__(self, x, y, onclick_function=None, one_press=False, norm='', hov='', spr=''):

        self.x = x
        self.y = y
        self.onclickFunction = onclick_function
        self.onePress = one_press
        self.alreadyPressed = False
        self.fillColors = {
            'normal': norm,
            'hover': hov,
            'pressed': spr,
        }
        self.buttonSurface = pygame.Surface((259, 71))
        self.buttonRect = pygame.Rect(self.x, self.y, 259, 71)
        self.buttonSurf = font.render('', True, (20, 20, 20))

        objects.append(self)

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        menu_bc1 = pygame.image.load(self.fillColors['normal'])

        if self.buttonRect.collidepoint(mouse_pos):
            menu_bc1 = pygame.image.load(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                menu_bc1 = pygame.image.load(self.fillColors['pressed'])
                if self.onePress:

                    return self.onclickFunction()
                elif not self.alreadyPressed:

                    self.alreadyPressed = True
                    return self.onclickFunction()
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(menu_bc1, (self.x, self.y))


def load_image(name):
    im = pygame.image.load(name)
    return im


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, namep, x, y, kol_vo, isk, otr=False):
        global flag2, cur_frame
        super().__init__()
        self.namep = namep
        self.x = x
        self.y = y
        self.kol_vo = kol_vo
        if flag2:
            flag2 = False
            cur_frame = 0
        if cur_frame < self.kol_vo:
            cur_frame += 1
        else:
            cur_frame = 1
        self.frames = load_image(f'{namep}/{cur_frame}.png')
        image1 = pygame.transform.scale(self.frames, isk)
        if otr:
            image1 = pygame.transform.flip(image1, True, False)
        screen.blit(image1, (self.x, self.y))


def menu():
    global flag1, flag2, cur_frame
    global run, mus
    flag1 = True
    flag2 = True
    menu_bc = pygame.image.load('sprites_Back/fon21.png')
    menu_bc = pygame.transform.scale(menu_bc, (1080, 540))
    clock = pygame.time.Clock()
    mus = pygame.mixer.music
    mus.load('data/space.mp3')
    mus.set_volume(0.09)
    mus.play(-1)
    pygame.mouse.set_cursor((0, 0), pygame.image.load('data/cur.png'))

    while True:
        for i in event.get():
            if i.type == pygame.KEYDOWN and i.key == K_ESCAPE:
                my_funt()

        screen.blit(menu_bc, (0, 0))
        Button(410, 100, start_layers, False,'sprites_Back/Играть.png', 'sprites_Back/Играть2.png',
               'sprites_Back/Играть1.png')
        Button(410, 300, my_funt, False, 'sprites_Back/Выход.png', 'sprites_Back/Выход1.png',
               'sprites_Back/Выход.png')
        Button(410, 200, recorders, False, 'sprites_Back/успехи.png', 'sprites_Back/успехи2.png',
               'sprites_Back/успехи.png')
        AnimatedSprite("sprites_Back/Moon", 800, 320, 60, (180, 180))

        for obj in objects:
            n = obj.process()
            if n:
                return n
        display.update()
        clock.tick(20)


def start_layers():
    mus.stop()
    return my_funt(True)


def recorders():
    champ.champs()


def my_funt(from_layers=False):
    if from_layers:
        name = rec.record()
    else:
        pygame.quit()
        sys.exit()
    if name:
        return name, lp.difficulty_levels(), rok.rocket()



