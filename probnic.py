import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size, pygame.NOFRAME)
clock = pygame.time.Clock()


def fly(scrn, pos):
    n, m = pos
    r = 1
    for i in range(10000):
        pygame.draw.circle(scrn, 'cadetblue1', (n, m), r)
        r += 100 * clock.tick() / 100


x, y = 499, 499
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            fly(screen, pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(15)
pygame.quit()