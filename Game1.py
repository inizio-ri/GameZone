import math
import random

import pygame
from pygame import mixer

# Initialize
# the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('body.png')

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon of the gaming window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship (1).png')
playerX = 370
playerY = 526
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(20, 705))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(20)

#bullet

#ready state means we cant see the bullet on screen
#fire means we can see the bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
testY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score (x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

# def draw_text_middle(text, size, color, surface):
#     font = pygame.font.SysFont('comicsans', size, bold=True)
#     label = font.render(text, 1, color)
#
#     surface.blit(label, (800 + 600 / 2 - (600/2), 800 + 600 / 2 - 800 / 2))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg , (x+22 , y+10))

def isCollision(enemyX, enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance <27:
        return True
    else:
        return False
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))



# Game loop which ensures the game is running in continuously
running = True
while running:

    # RGB values stated in the tuple
    screen.fill((0, 0, 0))
    # draw_text_middle(
    #     'Left/Right Arrows: Move block horizontally. Down Arrow: Accelerate block fall. Up Arrow: Rotate block clockwise.',
    #     12, (255, 255, 255), screen)
    # pygame.display.update()
    #background image
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check if it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

# checking for player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

# checking for enemy
    for i in range (num_of_enemies):

        # game over
        if enemyY[i] > 450:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text ()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(20, 705)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX,testY)
    pygame.display.update()