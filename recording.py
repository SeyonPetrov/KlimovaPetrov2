import pygame
import pygame_gui
import sys
import os


def load_image(name):
    fullname = os.path.join('sprites_Back', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def record():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    mix = pygame.mixer.music
    size = width, height = 1080, 540
    fon = pygame.transform.scale(load_image('fon31.png'), (1080, 540))
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    clock = pygame.time.Clock()
    font = pygame.font.Font('sprites_Back/Fifaks10Dev1.ttf', 40).render('Как вас зовут?', True, (106, 240, 249))
    pygame.mouse.set_cursor((0, 0), pygame.image.load('data/cur.png'))

    manag = pygame_gui.UIManager((1080, 540), 'data/theme_for_buttons.json')
    manag.add_font_paths('Faks', 'sprites_Back/Fifaks10Dev1.ttf')
    manag.preload_fonts([{
        'name': 'Faks',
        'html_size': 4,
        'style': 'regular'
    }])
    line_edit = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(290, 162, 500, 50),
        manager=manag, object_id='line'
    )
    button_1 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(415, 340, 250, 50),
        text='ВЫЙТИ',
        manager=manag,
        object_id='button1'
    )
    button_2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(415, 280, 250, 50),
        text='В ГЛАВНОЕ МЕНЮ',
        manager=manag,
        object_id='button2'
    )
    button_3 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(415, 220, 250, 50),
        text='ВЫБРАТЬ СЛОЖНОСТЬ',
        manager=manag,
        object_id='button3'
    )
    fontt = pygame.font.Font('sprites_Back/Fifaks10Dev1.ttf', 40)
    text = fontt.render('ВВЕДИТЕ СВОЕ ИМЯ', True, 'red')
    no_name = False
    run = True
    mix.load('data/space.mp3')
    mix.set_volume(0.09)
    mix.play(-1)
    while run:
        t_delta = clock.tick(60) / 1000.0
        screen.blit(fon, (0, 0))
        screen.blit(font, (410, 100))
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                close()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                print(line_edit.get_text())

            if button_1.check_pressed():
                close()

            if button_2.check_pressed():
                return None

            if button_3.check_pressed():
                if not line_edit.get_text():
                    no_name = True
                else:
                    return line_edit.get_text()

            manag.process_events(e)
        if no_name:
            screen.blit(text, (380, 450))
        manag.update(t_delta)
        manag.draw_ui(screen)
        pygame.display.flip()


def close():
    pygame.quit()
    sys.exit()

