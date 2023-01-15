import pygame.image
from pygame import *
import sys

init()

size = (960, 540)
screen = display.set_mode(size)
font = font.Font('sprites_Back/Fifaks10Dev1.ttf', 40)
objects = []





class Button():
    def __init__(self, x, y, onclickFunction=None, onePress=False, norm='', hov='', spr=''):

        self.x = x
        self.y = y
        self.onclickFunction = onclickFunction
        self.onePress = onePress
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
        mousePos = pygame.mouse.get_pos()
        menu_bc1 = pygame.image.load(self.fillColors['normal'])

        if self.buttonRect.collidepoint(mousePos):
            menu_bc1 = pygame.image.load(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                menu_bc1 = pygame.image.load(self.fillColors['pressed'])
                if self.onePress:

                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(menu_bc1, (self.x, self.y))

def load_image(name, colorkey=None):
    image = pygame.image.load(name)
    return image



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
    menu_bc = pygame.image.load('sprites_Back/fon2.png')
    clock = pygame.time.Clock()
    mus = pygame.mixer.Sound('sprites_Back/Музыка/Меню.mp3')
    #mus.play()

    run = True
    while run:
        for i in event.get():
            if i.type == QUIT:
                run = False


        screen.blit(menu_bc, (0, 0))
        Button(600, 100, myFunction, False,'sprites_Back/Играть.png', 'sprites_Back/Играть2.png',
               'sprites_Back/Играть1.png')
        Button(600, 200, myFunt, False, 'sprites_Back/Выход.png', 'sprites_Back/Выход1.png',
               'sprites_Back/Выход.png')
        AnimatedSprite("sprites_Back/Moon", 635, 290, 60, (180, 180))

        for object in objects:
            object.process()
        display.update()
    clock.tick(20)
    quit()

def myFunt1():
    global run
    run = False

def myFunt():
    global run
    run = False

def myFunction():
    global flag1
    global flag2, cur_frame
    flag2 = True
    #mus.stop()
    mus1 = pygame.mixer.Sound('sprites_Back/Музыка/Шапка.mp3')
    mus1.play()
    if flag1:
        flag1 = False
        print('Button Pressed')
        fon = pygame.image.load('sprites_Back/fon1.png')
        FPS = 20
        W = 811  # ширина экрана
        H = 521  # высота экрана
        screen.blit(fon, (0, 0))
        frames = []
        RIGHT = "to the right"
        LEFT = "to the left"
        RIGHT1 = "to the right1"
        LEFT1 = "to the left1"
        STOP = "stop"

        clock = pygame.time.Clock()
        sc = pygame.display.set_mode((W, H))


        # координаты и радиус круга
        x = W
        y = H // 2
        r = 50
        jumpCount = 10
        isJump = False
        motion = STOP
        zaderzh = 0
        a = 0
        x = 0
        a1 = 0
        a2 = 0
        prig = True

        while 1:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()

                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_SPACE:
                        if y == 430:
                            prig = False
                            a1 = 3
                    if i.key == pygame.K_LEFT:
                        motion = LEFT
                        a2 = 0
                        a1 = 1
                    if i.key == pygame.K_RIGHT:
                        motion = RIGHT
                        a2 = 2
                        a1 = 2
                    if i.key == pygame.K_DOWN:
                        motion = RIGHT1
                    if i.key == pygame.K_UP:
                        motion = LEFT1
                    if i.key == pygame.K_a:
                        motion = LEFT
                        a2 = 0
                        a1 = 1
                    if i.key == pygame.K_d:
                        motion = RIGHT
                        a2 = 2
                        a1 = 2
                    if i.key == pygame.K_s:
                        motion = RIGHT1
                    if i.key == pygame.K_w:
                        motion = LEFT1
                    if i.key == pygame.K_SPACE:
                        if y > 430:
                            a1 = 3


                elif i.type == pygame.KEYUP:
                    m = [pygame.K_LEFT,
                         pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP,
                         pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a]
                    if i.key in [pygame.K_LEFT,
                                 pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP,
                                 pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a]:
                        a1 = 0
                        motion = STOP

            if y >= 430:
                y = 430
                a = 0

            fon = pygame.image.load('sprites_Back/fon1.png')
            screen.blit(fon, (x, 0))
            screen.blit(fon, (x + 811, 0))
            if a1 == 0:
                AnimatedSprite("sprites_Back/Ожидание", 400, y - 230, 1, (350, 350))
            if a1 == 1:
                AnimatedSprite("sprites_Back/БегВправо", 400, y-230, 25, (350, 350))
            if a1 == 2:
                AnimatedSprite("sprites_Back/БегВправо", 400, y - 230, 25, (350, 350), True)
            if a1 == 3 and a2 == 0:
                AnimatedSprite("sprites_Back/Прыжок", 400, y - 230, 35, (350, 350))
            if a1 == 3 and a2 == 2:
                AnimatedSprite("sprites_Back/Прыжок", 400, y - 230, 35, (350, 350), True)

            pygame.display.update()

            if not prig:
                if y <= 350:
                    prig = True
                y -= 10 - (0.5 ** a)

            if y < 430 and prig:
                y += 1 + (1.1 ** a)
                a += 1
                if y >= 425:
                    a1 = 0

            if y >= 430:
                y = 430

            if x <= -811:
                x = 0
            if x >= 406:
                x = 406

            if motion == LEFT:
                a1 = 1
                x += 3
            elif motion == RIGHT:
                a1 = 2
                x -= 3
            elif motion == RIGHT1:
                if y <= 430:
                    y += 3
            elif motion == LEFT1:
                y -= 3

            clock.tick(FPS)

menu()




