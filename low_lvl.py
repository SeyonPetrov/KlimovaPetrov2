import pygame


def sl():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), pygame.NOFRAME)
    clock = pygame.time.Clock()
    run = True
    r, g, b = 0, 0, 0
    while run:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                run = False
        pygame.draw.rect(screen, (r, g, b), (10, 10, 300, 300))
        if r < 245 and g < 245 and b < 245:
            r += 10
            g += 10
            b += 10
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()


sl()