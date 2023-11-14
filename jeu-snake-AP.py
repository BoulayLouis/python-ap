import pygame
import random as rd
import argparse



pygame.init()

clock = pygame.time.Clock()

#Constantes
NOIR,VERT,ROUGE,BLANC=(0,0,0),(0,255,0),(255,0,0),(255,255,255)
HAUTEUR,LARGEUR=300,400
CASE=20
FRAME=5
COL=[5,6,7]
LIGNE=[10,10,10]
TAILLE=3
NOURRITURE1=(3*CASE,3*CASE)     
NOURRITURE2=(15*CASE,10*CASE)

#Variables
n=1         
score=0
direction=(1,0) 


# Lignes de commandes
parser = argparse.ArgumentParser(description='Some description.')
parser.add_argument('--bg-color-1',default= NOIR ,help="Prend une couleur")
parser.add_argument('--bg-color-2', default=BLANC ,help="Prend une couleur")
parser.add_argument('--height', default=HAUTEUR,help="Prend la hauteur de la fenêtre")
parser.add_argument('--width', default=LARGEUR,help="Prend la largeur de la fenêtre")
parser.add_argument('--fps', default=FRAME,help="Prend le nombre d'images par secondes")
parser.add_argument('--fruit-color', default=ROUGE, help="Prend une couleur pour le fruit")
parser.add_argument('--snake-color', default=VERT, help="Prend une couleur pour le serpent")
parser.add_argument('--snake-length', default=TAILLE,help="Prend un entier pour la longueur du serpent")
parser.add_argument('--tile-size', default= CASE,help="Prend un entier pour la taille des cases")
parser.add_argument('--gameover-on-exit',help="Un flag",action='store_false')
args = parser.parse_args()


#Conditions d'erreurs
if args.fruit_color==args.bg_color_1 or args.fruit_color==args.bg_color_2:
    raise ValueError("Le fruit ne peut pas avoir la même couleur que le fond")
if args.snake_color==args.bg_color_1 or args.snake_color==args.bg_color_2:
    raise ValueError("Le serpent ne peut pas avoir la même couleur que le fond")
if int(args.snake_length)<2 :
    raise ValueError("Le serpent ne peut pas avoir une longueur inférieure à 2")
if int(args.height)%int(args.tile_size)!=0:
    raise ValueError("La hauteur du cadre doit être un multiple de la taille des cases")
if int(args.width)%int(args.tile_size)!=0:
    raise ValueError("La largeur du cadre doit être un multiple de la taille des cases")
if int(args.height)<12 or int(args.width)<20:
    raise ValueError("Il doit y avoir au minimum 12 lignes et 20 colonnes")
if int(args.width)<NOURRITURE2[1] or int(args.height)<NOURRITURE2[0]:
    raise ValueError("le deuxième fruit n'est pas sur l'écran")


#Création de l'écran
screen = pygame.display.set_mode( (int(args.width), int(args.height)) )


#On initialise le serpent
serpent=[]    
for k in range (int(args.snake_length)):
    serpent.append((COL[k]*int(args.tile_size),LIGNE[k]*int(args.tile_size)))


while True:
    
    

    clock.tick(args.fps)

    # Changement direction serpent
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # on quitte le programme si la touvche Q est préssée
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

    #Changement du serpent
    tete_x, tete_y = serpent[0]         
    nouvelle_tete = (tete_x + direction[0] * int(args.tile_size), tete_y + direction[1] * int(args.tile_size))
    (new_tete_x,new_tete_y)=nouvelle_tete
    

    #Vérification de la position du serpent
    if args.gameover_on_exit==False:
        if new_tete_x<0 or new_tete_x>int(args.width):
            pygame.quit()
        elif new_tete_y<0 or new_tete_y>int(args.height):
            pygame.quit()
    else:
        if new_tete_x<0:
            new_tete_x=int(args.width)+new_tete_x
        elif new_tete_x>int(args.width):
            new_tete_x=new_tete_x-int(args.width)-args.tile_size
        elif new_tete_y<0:
            new_tete_x=int(args.height)+new_tete_y
        elif new_tete_y>int(args.height):
            new_tete_y=new_tete_y-int(args.height)-args.tile_size

    serpent.insert(0, (new_tete_x,new_tete_y))
       

    #Effet de la nourriture 
    if serpent[0]!=NOURRITURE1 and n==1:    
        serpent.pop()                       
    elif serpent[0]!=NOURRITURE2 and n==2:  
        serpent.pop()                       
    elif serpent[0]==NOURRITURE2 and n==2:  
        n=1                                 
        score+=1                            
    elif serpent[0]==NOURRITURE1 and n==1:  
        n=2                                 
        score+=1           

    #Affichage de l'écran                 
    screen.fill( args.bg_color_2 )          
    for k in range(0,int(args.width),2*int(args.tile_size)):       
        for i in range (0,int(args.height),2*int(args.tile_size)):
            rect = pygame.Rect(k,i, int(args.tile_size), int(args.tile_size))
            rect2 = pygame.Rect(k+int(args.tile_size),i+int(args.tile_size), int(args.tile_size), int(args.tile_size))
            pygame.draw.rect(screen, args.bg_color_1, rect)
            pygame.draw.rect(screen, args.bg_color_1, rect2)
    
    #Affichage du serpent, des fruits et du score
    for position in serpent:                   
        pygame.draw.rect(screen, args.snake_color, (position[0], position[1], int(args.tile_size), int(args.tile_size)))
    if n==1:                                    
        pygame.draw.rect(screen, args.fruit_color, (NOURRITURE1[0], NOURRITURE1[1], int(args.tile_size), int(args.tile_size)))
    else:                                       
        pygame.draw.rect(screen, args.fruit_color, (NOURRITURE2[0], NOURRITURE2[1], int(args.tile_size), int(args.tile_size)))
    pygame.display.set_caption(f"Snake - Score : {score}")  
    pygame.display.update()
