import pygame

pygame.init()

screen = pygame.display.set_mode((600, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()