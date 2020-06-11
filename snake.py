import pygame
import sys
import random
white = (255,255,255)
black = (0,0,0)
map_size = 900
pygame.init()
screen = pygame.display.set_mode((map_size, map_size*3//4))
pygame.display.set_caption("Snake")
#screen.blit(circle_surface, 0)
main_Font = pygame.font.SysFont('Calibri', 170)
banner_Font = pygame.font.SysFont('Calibri', 100)
pygame.font.init()
screen.fill((141,141,141))

def end_game():
    pygame.quit()
    sys.exit()
    
while True:
  
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            
            print("break")
            end_game()
    pygame.display.update()