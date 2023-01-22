import pygame.image
from pygame import *
import sys
import Animation as An
import random



init()

size = (892, 504)
screen = display.set_mode(size)
font = font.Font('sprites_Back/Fifaks10Dev1.ttf', 40)
objects = []

try:
    def spisok_pol(rez):
        global p1, p2, p3, p4, p5, p6, p7
        a = random.choices(range(1, 10), k=7)
        p1 = pygame.image.load(f'sprites_Back/Пол{rez}/{a[0]}.png').convert_alpha()
        p2 = pygame.image.load(f'sprites_Back/Пол{rez}/{a[1]}.png').convert_alpha()
        p3 = pygame.image.load(f'sprites_Back/Пол{rez}/{a[2]}.png').convert_alpha()
        p4 = pygame.image.load(f'sprites_Back/Пол{rez}/{a[3]}.png').convert_alpha()
        p5 = pygame.image.load(f'sprites_Back/Пол{rez}/{a[4]}.png').convert_alpha()
        p6 = pygame.image.load(f'sprites_Back/Пол{rez}/{a[5]}.png').convert_alpha()
        p7 = pygame.image.load(f'sprites_Back/Пол{rez}/{a[6]}.png').convert_alpha()
        return p1, p2, p3, p4, p5, p6, p7



    def close_wind():
        pygame.quit()
        sys.exit()


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
            global image1
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
            self.image1 = image1

            screen.blit(image1, (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image1)
            self.rect = self.image1.get_rect()
            self.rect.bottom = (self.y)






    class Mountain(pygame.sprite.Sprite):
        def __init__(self, im, x, y, rez):
            self.im = im
            x = x + 300
            self.y = y
            super().__init__()
            start = pygame.image.load(f'sprites_Back/Пол{rez}/Start.png').convert_alpha()
            end = pygame.image.load(f'sprites_Back/Пол{rez}/End.png').convert_alpha()

            # располагаем горы внизу
            screen.blit(start, (x-1080, 0))
            screen.blit(self.im[0], (x, 0))
            screen.blit(self.im[1], (x + 1080, 0))
            screen.blit(self.im[2], (x + 2160, 0))
            screen.blit(self.im[3], (x + 3240, 0))
            screen.blit(self.im[4], (x + 4320, 0))
            screen.blit(self.im[5], (x + 5400, 0))
            screen.blit(self.im[6], (x + 6480, 0))
            screen.blit(end, (x + 7560, 0))





    def menu():
        global flag1, flag2, cur_frame
        global run, mus
        flag1 = True
        flag2 = True
        menu_bc = pygame.image.load('sprites_Back/fon21.png')
        clock = pygame.time.Clock()
        mus = pygame.mixer.Sound('sprites_Back/Музыка/Меню1.mp3')
        mus.play()

        run = True
        while run:
            for i in event.get():
                if i.type == QUIT:
                    run = False


            screen.blit(menu_bc, (0, 0))
            Button(600, 100, myFunt1, False,'sprites_Back/Играть.png', 'sprites_Back/Играть2.png',
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
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        size = width, height = 1080, 540
        screen = pygame.display.set_mode(size, pygame.NOFRAME | pygame.SCALED)
        clock = pygame.time.Clock()
        mix = pygame.mixer.music
        sounds = pygame.mixer.Sound('data/choi.mp3')
        spr = An.all_sprites

        planet = An.AnimatedSprite(An.load_image('moon.png'), 50, 1, 200, 219)
        lava = An.AnimatedSprite(An.load_image('plnt.png'), 50, 1, 399, 219)
        gas = An.AnimatedSprite(An.load_image('gas2.png'), 50, 1, 490, 119)
        hole = An.AnimatedSprite(An.load_image('star.png'), 50, 1, 700, 119)
        space = pygame.transform.scale(An.load_image('space.png'), (1080, 540))

        pygame.mouse.set_cursor((0, 0), An.load_image('cur.png'))

        push = False
        n = 0
        mix.load('data/space.mp3')
        mix.set_volume(0.09)
        mix.play(-1)

        text = pygame.font.Font(None, 30).render('ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ', True, 'bisque')

        while True:
            screen.blit(space, (0, 0))
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    close_wind()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    push = True

            spr.draw(screen)
            screen.blit(text, (360, 30))

            planet.update()
            lava.update()
            gas.update()
            hole.update()
            n = 0
            for s in spr:
                pos = pygame.mouse.get_pos()
                if s.rect.collidepoint(pos):

                    if 180 < pos[0] < 360:

                        screen.blit(pygame.font.Font(None, 29).render('ЛЕГКО', True, 'green'), (490, 50))
                        pygame.draw.line(screen, 'aquamarine2', (213, 200), (288, 200), 3)
                        pygame.draw.line(screen, 'aquamarine2', (218, 340), (288, 340), 3)
                        screen.blit(pygame.font.Font(None, 22).render('ВЕЛОКИТЕР', True, 'aquamarine2'), (203, 180))
                        screen.blit(pygame.font.Font(None, 22).render('СПУТНИК', True, 'aquamarine2'), (217, 350))
                        if push:
                            sounds.play()
                            n = 1
                            myFunction(1)
                    if 360 < pos[0] < 540:
                        screen.blit(pygame.font.Font(None, 29).render('НОРМАЛЬНО', True, 'yellow'), (465, 50))
                        pygame.draw.line(screen, 'aquamarine2', (412, 200), (488, 200), 3)
                        pygame.draw.line(screen, 'aquamarine2', (412, 340), (488, 340), 3)
                        screen.blit(pygame.font.Font(None, 22).render('ТОППЕР', True, 'aquamarine2'), (419, 180))
                        screen.blit(pygame.font.Font(None, 22).render('ПЛАНЕТА', True, 'aquamarine2'), (416, 350))
                        if push:
                            sounds.play()
                            n = 2
                            myFunction(2)
                    if 540 < pos[0] < 720:
                        screen.blit(pygame.font.Font(None, 29).render('ТРУДНО', True, 'orange'), (485, 50))
                        pygame.draw.line(screen, 'aquamarine2', (613, 200), (669, 200), 3)
                        pygame.draw.line(screen, 'aquamarine2', (613, 340), (669, 340), 3)
                        screen.blit(pygame.font.Font(None, 22).render('ФЕРИТАТИС', True, 'aquamarine2'), (595, 180))
                        screen.blit(pygame.font.Font(None, 22).render('ГАЗОВЫЙ', True, 'aquamarine2'), (603, 350))
                        screen.blit(pygame.font.Font(None, 22).render('ГИГАНТ', True, 'aquamarine2'), (612, 370))
                        if push:
                            sounds.play()
                            n = 3
                            myFunction(3)
                    if 720 < pos[0] < 900:
                        screen.blit(pygame.font.Font(None, 29).render('НЕВОЗМОЖНО', True, 'red1'), (465, 50))
                        pygame.draw.line(screen, 'aquamarine2', (820, 175), (876, 175), 3)
                        pygame.draw.line(screen, 'aquamarine2', (820, 365), (876, 365), 3)
                        screen.blit(pygame.font.Font(None, 22).render('РАПТУС', True, 'aquamarine2'), (817, 155))
                        screen.blit(pygame.font.Font(None, 22).render('ЗВЕЗДА', True, 'aquamarine2'), (817, 375))
                        if push:
                            sounds.play()
                            n = 4
                            myFunction(4)
            if push:
                pygame.time.delay(1000)
                return n
            push = False
            pygame.display.flip()
            clock.tick(15)


    def myFunt():
        global run
        run = False

    def myFunction(rez):
        global flag1
        global flag2, cur_frame, fon
        flag2 = True
        mus.stop()

        mus1 = pygame.mixer.Sound(f'sprites_Back/Музыка/Фон{rez}.mp3')
        mus1.play()
        if flag1:
            flag1 = False
            fon1 = pygame.image.load(f'sprites_Back/fon{rez}.png')
            FPS = 20
            W = 1080  # ширина экрана
            H = 540  # высота экрана


            screen.blit(fon1, (0, 0))
            frames = []
            RIGHT = "to the right"
            LEFT = "to the left"
            RIGHT1 = "to the right1"
            LEFT1 = "to the left1"
            STOP = "stop"

            clock = pygame.time.Clock()
            sc = pygame.display.set_mode((W, H))

            ur = True
            # координаты и радиус круга
            x = W
            y = 0
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
            e = False
            toz = True
            how = False
            while toz:
                fon1 = pygame.image.load(f'sprites_Back/fon{rez}.png')
                y = H / 2 + 100
                screen.blit(fon1, (0, 0))
                ur = True
                x = 0
                a1 = 0
                a2 = 0
                fon = spisok_pol(rez)

                while ur:
                    for i in pygame.event.get():
                        if i.type == pygame.QUIT:
                            sys.exit()

                        elif i.type == pygame.KEYDOWN:
                            if i.key == pygame.K_ESCAPE:
                                if not how:
                                    how = True
                                else:
                                    how = False

                            if i.key == pygame.K_SPACE:
                                if y == 410:
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
                            if i.key == pygame.K_e:
                                if how:
                                    ur = False
                                    toz = False
                                    sc = pygame.display.set_mode((W + 100, H))
                                    mus1.stop()
                                    menu()

                                e = True
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
                                if y > 410:
                                    a1 = 3


                        elif i.type == pygame.KEYUP:
                            m = [pygame.K_LEFT,
                                 pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP,
                                 pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a]
                            if i.key == pygame.K_e:
                                e = False
                            if i.key in [pygame.K_LEFT,
                                         pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP,
                                         pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_a]:
                                a1 = 0
                                motion = STOP

                    fon1 = pygame.image.load(f'sprites_Back/fon{rez}.png')
                    next1 = pygame.image.load(f'sprites_Back/Продолжить.png')

                    screen.blit(fon1, (0, 0))

                    ploz = Mountain(fon, x, 0, rez)
                    if a1 == 0:
                        player = AnimatedSprite("sprites_Back/Ожидание", 100, y - 230, 1, (350, 350))
                    if a1 == 1:
                        player = AnimatedSprite("sprites_Back/БегВправо", 100, y-230, 25, (350, 350))
                    if a1 == 2:
                        player = AnimatedSprite("sprites_Back/БегВправо", 100, y - 230, 25, (350, 350), True)
                    if a1 == 3 and a2 == 0:
                        player = AnimatedSprite("sprites_Back/Прыжок", 100, y - 230, 35, (350, 350))
                    if a1 == 3 and a2 == 2:
                        player = AnimatedSprite("sprites_Back/Прыжок", 100, y - 230, 35, (350, 350), True)

                    #if y >= 410:
                        #y = 410
                        #a = 0

                    if x <= -7700:
                        x = -7700
                        screen.blit(next1, (200, 0))

                    if how:
                        fh = pygame.image.load('sprites_Back/Уверены.png')
                        screen.blit(fh, (300, -200))



                    pygame.display.update()

                    #if not prig:
                        #if y <= 350:
                            #prig = True
                        #y -= 10 - (0.5 ** a)

                    #if y < 410 and prig:
                        #y += 1 + (1.1 ** a)
                        #a += 1
                        #if y >= 405:
                            #a1 = 0

                    if x <= -7700 and e:
                        ur = False

                    if x <= -7700:
                        x = -7700
                        screen.blit(next1, (100, 300))

                    if x > 0:
                        x = 0

                    if motion == LEFT:
                        a1 = 1
                        x += 20
                    elif motion == RIGHT:
                        a1 = 2
                        x -= 20
                    elif motion == RIGHT1:
                        if y <= 410:
                            y += 3
                    elif motion == LEFT1:
                        y -= 3


                    clock.tick(FPS)

            clock.tick(FPS)
    menu()

    quit()
except FileExistsError:
    pass



