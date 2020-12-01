import pygame
import random
import math

pygame.init()

#Screen
screen = pygame.display.set_mode((800,600))
#Background
bg = pygame.image.load('background.png')

#Title and Icon
pygame.display.set_caption("My first game")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)
fontX = 10
fontY = 10

#Player
pImage = pygame.image.load('player.png')
playerX = 360
playerY = 460
playerX_change = 0

#Enemy
eImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =  []

for i in range(5):
    eImage.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,700)) 
    enemyY.append(random.randint(80,180))
    enemyX_change.append(2) 
    enemyY_change.append(40)  


#Bullet
bulletImage = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 460
bulletX_change = 0
bulletY_change = 10
bullet_state = "Ready"

def show_score(x,y):
    score = font.render("Score: "+ str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))


def player(x,y):
    screen.blit(pImage,(x,y))

def enemy(x,y,i):
    screen.blit(eImage[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImage,(x+20,y+5))

def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2) + math.pow((enemyY-bulletY),2))
    if distance < 27:
        return True
    else:
        return False

#Game loop
running = True

while running:
    screen.fill((0,0,0))
    
    #Background Image:
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    #Keystroke
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -3
        if event.key == pygame.K_RIGHT:
            playerX_change = 3
        if event.key == pygame.K_UP:
            if bullet_state == "Ready":
                bulletX = playerX
                fire_bullet(bulletX,bulletY)


    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        
     

    #Player change
    playerX += playerX_change

    if(playerX <= 0):
        playerX = 0
    elif(playerX >= 740):
        playerX = 740

    #enemy change
    for i in range(5):
        enemyX[i] +=  enemyX_change[i]
        if(enemyX[i] <= 0):
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i] 
        elif(enemyX[i] >= 700):
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        
        #Collision

        col = collision(enemyX[i],enemyY[i],bulletX,bulletY)

        if col:
            bullet_state = "Ready"
            bulletY = 460
            score_value += 1
            
            enemyX[i] = random.randint(0,700)
            enemyY[i] = random.randint(40,90)
    
        enemy(enemyX[i],enemyY[i],i)


    #Bullet change

    if bulletY <= 0:
        bullet_state = "Ready"
        bulletY = 460

    if bullet_state == "Fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    
    show_score(fontX,fontY)
    player(playerX,playerY)
    pygame.display.update()
