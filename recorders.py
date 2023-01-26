from pygame import *
import sqlite3


def champs():
    init()
    screen = display.set_mode((1080, 540), NOFRAME)
    clock = time.Clock()
    shrft = 'sprites_Back/Fifaks10Dev1.ttf'
    im = image.load('data/космо.png')
    im1 = transform.scale(im, (1080, 540))
    pod = sqlite3.connect('рекорды.sqlite3')
    cu = pod.cursor()
    data = sorted(cu.execute('select * from record').fetchall(), key=lambda x: x[-1])[::-1]
    text = font.Font(shrft, 30).render('ИМЯ', True, (106, 240, 249))
    text1 = font.Font(shrft, 30).render('УРОВЕНЬ', True, (106, 240, 249))
    text2 = font.Font(shrft, 30).render('СЧЕТ', True, (106, 240, 249))
    if data:
        name1 = font.Font(shrft, 40).render(data[0][1], True, 'gold')
        lev = font.Font(shrft, 40).render(str(data[0][2]), True, 'gold')
        score = font.Font(shrft, 40).render(str(data[0][3]), True, 'gold')
    else:
        name1 = ''
        lev = ''
        score = ''
    if len(data) >= 2:
        name2 = font.Font(shrft, 40).render(data[1][1], True, 'greenyellow')
        lev2 = font.Font(shrft, 40).render(str(data[1][2]), True, 'greenyellow')
        score2 = font.Font(shrft, 40).render(str(data[1][3]), True, 'greenyellow')
    else:
        name2 = ''
        lev2 = ''
        score2 = ''
    if len(data) >= 3:
        name3 = font.Font(shrft, 40).render(data[2][1], True, 'greenyellow')
        lev3 = font.Font(shrft, 40).render(str(data[2][2]), True, 'greenyellow')
        score3 = font.Font(shrft, 40).render(str(data[2][3]), True, 'greenyellow')
    else:
        name3 = ''
        lev3 = ''
        score3 = ''

    exit_menu = font.Font(shrft, 20).render('НАЖМИТЕ "SPACE", ЧТОБЫ ВЕРНУТЬСЯ В МЕНЮ', True, 'green')

    while True:
        screen.blit(im1, (0, 0))
        for e in event.get():
            if e.type == KEYDOWN and e.key == K_SPACE:
                return None
        screen.blit(text, (340, 20))
        screen.blit(text1, (470, 20))
        screen.blit(text2, (670, 20))

        screen.blit(name1, (330, 150))
        screen.blit(name2, (330, 250))
        screen.blit(name3, (330, 350))
        screen.blit(lev, (520, 150))
        screen.blit(lev2, (520, 250))
        screen.blit(lev3, (520, 350))
        screen.blit(score, (680, 150))
        screen.blit(score2, (680, 250))
        screen.blit(score3, (680, 350))

        screen.blit(exit_menu, ((1080 - exit_menu.get_width()) // 2, 500))
        display.flip()
        clock.tick(15)
