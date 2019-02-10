import pygame

pygame.init()
pygame.display.set_caption('Drawing example')

screen_size = [600, 480]
screen = pygame.display.set_mode(screen_size)
screen.fill([249, 251, 255])

clock = pygame.time.Clock()
exit = False
while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.draw.polygon(screen, [0, 255, 0], [[100, 100], [0, 200], [200, 200]], 0)
    pygame.draw.polygon(screen, [255, 98, 84], [[100, 100], [0, 200], [200, 200]], 0)

    pygame.display.flip()

pygame.quit()
