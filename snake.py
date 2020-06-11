import pygame
import sys
import random
white = (255,255,255)
black = (0,0,0)
map_size = 500

pygame.init()
screen = pygame.display.set_mode((map_size, map_size))
pygame.display.set_caption("Kółko i Krzyżyk")
#screen.blit(circle_surface, 0)
main_Font = pygame.font.SysFont('Calibri', 170)
banner_Font = pygame.font.SysFont('Calibri', 100)


while True:
  
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            
            print("break")
            end_game()
    pygame.display.update()