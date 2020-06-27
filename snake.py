import pygame
import sys
import random
import time

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
map_size = 900
x,y = 0,0
dx, dy = 0,0
score = 0
pygame.init()
screen = pygame.display.set_mode((map_size, map_size*3//4))
pygame.display.set_caption("Snake")
#screen.blit(circle_surface, 0)

snake_font_size =30
main_Font = pygame.font.SysFont('Calibri', 170)
banner_Font = pygame.font.SysFont('Calibri', 70)
snake_Font = pygame.font.SysFont('Calibri', snake_font_size)
pygame.font.init()

screen.fill((141,141,141))
print(pygame.key.get_repeat())
pygame.key.set_repeat(1,1)
snake_all = []
apple_all = []
class Snake_element:
    def __init__(self,number,x,y):
        self.number = number
        self.x = x
        self.y = y

class Apple_element:
    def __init__(self,id,x,y):
        self.id = id
        self.x = x
        self.y = y

for i in range(1,2):
    snake_el = Snake_element(i,400,350+i*snake_font_size*0.7)
    snake_all.append(snake_el)

for o in range(1,11):
    apple2_x = random.randint(0,40)
    apple2_y = random.randint(4,40)
    apple_all.append(Apple_element( o, apple2_x * 21, apple2_y * 21))



#print(snake_el.x)
#snake_all.append(snake_el)
#snake_all.append(snake_el_2)
#snake_all.append(snake_el_3)
print(snake_all[0])

def end_game():
    pygame.quit()
    sys.exit()

def banner(score):
    screen.blit(banner_Font.render("Score: " + str(score), False, white),(0,0))

def show_snake(snake,dx,dy):
    for i in snake:
       screen.blit(snake_Font.render('O', False, red),(i.x , i.y ))
      # print(i,  i.x, " ", i.y)
    first_el_x = snake[0].x
    first_el_y = snake[0].y

    for i in range(len(snake)-2,-1, -1):
       # print("i", i)
        snake[i+1].x = snake[i].x
        snake[i+1].y = snake[i].y
       
        

    first_el_y += dy*snake_font_size*0.6
    first_el_x += dx*snake_font_size/2
    snake[0].x = first_el_x
    snake[0].y = first_el_y
   # print("len snake: ", len(snake))
    
show_snake(snake_all,0,0)

def snake_growth(d_x, x, y):
    if len(snake_all) > 1 and (snake_all[-1].x - snake_all[-2].x) != 0:
        x_sign = (snake_all[-1].x - snake_all[-2].x)/abs(snake_all[-1].x - snake_all[-2].x)
    else:
        x_sign = -1

    if len(snake_all) > 1 and (snake_all[-1].y - snake_all[-2].y) != 0:
        y_sign = (snake_all[-1].y - snake_all[-2].y)/abs(snake_all[-1].y - snake_all[-2].y)
    else:
        y_sign = -1

    if d_x != 0:
        snake_all.append(Snake_element(i,snake_all[-1].x + snake_font_size * 0.7 * x_sign ,snake_all[-1].y + snake_font_size*0.7 * y_sign))
        print(d_x)
        print("len snake: ", len(snake_all))
        
def add_apple():
    last_apple_id = apple_all[-1].id
    apple_x = random.randint(0,40)
    apple_y = random.randint(4,40)
    apple_all.append(Apple_element(last_apple_id+1, apple_x * 21, apple_y * 21))

def show_apple():
   
    for apple in apple_all:
        screen.blit(snake_Font.render('X', False, blue),(apple.x, apple.y))

def detect_colision(x,y):
    global score
    for apple in apple_all:
        if ((snake_all[0].x in range(int(apple.x), int(apple.x + 22))) and (snake_all[0].y in range(int(apple.y), int(apple.y + 21)))) or (((snake_all[0].x + 21) in range(int(apple.x), int(apple.x + 22))) and ((snake_all[0].y + 21) in range(int(apple.y), int(apple.y + 21)))) :
            print("collision")
            print(apple.id)
            apple_all.remove(apple)
            score +=1
            add_apple()
            snake_growth(1,x,y)

while True:
  
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            
            print("break")
            end_game()
        if action.type is pygame.KEYDOWN:
            if action.key is pygame.K_o:
                x=-1
                y=0
               # print(x)
            if action.key is pygame.K_p:
                x=+1
                y=0
               # print(x)
            if action.key is pygame.K_q:
                y=-1
                x=0
               # print(y)
            if action.key is pygame.K_a:
                y=+1
                x=0
              #  print(y)
        #keys = pygame.key.get_pressed()
       
                 
    screen.fill((141,141,141))
    banner(score)
    
    dx +=x
    dy +=y
    show_snake(snake_all,x,y)
    if dx+dy % 19 == 0 and dx+dy != 0:
        add_apple()
        
    #print(dx)
    detect_colision(x,y)
    show_apple()
    
    if dx !=0 and dx % 7 == 0:
        snake_growth(dx,x,y)
   
    time.sleep(1/8)
    pygame.display.update()