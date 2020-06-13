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
snake_all = []
class Snake_element:
    def __init__(self,number,x,y):
        self.number = number
        self.x = x
        self.y = y
snake_el = Snake_element(1,400,400)
snake_el_2 = Snake_element(2,400,465)
snake_el_3 = Snake_element(3,
400,530)



print(snake_el.x)
snake_all.append(snake_el)
snake_all.append(snake_el_2)
snake_all.append(snake_el_3)
print(snake_all[0])

def end_game():
    pygame.quit()
    sys.exit()

def banner():
    screen.blit(banner_Font.render("Score: ", False, white),(0,0))

def show_snake(snake,dx,dy):
    for i in snake:
       screen.blit(banner_Font.render(str(i.number), False, red),(i.x , i.y ))
       print(i,  i.x, " ", i.y)
    first_el_x = snake[0].x
    first_el_y = snake[0].y

    for i in range(len(snake)-2,-1, -1):
        print("i", i)
        snake[i+1].x = snake[i].x
        snake[i+1].y = snake[i].y
       
        

    first_el_y += dy*65
    first_el_x += dx*60
    snake[0].x = first_el_x
    snake[0].y = first_el_y
    print("len snake: ", len(snake))
    
show_snake(snake_all,0,0)
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
       
                 
            screen.fill((141,141,141))
            banner()
    
            dx +=x
            dy +=y
            show_snake(snake_all,x,y)
    pygame.display.update()