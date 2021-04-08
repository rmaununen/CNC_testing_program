import pygame
import serial
import time
import numpy as np
#serialcom = serial.Serial('/dev/cu.usbserial-1420', baudrate=9600, timeout=1) #Change port name to the one you are using


####################### INITIAL VALUES:
x = 320
y = 320
FPS = 30
speed_h = 8
speed_v = 10
r = 10
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
        #left and right
        if pressed[pygame.K_LEFT] and x>round(screen_width/20)+r:
            x-= speed_h
        elif pressed[pygame.K_RIGHT] and x<round(screen_width/20 + screen_width/2)-r:
            x+= speed_h
        if pressed[pygame.K_UP] and y>round(screen_width/10):
            y-= speed_v
        elif pressed[pygame.K_DOWN] and y<round((screen_width/10) + np.sqrt(2)*round(screen_width/2))-2*r:
            y+= speed_v
    #########################################
    # CALLING THE DRAWER TO DRAW A FRAME
    draw_background(0)
    # ПCHECK FOR GAME QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
