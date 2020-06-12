import pygame
import sys
import random
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
map_size = 900
x,y = 0,0
dx, dy =0,0
pygame.init()
screen = pygame.display.set_mode((map_size, map_size*3//4))
pygame.display.set_caption("Snake")
#screen.blit(circle_surface, 0)
main_Font = pygame.font.SysFont('Calibri', 170)
banner_Font = pygame.font.SysFont('Calibri', 100)
pygame.font.init()
screen.fill((141,141,141))
print(pygame.key.get_repeat())
pygame.key.set_repeat(1,1)

def end_game():
    pygame.quit()
    sys.exit()

def banner():
    screen.blit(banner_Font.render("Score: ", False, white),(0,0))

def show_snake(x,y):
    screen.blit(banner_Font.render("O", False, red),(x,y))

while True:
  
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            
            print("break")
            end_game()
        if action.type is pygame.KEYDOWN:
            if action.key is pygame.K_q:
                x=-1
                y=0
                print(x)
            if action.key is pygame.K_w:
                x=+1
                y=0
                print(x)
            if action.key is pygame.K_p:
                y=-1
                x=0
                print(y)
            if action.key is pygame.K_l:
                y=+1
                x=0
                print(y)
        #keys = pygame.key.get_pressed()
       
                 

    banner()
    screen.fill((141,141,141))
    dx +=x
    dy +=y
    show_snake(400+dx,400+dy)
    print("S")
    pygame.display.update()