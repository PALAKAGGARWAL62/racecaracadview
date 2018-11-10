import pygame as p
import time
import random

p.init()

dispwidth = 800
dispheight = 600

gamedisplay = p.display.set_mode((dispwidth, dispheight))
p.display.set_caption("BiT RaCeY")


black = (0,0,0)
white=(255,255,255)
red = (255,0,0)

car_width = 73

carImg  = p.image.load('racecar.png')

def things(thingx, thingy, thingw, thingh, color):
    p.draw.rect(gamedisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gamedisplay.blit(carImg, (x,y))

def text_objects(text,font):
    text_Surface= font.render(text,True, black)
    return text_Surface,text_Surface.get_rect()

def message_display(text):
    largeText = p.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (dispwidth/2),(dispheight/2)
    gamedisplay.blit(TextSurf,TextRect)

    p.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('YOU CRASHED!')


def game_loop():
    x=dispwidth*0.45
    y=dispheight*0.8

    x_change = 0
    car_speed = 0

    clock = p.time.Clock()

    gameExit = False

    while not gameExit:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()

            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    x_change = -5
                elif event.key == p.K_RIGHT:
                    x_change = 5
            if event.type == p.KEYUP:
                if event.key == p.K_LEFT or event.key == p.K_RIGHT:
                    x_change=0

            print(event)
        x += x_change
        gamedisplay.fill(white)
        car(x,y)

        if x>dispwidth-car_width or x<0:
            crash()

        p.display.update()
        clock.tick(60)

game_loop()
p.quit()
quit()