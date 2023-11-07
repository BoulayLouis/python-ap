import pygame

pygame.init()

screen = pygame.display.set_mode( (400, 300) )

clock = pygame.time.Clock()

noir,vert=(0,0,0),(0,255,0)
hauteur,largeur=300,400
frame=20


while True:

    clock.tick(frame)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.QUIT()
        if event.type == pygame.QUIT:
            pygame.QUIT()

    screen.fill( (255, 255, 255) )

    pygame.display.update()