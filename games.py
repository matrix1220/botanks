import pygame
from time import sleep

pygame.init()

d_width = 1024
d_height = 700

white = (255,  255, 255)
green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((d_width, d_height))
pygame.display.set_caption('The Tank')

clock = pygame.time.Clock()

full_path = r'D:\Projects\botanks\\' # mana shu joyini rasm turgan papkaga yo'naltiriladi

tankImg = pygame.image.load(full_path + 'truck_up.png')
tankLeftImg = pygame.image.load(full_path + 'truck_left.png')
tankRightImg = pygame.image.load(full_path + 'truck_right.png')
tankDownImg = pygame.image.load(full_path + 'truck_down.png')
bulletImg = pygame.image.load(full_path + 'bullet_1.png')
gameDisplay.fill(green)

def fire(current, aim, truck, bg=None):
    
    bullet_position = current
    
    if aim == 0:
        bullet_position[0] += 85
    elif aim == 1:
        bullet_position[1] += 85
    elif aim == 2:
        bullet_position[1] += 85
        bullet_position[0] += 200
    elif aim == 3:
        bullet_position[0] += 85
        bullet_position[1] += 200
    
    gameDisplay.fill(green)
    gameDisplay.blit(truck, (x, y))
    gameDisplay.blit(bulletImg, bullet_position)
    pygame.display.update()
    
    bullet_step = 5
    
    for i in range(100):
        if aim == 0:
            bullet_position[1] -= bullet_step  #UP
            gameDisplay.fill(green)
            gameDisplay.blit(truck, (x, y))
            
            gameDisplay.blit(bulletImg, bullet_position)
            pygame.display.update()
        elif aim == 2:  #RIGHT
            bullet_position[0] += bullet_step
            gameDisplay.fill(green)
            gameDisplay.blit(truck, (x, y))
            
            gameDisplay.blit(bulletImg, bullet_position)
            pygame.display.update()
        elif aim == 3:  #DOWN
            bullet_position[1] += bullet_step
            gameDisplay.fill(green)
            gameDisplay.blit(truck, (x, y))
            
            gameDisplay.blit(bulletImg, bullet_position)
            pygame.display.update()
        elif aim == 1:  #LEFT
            bullet_position[0] -= bullet_step
            gameDisplay.fill(green)
            gameDisplay.blit(truck, (x, y))
            
            gameDisplay.blit(bulletImg, bullet_position)
            pygame.display.update()
        sleep(0.000001)    
        
    gameDisplay.fill(green)
    gameDisplay.blit(truck, (x, y))
    pygame.display.update()    
        
crashed = False

def tank(img, x, y, fire=False):
    # gameDisplay.blit(bgImg, (0, 0))
    gameDisplay.blit(img[1], (x, y))
    
x_change = 0
y_change = 0
x = d_width * 0.5
y = d_height * 0.5

step = 3

current_position = 0, tankImg

while not crashed:
    
    events = pygame.event.get()
    
    for event in events:
        
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                events.remove(event)
                if x > 0:
                    x_change = -step
                current_position = 1, tankLeftImg
                
            if event.key == pygame.K_RIGHT:
                events.remove(event)
                if x < d_width:
                    x_change = step
                current_position = 2, tankRightImg
                
            if event.key == pygame.K_UP:
                events.remove(event)
                if y > 0:
                    y_change = -step
                current_position = 0, tankImg
                
            if event.key == pygame.K_DOWN:
                events.remove(event)
                if y < d_height:
                    y_change = step
                current_position = 3, tankDownImg
            
            if event.key == pygame.K_SPACE:
                fire([x, y], current_position[0], current_position[1], )
            
            while len(pygame.event.get()) == 0:
                if x_change != 0 or y_change != 0:
                    if x_change > 0:
                        if x < (d_width - 200):
                            x += x_change
                    if x_change < 0:
                        if x > 0:
                            x += x_change
                    if y_change > 0:
                        if y < (d_width - 223):
                            y += y_change
                    if y_change < 0:
                        if y > 0:
                            y += y_change
                            
                    gameDisplay.fill(green)        
                    tank(current_position, x, y)
                    pygame.display.update()
                    sleep(0.000001)
                else:
                    x_change = 0
                    y_change = 0
                    break   
                    
        x_change = 0
        y_change = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0    
        
        print('X: ', x, '  Y: ', y)
        
        print(event)
        
    pygame.display.update()
    
    clock.tick(120)
    
pygame.quit()
quit()