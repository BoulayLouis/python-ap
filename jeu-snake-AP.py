import pygame

pygame.init()

screen = pygame.display.set_mode( (400, 300) )

clock = pygame.time.Clock()

noir,vert=(0,0,0),(0,255,0)
hauteur,largeur=300,400
frame=20
a,b,c=5,6,7
d,e,f=10,10,10


while True:

    clock.tick(frame)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.QUIT()
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame.QUIT()
            pygame.quit()

    screen.fill( (255, 255, 255) )       
    for k in range(0,largeur,40):
        for i in range (0,hauteur,40):
            rect = pygame.Rect(k,i, 20, 20)
            rect2 = pygame.Rect(k+20,i+20, 20, 20)
            pygame.draw.rect(screen, noir, rect)
            pygame.draw.rect(screen, noir, rect2)

    serpent1=pygame.Rect(a*20,d*20,20,20)
    serpent2=pygame.Rect(b*20,e*20,20,20)
    serpent3=pygame.Rect(c*20,f*20,20,20)
    pygame.draw.rect(screen, vert, serpent1)
    pygame.draw.rect(screen, vert, serpent2)
    pygame.draw.rect(screen, vert, serpent3)

    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                f=e
                e=d
                d-=1
                serpent1=pygame.Rect(a*20,d*20,20,20)
                serpent2=pygame.Rect(b*20,e*20,20,20)
                serpent3=pygame.Rect(c*20,f*20,20,20)
                pygame.draw.rect(screen, vert, serpent1)
                pygame.draw.rect(screen, vert, serpent2)
                pygame.draw.rect(screen, vert, serpent3)
            if event.key == pygame.K_DOWN:
                f=e
                e=d
                d+=1
                serpent1=pygame.Rect(a*20,d*20,20,20)
                serpent2=pygame.Rect(b*20,e*20,20,20)
                serpent1=pygame.Rect(c*20,f*20,20,20)
                pygame.draw.rect(screen, vert, serpent1)
                pygame.draw.rect(screen, vert, serpent2)
                pygame.draw.rect(screen, vert, serpent3)
            if event.key == pygame.K_RIGHT:
                c=b
                b=a
                a+=1
                serpent1=pygame.Rect(a*20,d*20,20,20)
                serpent2=pygame.Rect(b*20,e*20,20,20)
                serpent1=pygame.Rect(c*20,f*20,20,20)
                pygame.draw.rect(screen, vert, serpent1)
                pygame.draw.rect(screen, vert, serpent2)
                pygame.draw.rect(screen, vert, serpent3)
            if event.key == pygame.K_LEFT:
                c=b
                b=a
                a-=1
                serpent1=pygame.Rect(a*20,d*20,20,20)
                serpent2=pygame.Rect(b*20,e*20,20,20)
                serpent1=pygame.Rect(c*20,f*20,20,20)
                pygame.draw.rect(screen, vert, serpent1)
                pygame.draw.rect(screen, vert, serpent2)
                pygame.draw.rect(screen, vert, serpent3)



    pygame.display.update()
