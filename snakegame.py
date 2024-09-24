# Include libraries
import pygame
import time
import random
# Initialize Pygame
pygame.init()
# Define some colors
white = (255, 255, 255)
yellow = (255,255,102)
red = (213, 50, 80)
black = (0,0,0)
green = (0,255,0)
blue = (50,153,213)
# Set the width and height of each snake segment
dis_width = 800
dis_height = 800
# Set snake block size and speed
snake_block = 10
snake_speed = 15
# Create the display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game By HussainXPython")
# Set the clock
clock = pygame.time.Clock()
# Define font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms",35)
def our_snake(snake_blick, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block,snake_block])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block)/10.0) *10.0
    foody = round(random.randrange(0, dis_width - snake_block)/10.0) *10.0
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis,green,[foodx,foody,snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_list)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block)/10.0) * 10.0
            foody = round(random.randrange(0, dis_width - snake_block)/10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()
