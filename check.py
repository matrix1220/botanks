import pygame,botank
from time import sleep
import time,math
from sympy import Point, pi
from sympy.geometry import Ray

pygame.init()
gameDisplay = pygame.display.set_mode(botank.display)
pygame.display.set_caption('Battle City')

def pgpoint(x,y):
	return (256+x,128-y)

def dipray(r):
    l=r.getLine()
    list = [pgpoint(r.source.x,r.source.y)]
    #intersection
    if r.checkPoint(-256):
        list.append(pgpoint(-256,l.getPoint(-256)))
    elif r.checkPoint(256):
        list.append(pgpoint(256,l.getPoint(256)))
    pygame.draw.lines(gameDisplay, (255,0,0), True, list, 1) 
     
crashed = False
while not crashed:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_SPACE:
               pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

    gameDisplay.fill((0,0,0))
    #p=pygame.mouse.get_pos()
    r = Ray(Point(2, 3), Point(3, 5))
    dipray(r)
    #list = [pgpoint(0,0),pgpoint(100,100)]
    #pygame.draw.lines(gameDisplay, (255,0,0), True, list, 1) 

    pygame.display.update()
    time.sleep(1)

pygame.quit()
quit()