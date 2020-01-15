import math
import pygame

pygame.display.init()

winx,winy=800,600
screen = pygame.display.set_mode((winx,winy))

done = False
xAxis=0
xCoefficient=0.001

yAxis=0
yCoefficient=0.001

centerX = int(winx/2)
centerY = int(winy/2)

bRad=55

while not done:

    xAxis += xCoefficient
    yAxis += yCoefficient
    
    if xCoefficient >= 1.0:
        xCoefficient*=-1
    
    if xCoefficient <= -1.0:
        xCoefficient*=-1
    
    if yCoefficient >= 1.0:
        yCoefficient*=-1
        
    if yCoefficient <= -1.0:
        yCoefficient*=-1
       
    mpointX = 400+(math.cos(xAxis) * 100)
    mpointY = 300+(math.sin(yAxis) * 100)
    
    mX,mY=pygame.mouse.get_pos()
    
    bRad = math.sqrt((mX-mpointX)**2 + (mY-mpointY)**2)
    
    events = pygame.event.get()
    
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done=True
        if e.type == pygame.QUIT:
            done=True
    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0), (int(mpointX),int(mpointY)), int(bRad))
    pygame.display.flip()
    

pygame.display.quit()