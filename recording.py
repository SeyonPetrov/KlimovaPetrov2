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
    pygame.init()
    size = width, height = 1080, 540
    fon = pygame.transform.scale(load_image('fon2.png'), (1080, 540))
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
        relative_rect=pygame.Rect(415, 220, 250, 50),
        text='далее',
        manager=manag,
        object_id='button1'
    )
    button_2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(415, 280, 250, 50),
        text='В главное меню',
        manager=manag,
        object_id='button2'
    )
    pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(415, 340, 250, 50),
        text='Выбрать сложность',
        manager=manag,
        object_id='button3'
    )

    while True:
        t_delta = clock.tick(60) / 1000.0
        screen.blit(fon, (0, 0))
        screen.blit(font, (410, 100))
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                close()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                print(line_edit.get_text())

            manag.process_events(e)
        manag.update(t_delta)
        manag.draw_ui(screen)
        pygame.display.flip()


def close():
    pygame.quit()
    sys.exit()


record()