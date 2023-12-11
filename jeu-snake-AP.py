import pygame
import random as rd
import argparse
import logging
import sys



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



#  fonction pour lignes de commandes et conditions d'erreurs
def read_args():
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
    parser.add_argument('--debug',help="Utile pour le debug")
    args = parser.parse_args()
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
    return args

def get_score():
    return len(serpent)-3

def process_events(direction):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP and direction != (0, 1):  
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):   
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):    
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):  
                direction = (1, 0)
    return direction
                
def draw_checkerboard(screen,args):
    screen.fill( args.bg_color_2 )          
    for k in range(0,int(args.width),2*int(args.tile_size)):       
        for i in range (0,int(args.height),2*int(args.tile_size)):
            rect = pygame.Rect(k,i, int(args.tile_size), int(args.tile_size))
            rect2 = pygame.Rect(k+int(args.tile_size),i+int(args.tile_size), int(args.tile_size), int(args.tile_size))
            pygame.draw.rect(screen, args.bg_color_1, rect)
            pygame.draw.rect(screen, args.bg_color_1, rect2)

def draw_fruit(screen, fruit_position, args):
    if n==1:                                    
        pygame.draw.rect(screen, args.fruit_color, (NOURRITURE1[0], NOURRITURE1[1], int(args.tile_size), int(args.tile_size)))
    else:                                       
        pygame.draw.rect(screen, args.fruit_color, (NOURRITURE2[0], NOURRITURE2[1], int(args.tile_size), int(args.tile_size)))

def draw_snake(screen, snake_positions, args):
    for position in serpent:                   
        pygame.draw.rect(screen, args.snake_color, (position[0], position[1], int(args.tile_size), int(args.tile_size)))

def draw(screen, serpent, n, args):
    draw_checkerboard(screen, args)
    draw_fruit(screen, n, args)
    draw_snake(screen, serpent, args)

def update_display(screen, score):
    pygame.display.set_caption(f"Snake - Score : {score}")
    pygame.display.update()

def move_snake(serpent, direction, args):
    tete_x, tete_y = serpent[0]
    nouvelle_tete = (tete_x + direction[0] * int(args.tile_size), tete_y + direction[1] * int(args.tile_size))
    (new_tete_x, new_tete_y) = nouvelle_tete
    if len(serpent) > 3:
        if (new_tete_x, new_tete_y) in serpent[1:]:
            logger.info("Game over c")
            pygame.quit()
            sys.exit()
    if args.gameover_on_exit == False:
        if new_tete_x < 0 or new_tete_x > int(args.width) or new_tete_y < 0 or new_tete_y > int(args.height):
            pygame.quit()
            sys.exit()
    else:
        if new_tete_x < 0:
            new_tete_x = int(args.width) + new_tete_x
        elif new_tete_x > int(args.width):
            new_tete_x = new_tete_x - int(args.width) - args.tile_size
        elif new_tete_y < 0:
            new_tete_x = int(args.height) + new_tete_y
        elif new_tete_y > int(args.height):
            new_tete_y = new_tete_y - int(args.height) - args.tile_size
    serpent.insert(0, (new_tete_x, new_tete_y))


def update_fruit(snake_positions, n, read_args):
    if serpent[0]!=NOURRITURE1 and n==1:    
        serpent.pop()                       
    elif serpent[0]!=NOURRITURE2 and n==2:  
        serpent.pop()                       
    elif serpent[0]==NOURRITURE2 and n==2:  
        n=1                                 
        logger.debug("Snake has eaten a fruit.")                          
    elif serpent[0]==NOURRITURE1 and n==1:  
        n=2                                    
        logger.debug("Snake has eaten a fruit.")
    return n




args=read_args()

#Création de l'écran
screen = pygame.display.set_mode( (int(read_args().width), int(read_args().height)) )


#On initialise le serpent
serpent=[]    
for k in range (int(read_args().snake_length)):
    serpent.append(((COL[k]+k)*int(read_args().tile_size),LIGNE[k]*int(read_args().tile_size)))

#Set uo logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stderr)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
if read_args().debug:
    logger.setLevel(logging.DEBUG)

logger.debug("Start main loop.")


while True:
    

    clock.tick(args.fps)

    direction=process_events(direction)

    move_snake(serpent, direction,args)
       

    n=update_fruit(serpent, n, args)
     

    draw(screen, serpent, n, args)
    
    score=get_score()
    update_display(screen, score)




logger.info("Game over.")
pygame.quit()
sys.exit()
quit(0)
