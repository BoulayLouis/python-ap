import pygame
import random as rd

pygame.init()

screen = pygame.display.set_mode( (400, 300) )

clock = pygame.time.Clock()

noir,vert,rouge=(0,0,0),(0,255,0),(255,0,0)
hauteur,largeur=300,400
case=20
frame=5
col=[5,6,7]
ligne=[10,10,10]
serpent=[]
serpent.append((col[0]*case,ligne[0]*case))
serpent.append((col[1]*case,ligne[1]*case))
serpent.append((col[2]*case,ligne[2]*case))
direction=(1,0)
nourriture1=(3*case,3*case)
nourriture2=(15*case,10*case)
n=1


while True:
    
    

    clock.tick(frame)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.QUIT()
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
    tete_x, tete_y = serpent[0]
    nouvelle_tete = (tete_x + direction[0] * case, tete_y + direction[1] * case)
    serpent.insert(0, nouvelle_tete)
    if serpent[0]!=nourriture1 and n==1:
        serpent.pop()
    elif serpent[0]!=nourriture2 and n==2:
        serpent.pop()
    elif serpent[0]==nourriture2 and n==2:
        n=1
    elif serpent[0]==nourriture1 and n==1:
        n=2
    screen.fill( (255, 255, 255) ) 
    for k in range(0,largeur,2*case):
        for i in range (0,hauteur,2*case):
            rect = pygame.Rect(k,i, case, case)
            rect2 = pygame.Rect(k+case,i+case, case, case)
            pygame.draw.rect(screen, noir, rect)
            pygame.draw.rect(screen, noir, rect2)
    for position in serpent:
        pygame.draw.rect(screen, vert, (position[0], position[1], case, case))
    if n==1:
        pygame.draw.rect(screen, rouge, (nourriture1[0], nourriture1[1], case, case))
    else:
        pygame.draw.rect(screen, rouge, (nourriture2[0], nourriture2[1], case, case))
    pygame.display.update()
