import pygame, sys, math, time
from pygame.locals import *
pygame.init()

pygame.mixer.init()
failsound=pygame.mixer.Sound('hey.mp3')
winsound=pygame.mixer.Sound('win.mp3')
screenW=1700
screenH=1000

background = pygame.image.load('ground.png')
background = pygame.transform.scale(background, (screenW, screenH))

font = pygame.font.SysFont(None, 50)

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption('myGame')

start = pygame.Rect(0,850,150,150)

end = pygame.Rect(1550, 0, 150, 150)

player = pygame.Rect((100,900,50,50))

detected = False

clock = pygame.time.Clock()

enemy = [
    pygame.Rect(400, 400, 100, 100),
    pygame.Rect(900, 10, 100, 100),
    pygame.Rect(1200, 600, 100, 100),
    pygame.Rect(600, 900, 100, 100),
    pygame.Rect(650, 450, 100, 100)
]

vision = [
    pygame.Rect(350, 200, 200, 200),
    pygame.Rect(850, 110, 200, 200),
    pygame.Rect(1150, 400, 200, 200),
    pygame.Rect(550, 700, 200, 200),
    pygame.Rect(750, 400, 200, 200)
]

warnings = [False, False, False, False, False]

dangerZones = []

dangerZones.append(enemy)
dangerZones.append(vision)

def UpDownLeftRight():
    if key[pygame.K_LEFT]:
        player.x-=1
    if key[pygame.K_RIGHT]:
        player.x+=1
    if key[pygame.K_UP]:
        player.y-=1
    if key[pygame.K_DOWN]:
        player.y+=1
def Boundaries():
    if player.x<0:
        player.x=0
    if player.y<0:
        player.y=0
    if player.x >screenW-player.w:
        player.x=screenW-player.w
    if player.y >screenH-player.h:
        player.y=screenH-player.h

def CollisionCheck():
    for i in range(5):

        if player.colliderect(vision[i]) or player.colliderect(enemy[i]):

            if not warnings[i]:
                failsound.play()

            warnings[i] = True

        else:
            warnings[i] = False
        if player.colliderect(end):
            winsound.play()

##    global detected
##    if player.colliderect(enemy):
##        detected = True
##        pygame.mixer.music.play()
##    if player.colliderect(vision):
##        detected = True
##        pygame.mixer.music.play()
##    if player.collidelist(dangerZones) >= 0:
##        detected = True


##    detectionRadius = 300
##    distance = math.hypot(player.x-enemy.x, player.y-enemy.y)
##    if distance < detectionRadius:
##        detected = True
    
def Draw():
    screen.blit(background, (0, 0))

    for i in range(5):

        if warnings[i]:
            pygame.draw.rect(screen, 'firebrick4', enemy[i], 0, 5)
        else:
            pygame.draw.rect(screen, 'red', enemy[i], 0, 5)

        pygame.draw.rect(screen, 'red', vision[i], 1, 0)

    pygame.draw.rect(screen, 'red', start, 0, 5)

    pygame.draw.rect(screen, 'green', end, 0, 5)

    pygame.draw.rect(screen, 'blue', player, 0, 5)



    pygame.display.update()



##    global detected
##    screen.fill('black')
##    if detected:
##        pygame.draw.rect(screen, 'crimson', enemy,0,5)
##    else:
##        pygame.draw.rect(screen, 'orange', enemy,0,5)
##
##    pygame.draw.rect(screen, 'blue', player,0,5)
##    pygame.draw.rect(screen, 'yellow', vision,1,0)
##    pygame.display.update()
running = True
while running:
    key = pygame.key.get_pressed()
    UpDownLeftRight()
    Boundaries()
    CollisionCheck()
    Draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
    if key[pygame.K_ESCAPE]:
        running=False
clock.tick(60)
pygame.quit()
sys.exit()
    

