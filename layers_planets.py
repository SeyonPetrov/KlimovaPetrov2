import pygame
import sys
import Animation as An


def close_wind():
    pygame.quit()
    sys.exit()


def difficulty_levels():
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
                if 360 < pos[0] < 540:
                    screen.blit(pygame.font.Font(None, 29).render('НОРМАЛЬНО', True, 'yellow'), (465, 50))
                    pygame.draw.line(screen, 'aquamarine2', (412, 200), (488, 200), 3)
                    pygame.draw.line(screen, 'aquamarine2', (412, 340), (488, 340), 3)
                    screen.blit(pygame.font.Font(None, 22).render('ТОППЕР', True, 'aquamarine2'), (419, 180))
                    screen.blit(pygame.font.Font(None, 22).render('ПЛАНЕТА', True, 'aquamarine2'), (416, 350))
                    if push:
                        sounds.play()
                        n = 2
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
                if 720 < pos[0] < 900:
                    screen.blit(pygame.font.Font(None, 29).render('НЕВОЗМОЖНО', True, 'red1'), (465, 50))
                    pygame.draw.line(screen, 'aquamarine2', (820, 175), (876, 175), 3)
                    pygame.draw.line(screen, 'aquamarine2', (820, 365), (876, 365), 3)
                    screen.blit(pygame.font.Font(None, 22).render('РАПТУС', True, 'aquamarine2'), (817, 155))
                    screen.blit(pygame.font.Font(None, 22).render('ЗВЕЗДА', True, 'aquamarine2'), (817, 375))
                    if push:
                        sounds.play()
                        n = 4
        if push:
            pygame.time.delay(1000)
            return n
        push = False
        pygame.display.flip()
        clock.tick(15)


print(difficulty_levels())

