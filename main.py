import pygame
import serial
import time
import numpy as np
#serialcom = serial.Serial('/dev/cu.usbserial-1420', baudrate=9600, timeout=1) #Change port name to the one you are using


####################### INITIAL VALUES:
x = 320
y = 320
FPS = 30
speed_h = 5
speed_v = 5
r = 4
down = False
trace = []
b_time = 0
trace_length = 100
color_grad = round(200/trace_length)
screen_width, screen_height = 720, 600
run = True
t = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CNC control testing")
#bg1 = pygame.image.load("images/bg_lvl1.jpg")
#pl_stand = pygame.image.load("images/bg_lvl1.jpg")
####################### FUNCTIONS:

#FUNCTION THAT PRINTS TEXT
def print_text(message, x, y, font_col, font_type, font_size):
    pygame.display.init()
    pygame.font.init()
    font_type1 = pygame.font.Font(font_type, font_size)
    text = font_type1.render(message, True, font_col)
    win.blit(text, (x, y))
    pygame.display.update()

def draw_background(image):
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (200, 200, 200), (round(screen_width/20), round(screen_height/10), round(screen_width/2), np.sqrt(2)*round(screen_width/2)))
    for i in trace:
        pygame.draw.circle(win, (i[2], i[3], i[4]), (i[0], i[1]), r)
    if down:
        pygame.draw.circle(win, (255, 0, 0), (round(screen_width/2), round(screen_width/20)), r)
    pygame.draw.circle(win, (0, 0, 0), (x, y), r)
    #win.blit(bg, (0, 0))
    #win.blit(pl_stand, (x, y))
    print_text(str(a_time), round(screen_width/30), round(screen_width/30), (0, 0, 0), "fonts/Pixeboy.ttf", 20)
    pygame.display.update()

while run == True:
    #time
    t.tick(FPS)
    #Variable for current time
    a_time = float(pygame.time.get_ticks()/1000)
    pressed = pygame.key.get_pressed()
    drawing = True
    #########################################
    if drawing:
        moving = False
        #left and right
        if pressed[pygame.K_LEFT] and x>round(screen_width/20)+r:
            x-= speed_h
            moving = True
        elif pressed[pygame.K_RIGHT] and x<round(screen_width/20 + screen_width/2)-r:
            x+= speed_h
            moving = True
        if pressed[pygame.K_UP] and y>round(screen_width/10):
            y-= speed_v
            moving = True
        elif pressed[pygame.K_DOWN] and y<round((screen_width/10) + np.sqrt(2)*round(screen_width/2))-2*r:
            y+= speed_v
            moving = True
        if a_time-b_time>0.1:
            if pressed[pygame.K_SPACE]:
                if down == True:
                    down = False
                else:
                    down = True
            b_time = float(pygame.time.get_ticks() / 1000)
        if down and len(trace)<trace_length:
            position = [x, y, 200, 0, 0]
            trace.append(position)
        elif down and len(trace)>=trace_length and moving:
            trace.pop(0)
            position = [x, y, 200, 0, 0]
            trace.append(position)
        if down and moving:
            for i in trace:
                i[3] = i[3] + color_grad
                i[4] = i[4] + color_grad
    #########################################
    # CALLING THE DRAWER TO DRAW A FRAME
    draw_background(0)
    # ПCHECK FOR GAME QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
