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
serpent=[]    #On initialise le serpent
serpent.append((col[0]*case,ligne[0]*case))
serpent.append((col[1]*case,ligne[1]*case))
serpent.append((col[2]*case,ligne[2]*case))
direction=(1,0) #On initialise la direction qu'il va suivre
nourriture1=(3*case,3*case)     #on crée les deux positions possibles pour la nourriture
nourriture2=(15*case,10*case)
n=1         #on indique la nourriture avec laquelle on va commencer
score=0


while True:
    
    

    clock.tick(frame)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # on quitte le programme si la touvche Q est préssée
                pygame.QUIT()
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):  #On change la direction si la touche UP est préssée et qu'on ne va pas déjà vers le bas (pour éviter les demi-tours)
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):   #De même pour la touche DOWN
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):    #De même pour la touche LEFT
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):  #De même pour la touche RIGHT
                    direction = (1, 0)
    tete_x, tete_y = serpent[0]         #on crée la nouvelle tête quand le serpent se déplace
    nouvelle_tete = (tete_x + direction[0] * case, tete_y + direction[1] * case)
    serpent.insert(0, nouvelle_tete)    
    if serpent[0]!=nourriture1 and n==1:    #Si la tête du serpent ne se trouve pas sur la nourriture 1 et qu'elle est affichée
        serpent.pop()                       #Le serpent reste de même longueur
    elif serpent[0]!=nourriture2 and n==2:  #Si la tête du serpent ne se trouve pas sur la nourriture 2 et qu'elle est affichée
        serpent.pop()                       #Le serpent reste de même longueur
    elif serpent[0]==nourriture2 and n==2:  #Si la tête du serpent se trouve sur la nourriture 2 et qu'elle est affichée
        n=1                                 #Le serpent s'allonge d'une case et on change de nourriture à afficher
        score+=1                            #On augmente le score de 1
    elif serpent[0]==nourriture1 and n==1:  #Si la tête du serpent se trouve sur la nourriture 1 et qu'elle est affichée
        n=2                                 #Le serpent s'allonge d'une case et on change de nourriture à afficher
        score+=1                            #On augmente le score de 1
    screen.fill( (255, 255, 255) )          #On affiche un écran blanc
    for k in range(0,largeur,2*case):       #On va afficher le cadrillage noir
        for i in range (0,hauteur,2*case):
            rect = pygame.Rect(k,i, case, case)
            rect2 = pygame.Rect(k+case,i+case, case, case)
            pygame.draw.rect(screen, noir, rect)
            pygame.draw.rect(screen, noir, rect2)
    for position in serpent:                   #on affiche le serpent
        pygame.draw.rect(screen, vert, (position[0], position[1], case, case))
    if n==1:                                    #Si on doit afficher la nourriture 1, on l'affiche
        pygame.draw.rect(screen, rouge, (nourriture1[0], nourriture1[1], case, case))
    else:                                       #Sinon on doit afficher la nourriture 2, on l'affiche
        pygame.draw.rect(screen, rouge, (nourriture2[0], nourriture2[1], case, case))
    pygame.display.set_caption(f"Snake - Score : {score}")  #On affiche le score
    pygame.display.update()
