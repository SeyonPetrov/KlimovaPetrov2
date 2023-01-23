import pygame
import sys
import random
import os


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert_alpha()
    return image


def rocket():
    clock = pygame.time.Clock()
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    mix = pygame.mixer.music
    mix.load('data/roket.mp3')
    mix.set_volume(0.09)
    mix.play(-1)
    pygame.display.set_caption('game base')
    screen = pygame.display.set_mode((1080, 540), pygame.NOFRAME)

    class Rock(pygame.sprite.Sprite):
        def __init__(self, n, m):
            super().__init__(group)
            self.image = jet
            self.rect = self.image.get_rect().move(n, m)

        def update(self):
            self.rect.y -= 10

    jet = load_image('rocket1.png').convert_alpha()
    particles = []
    x = 440
    y = 600
    group = pygame.sprite.Group()
    spr_jet = Rock(x, y)

    while True:

        screen.blit(pygame.transform.scale(load_image('sky.png'), (1080, 540)), (0, 0))
        mx, my = spr_jet.rect.x + 100, spr_jet.rect.y + 170
        particles.append([[mx, my], [random.randint(0, 50) / 10 - 1, -2], random.randint(10, 15)])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            color = (210, random.randint(0, 100), random.randint(0, 100))
            pygame.draw.circle(screen, color, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        group.draw(screen)
        spr_jet.update()
        if spr_jet.rect.y <= -400:
            mix.stop()
            return None
        pygame.display.flip()
        clock.tick(30)