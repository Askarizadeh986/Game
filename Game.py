import pygame
import time
import random

from pygame.constants import *

pygame.init()
dodlev=25

lev=1
stuff_speed=7
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
bred=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
bgreen=(0,100,0)
bwhite=(102, 102, 102)
Crash_sound=pygame.mixer.Sound('Crash.wav')
Win_sound=pygame.mixer.Sound('Win.wav')
pygame.mixer.music.load('Stars.wav')
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Car Race')
clock=pygame.time.Clock()
caring=pygame.image.load('BB.png')
x=(display_width*0.45)
y=(display_height*0.8)
x_change=0
y_change=0
car_width=44
car_height=96
def button(msg,x,y,w,h,ia,ac,action=None):
    #pygame.mixer.music.stop(Win_sound)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and  y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                gameloop()
            elif action =="quit":
                pygame.quit()
                quit()

    
    else:
        pygame.draw.rect(gameDisplay,ia,(x,y,w,h))
    smallText=pygame.font.Font('freesansbold.ttf',20)
    TextSurf,TextRect=text_objects(msg,smallText)
    TextRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)


def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(blue)
        largeText=pygame.font.Font('freesansbold.ttf',90)
        TextSurf,TextRect= text_objects("Let's Play Game",largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button('Play',display_width/4,450,100,50,green,bgreen,"play")
        button('Quit',display_width/1.49,450,100,50,red,bred,"quit")
        

        pygame.display.update()
def stuff_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("score: "+str(count),True,red)
    gameDisplay.blit(text,(0,0))
def Level_Show(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Level: "+str(count),True,bgreen)
    gameDisplay.blit(text,(display_width-80,0))
def Speed_Show(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Speed:  "+str(count)+"Km,h",True,blue)
    gameDisplay.blit(text,((display_width-80)/2,0))
    pygame.display.update()

def stuff(stuffx,stuffy,file):
    gameDisplay.blit(file,(stuffx,stuffy))
    
def car(x,y):
    gameDisplay.blit(caring,(x,y))
def text_objects(text,font):
    textSurface=font.render(text,True,black)
    textSurface=font.render(text,True,black)
    return textSurface, textSurface.get_rect()


def crash ():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(Crash_sound)
    largeText=pygame.font.Font('freesansbold.ttf',90)
    TextSurf,TextRect= text_objects('You Crashed',largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button('Try agian',display_width/4,450,100,50,green,bgreen,"play")
        button('Quit',display_width/1.49,450,100,50,red,bred,"quit")
        pygame.display.update()

def gameloop():
    pygame.mixer.music.stop()
    gameDisplay.fill(white)
    global x
    global x_change
    global y
    global y_change
    global dodged
    global stuff_starty
    global stuff_speed
    global dodlev
    global lev
    global event
    global stuff_startx_tree
    pygame.mixer.music.play(-1)
    
    gameExit=False
    stuff_startx=random.randrange(0,display_width)
    stuff_startx_2=random.randrange(0,display_width)
    stuff_startx_3=random.randrange(0,display_width)
    stuff_startx_tree=random.randrange(0,display_width)
    stuff_starty=-600
    stuff_width=46
    stuff_width_tree=96
    stuff_height=96
    dodged=0
    while not gameExit:
        gameDisplay.fill(white)
        speedkm=int(stuff_speed*12.26)
        if x>display_width-car_width or x<0:
            car(x-100,y-100)
        if stuff_starty> display_height:

            stuff_starty=0-stuff_height
            stuff_startx=random.randrange(0,display_width)
            stuff_startx_2=random.randrange(0,display_width)
            stuff_startx_3=random.randrange(0,display_width)
            stuff_startx_tree=random.randrange(0,display_width)
            dodged+=1
            if (dodged % 1==0):
                stuff_speed+=0.5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
                    stuff_speed+=1
                
                if event.key == pygame.K_PAGEDOWN:
                    stuff_speed-=1
                    if stuff_speed< (dodged/2) + 7:
                        stuff_speed=(dodged/2) + 7
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP  :
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0 
        if y>display_height-car_height :
            y_change=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
        if y<-1:
            y_change=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 5
        
        if x>display_width-car_width  :
            x_change=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

        if x<-1:
            x_change=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5 
        if dodged>=dodlev:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(Win_sound)
            largeText=pygame.font.Font('freesansbold.ttf',40)
            TextSurf,TextRect= text_objects('You Win, Your New Level is '+str(lev+1),largeText)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf,TextRect)
            lev+=1
            dodlev+=25
            stuff_speed+=3
            while True:
                button('Next Level',150,450,100,50,green,bgreen,"play")
                button('Quit',550,450,100,50,red,bred,"quit")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                pygame.display.update()
        x += x_change
        y+=y_change
        gameDisplay.fill(white)
        ops1=pygame.image.load('ops.png')
        ops2=pygame.image.load('oos.png')
        ops3=pygame.image.load('ooo.png')
        tree=pygame.image.load('tree.png')
        stuff(stuff_startx,stuff_starty,ops1)
        if dodged%10==0 and dodged!=0:
            stuff(stuff_startx_tree,stuff_starty,tree)
        if dodged>5 or lev>1:
            stuff(stuff_startx_2,stuff_starty,ops2)
        if dodged>15 or lev>1:
             stuff(stuff_startx_3,stuff_starty,ops3)
        
        stuff_starty+=stuff_speed
        car(x,y)
        stuff_dodged(dodged)
        Level_Show(lev)
        Speed_Show(speedkm)
        if y<stuff_starty+stuff_height and y>stuff_starty:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                lev=1
                dodlev=25
                stuff_speed=7
                crash()
            if dodged>5 or lev>1:
                if x > stuff_startx_2 and x < stuff_startx_2 + stuff_width or x + car_width > stuff_startx_2 and x + car_width < stuff_startx_2 + stuff_width:
                    lev=1
                    stuff_speed=7
                    dodlev=25
                    crash()

            if dodged>15 or lev>1:
                if x > stuff_startx_3 and x < stuff_startx_3 + stuff_width or x + car_width > stuff_startx_3 and x + car_width < stuff_startx_3 + stuff_width:
                    lev=1
                    stuff_speed=7
                    dodlev=25

                    crash()
            if dodged%5==0:
                if x > stuff_startx_tree and x < stuff_startx_tree + stuff_width_tree or x + car_width > stuff_startx_tree and x + car_width < stuff_startx_tree + stuff_width_tree:
                    lev=1
                    stuff_speed=7
                    dodlev=25
                    
                    crash()    
        pygame.display.update()
        clock.tick(60)

game_intro()
gameloop()
pygame.quit()

    
