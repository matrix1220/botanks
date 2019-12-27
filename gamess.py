from sympy import Point, pi
from sympy import atan2, oo, pi
import pygame,botank
from time import sleep
import time

bot = botank.Botank
bot.newTank(1)
tank=bot.newTank(2)
tank.newCommand(2,2)
tank.newCommand(1)

pygame.init()
gameDisplay = pygame.display.set_mode(botank.display)
pygame.display.set_caption('Battle City')


full_path = r'D:\Projects\botanks\\' # mana shu joyini rasm turgan papkaga yo'naltiriladi
#bulletImg = pygame.image.load(full_path + 'bullet_1.png')

tankImg = pygame.image.load(full_path + 'down1.png')

#gameDisplay.fill(green)
#gameDisplay.blit(tankImg, tank.getCoords())
#gameDisplay.blit(pygame.transform.rotate(tankImg,30), (10, 10))

        
crashed = False
while not crashed:   
    if tank.pos.x>200: tank.newCommand(2,3)
    if tank.pos.x<100: tank.newCommand(2,1)
    events = pygame.event.get()
    
    for event in events:
        
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bot.newCommand(1,2,0)
                #tank.turn(side)
            elif event.key == pygame.K_RIGHT:
                bot.newCommand(1,2,1)
                #tank.turn(side)
            elif event.key == pygame.K_UP:
                bot.newCommand(1,1)
                #tank.go()
            elif event.key == pygame.K_DOWN:
                bot.newCommand(1,0)
                #tank.stop()
            #if event.key == pygame.K_SPACE:
        #print(event)

    gameDisplay.fill((0,0,0))
    for t in botank.Tank.All:
        print(atan2(t.face.direction.y,t.face.direction.x))
        gameDisplay.blit(pygame.transform.rotate(tankImg,atan2(t.face.direction.y,t.face.direction.x)/pi*180), t.getCoords())
    pygame.display.update()
    time.sleep(1)


pygame.quit()
quit()