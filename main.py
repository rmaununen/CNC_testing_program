import pygame
import serial
import time
import numpy as np
#serialcom = serial.Serial('/dev/cu.usbserial-A50285BI', baudrate=28800, timeout=1) #Change port name to the one you are using


####################### INITIAL VALUES:
x = 320
y = 320
FPS = 30
speed_h = 6
speed_v = 6
motor_speed = 1
delta_motor_speed = 0.01
r = 5
r1 = 9
down = False
pressed_space = False
single_point_done = False
trace = []
b_time = 0
trace_length = 100
color_grad = round(200/trace_length)
screen_width, screen_height = 720, 600
run = True
move_left = False
move_right = False
move_up = False
move_down = False
contact_down = False
contact_up = False
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

def draw_button(direction, xb, yb):
    global motor_speed, delta_motor_speed
    width = 30
    height = 20
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (xb < mouse[0] < xb + width) and (yb < mouse[1] < yb + height):
        pygame.draw.rect(win, (210, 160, 160), (xb, yb, width, height))
        if click[0] == 1:
            pygame.time.delay(30)
            if direction == 'plus':
                motor_speed += delta_motor_speed
            else:
                motor_speed -= delta_motor_speed
    else:
        pygame.draw.rect(win, (160, 160, 160), (xb, yb, width, height))
    if direction == 'plus':
        print_text('+', xb+0.35*width, yb, (0, 0, 0), "fonts/Roboto.ttf", 20)
    else:
        print_text('-', xb+0.35*width, yb-height/2, (0, 0, 0), "fonts/Roboto.ttf", 35)

def draw_background(image):
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (200, 200, 200), (round(screen_width/20), round(screen_height/10), round(screen_width/2), np.sqrt(2)*round(screen_width/2)))
    for i in trace:
        pygame.draw.circle(win, (i[2], i[3], i[4]), (i[0], i[1]), r)
    if down:
        pygame.draw.rect(win, (255, 50, 50), (round(0.6*screen_width), round(screen_height/20), round(screen_width/10), round(screen_height/20)))
        print_text('contact', round(0.6*screen_width)+5, round(screen_height/20)+5, (0, 0, 0), "fonts/Roboto.ttf", 20)
    pygame.draw.rect(win, (220, 255, 220), (round(0.72 * screen_width), round(screen_height / 20), round(screen_width / 10), round(screen_height / 20)))
    print_text('reset 1', round(0.72 * screen_width) + 5, round(screen_height / 20) + 5, (0, 0, 0), "fonts/Roboto.ttf", 20)
    pygame.draw.rect(win, (220, 255, 220), (round(0.84 * screen_width), round(screen_height / 20), round(screen_width / 10), round(screen_height / 20)))
    print_text('reset 2', round(0.84 * screen_width) + 5, round(screen_height / 20) + 5, (0, 0, 0), "fonts/Roboto.ttf", 20)
    pygame.draw.circle(win, (0, 0, 0), (x, y), r)
    print_text(str(a_time), round(screen_width/30), round(screen_height/30), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('CW', round(3*screen_width/4), round(0.5*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('CCW', round(3*screen_width/4)+round(screen_width/7), round(0.5*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('Motor 1', round(0.6*screen_width), round(0.6*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('Motor 2', round(0.6*screen_width), round(0.69*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('Motor 3', round(0.6*screen_width), round(0.78*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('Motor 4', round(0.6*screen_width), round(0.87*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('x: ' + str(x) + ' p', round(0.6*screen_width), round(0.25*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    print_text('y: ' + str(y) + ' p', round(0.6*screen_width), round(0.30*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    if move_right:
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4), round(0.62*screen_height)), r1)
        pygame.draw.circle(win, (0, 0, 230), (round(3*screen_width/4)+round(screen_width/7), round(0.62 * screen_height)), r1)
    elif move_left:
        pygame.draw.circle(win, (0, 0, 230), (round(3*screen_width/4), round(0.62*screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4)+round(screen_width/7), round(0.62 * screen_height)), r1)
    else:
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4), round(0.62*screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4)+round(screen_width/7), round(0.62 * screen_height)), r1)
    if move_up:
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4), round(0.71*screen_height)), r1)
        pygame.draw.circle(win, (0, 0, 230), (round(3*screen_width/4)+round(screen_width/7), round(0.71 * screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4), round(0.8*screen_height)), r1)
        pygame.draw.circle(win, (0, 0, 230), (round(3*screen_width/4)+round(screen_width/7), round(0.8 * screen_height)), r1)
    elif move_down:
        pygame.draw.circle(win, (0, 0, 230), (round(3*screen_width/4), round(0.71*screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4)+round(screen_width/7), round(0.71 * screen_height)), r1)
        pygame.draw.circle(win, (0, 0, 230), (round(3*screen_width/4), round(0.8*screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4)+round(screen_width/7), round(0.8 * screen_height)), r1)
    else:
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4), round(0.71*screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4)+round(screen_width/7), round(0.71 * screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4), round(0.8*screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4)+round(screen_width/7), round(0.8 * screen_height)), r1)
    if contact_down:
        pygame.draw.circle(win, (0, 0, 230), (round(3 * screen_width / 4), round(0.89 * screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3 * screen_width / 4) + round(screen_width / 7), round(0.89 * screen_height)), r1)
    elif contact_up:
        pygame.draw.circle(win, (180, 180, 240), (round(3 * screen_width / 4), round(0.89 * screen_height)), r1)
        pygame.draw.circle(win, (0, 0, 230), (round(3 * screen_width / 4) + round(screen_width / 7), round(0.89 * screen_height)), r1)
    else:
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4), round(0.89*screen_height)), r1)
        pygame.draw.circle(win, (180, 180, 240), (round(3*screen_width/4)+round(screen_width/7), round(0.89 * screen_height)), r1)
    #win.blit(bg, (0, 0))
    #win.blit(pl_stand, (x, y))
    print_text('Motor speed [rps]', round(0.56 * screen_width), round(0.4 * screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
    draw_button('plus', round(0.95*screen_width), round(0.4*screen_height))
    draw_button('minus', round(0.8*screen_width), round(0.4*screen_height))
    print_text(str('{:.2f}'.format(round(motor_speed, 2))), round(0.87*screen_width), round(0.4*screen_height), (0, 0, 0), "fonts/Roboto.ttf", 20)
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
        move_left = False
        move_right = False
        move_up = False
        move_down = False
        #left and right
        if pressed[pygame.K_LEFT] and x>=round(screen_width/20)+r+speed_h:
            x-= speed_h
            moving = True
            move_left = True
            #serialcom.write("2\n".encode())
        elif pressed[pygame.K_RIGHT] and x<=round(screen_width/20 + screen_width/2)-r-speed_h:
            x+= speed_h
            moving = True
            move_right = True
            #serialcom.write("1\n".encode())
        #else:
            #serialcom.write("0\n".encode())
        if pressed[pygame.K_UP] and y>=round(screen_height/10)+r+speed_v:
            y-= speed_v
            moving = True
            move_up = True
        elif pressed[pygame.K_DOWN] and y<round((screen_height/10) + np.sqrt(2)*round(screen_width/2))-r-speed_v:
            y+= speed_v
            moving = True
            move_down = True

        if moving:
            single_point_done = False
        if pressed[pygame.K_SPACE] and not pressed_space:
            if down == True:
                down = False
            else:
                down = True
            pressed_space = True
        if not pressed[pygame.K_SPACE]:
            pressed_space = False
        if down and len(trace)<trace_length and moving:
            position = [x, y, 200, 0, 0]
            trace.append(position)
        elif down and len(trace)>=trace_length and moving:
            trace.pop(0)
            position = [x, y, 200, 0, 0]
            trace.append(position)
        elif down and not moving and not single_point_done:
            if len(trace)>=trace_length:
                trace.pop(0)
            position = [x, y, 200, 0, 0]
            trace.append(position)
            single_point_done = True
        if down and moving:
            for i in trace:
                i[3] = i[3] + color_grad
                i[4] = i[4] + color_grad
        if pressed[pygame.K_BACKSPACE]:
            trace = []
    #########################################
    # CALLING THE DRAWER TO DRAW A FRAME
    draw_background(0)
    # ПCHECK FOR GAME QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
serialcom.close()