import pygame

height = 500
width = 600
bgcolor = (200,255,255)
window = pygame.display.set_mode((width, height))
window.fill(bgcolor)
clock = pygame.time.Clock()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(60)