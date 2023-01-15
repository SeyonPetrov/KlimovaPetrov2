import pygame
import os
import Animation as An

pygame.init()
screen = pygame.display.set_mode((600, 400), pygame.NOFRAME)
pygame.display.set_caption("Свой курсор мыши")

im = pygame.image.load(os.path.join('data', 'arrow1.png'))  # загружаем изображение
spr = pygame.sprite.Group()


class Curr(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(spr)
        self.image = im
        self.rect = self.image.get_rect()


scrn = pygame.Surface((50, 50))
t = Curr()
scrn.blit(im, (0, 0))
cur = pygame.cursors.Cursor((0, 0), scrn)  # создаем курсор из нашего холста
pygame.mouse.set_cursor((0, 0), An.load_image('arrow.png'))  # устанавливаем созданный курсор
hero = An.AnimatedSprite(An.load_image('hole.png'), 50, 1, 100, 50)
clock = pygame.time.Clock()
go = True
while go:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            go = False
    An.all_sprites.draw(screen)
    hero.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()