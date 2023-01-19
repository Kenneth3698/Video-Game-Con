
#Name:Kenneth Ly
#Date:December 6, 2022
#Program Name: Cow Invaders
#Purpose:Video Game Culminating where you the player is killing Cows that are trying to invade your territory.

#Imports
import pygame, sys
from button import Button
from pygame import mixer
import random
import math
import os
import sys
import time
import colorama as cr
from art import *

#Intialize the pygame
pygame.init()

#Frame Rate
clock = pygame.time.Clock()
clock.tick(60)

#Create Screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('assets/background.png')

#Background Sound
mixer.music.load('sounds/background.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.2)

#Title and Icon
pygame.display.set_caption("Cow Invaders")
icon = pygame.image.load('assets/chick.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('assets/slingshot.png')  
playerX = 370
playerY = 480
playerX_change = 0

#Cow/Enemy
cowImg = []
cowX = []
cowY = []
cowX_change = []
cowY_change = []
num_of_cows = 7

#Getting the range of number of cows
for i in range(num_of_cows):
  cowImg.append(pygame.image.load('assets/cow.png'))
  cowX.append(random.randint(0,750))
  cowY.append(random.randint(25, 125))
  cowX_change.append(4)
  cowY_change.append(40)
  
#Barrier
blockImg = []
blockX = []
blockY = []
num_of_blocks = 5

#Getting the range of number of Blocks
for b in range(num_of_blocks):
  blockImg.append(pygame.image.load('assets/block.png'))
  blockX.append(random.randint(40,760))
  blockY.append(random.randint(250, 350))


#Rock/Object to hit enemy
rockImg = pygame.image.load('assets/rock.png')
rockX = 0
rockY = 480
rockX_change = 0
rockY_change = 10
rock_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Lives
lives_value = 1
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10


#Game Over
gameover = False

#Game Over text
over_font = pygame.font.Font('freesansbold.ttf',64)     
restart_font = pygame.font.Font('freesansbold.ttf',32)
def show_score(x,y):
  score = font.render("Score : " + str(score_value), True, (255, 255, 255))
  screen.blit(score, (x, 536))

#Display game over and press r to restart once enemy makes it passed a postion
def game_over_text():
    global gameover
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(restart_text, (250, 350))
    gameover = True

#Lives display 
def life(x,y):
    lives = font.render("Lives: " + str(lives_value), True, (255, 255, 255))
    screen.blit(lives, (670, 536))
  
#Player display
def player(x, y):
  screen.blit(playerImg, (playerX, playerY))

#Cow display
def cow(x, y, i):
  screen.blit(cowImg[i], (x, y))

#Block display
def blocked(x, y, b):
  screen.blit(blockImg[b], (x, y))
  
#Rock display when fired
def fire_rock(x, y):
  global rock_state
  rock_state = "fire"
  screen.blit(rockImg, (x + 16, y + 10))

#Detecting for a collision on the rock and cow
def isCollision(cowX, cowY, rockX, rockY):
    distance = math.sqrt(math.pow(cowX - rockX, 2) + (math.pow(cowY - rockY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Detecting for a collision on the rock and Block
def isBlocker(blockX, blockY, rockX, rockY):
    distance2 = math.sqrt(math.pow(blockX - rockX, 2) + (math.pow(blockY - rockY, 2)))
    if distance2 < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
      #Key Press Checker
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if rock_state is "ready":
                  #rock throw sounds
                  rock_sound = mixer.Sound('sounds/rock_throw.mp3')
                  rock_sound.play()
                  rock_sound.set_volume(0.2)
                #Gets Cordinate of the Slingshot
                  rockX = playerX
                  fire_rock(playerX, rockY)
            #Restarting Code so you can play again
            if event.key == pygame.K_r and gameover:
              playerX = 370
              PlayerY = 480
              for i in range(num_of_cows):
               cowY[i] = (random.randint(25, 125))
               cowX[i] = (random.randint(0,750))
              for b in range(num_of_blocks):
               blockY[b] = (random.randint(50,150))
               blockX[b] = (random.randint(0,750))
              score_value = 0
              lives_value = 1
              gameover = False
            if event.key == pygame.K_ESCAPE:
              sys.exit()
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_a or event.key == pygame.K_d:
            playerX_change = 0
          
    #player movement
    playerX += playerX_change
    if playerX <= 0:
      playerX = 0
    elif playerX >= 736:
      playerX = 736
      

    for i in range(num_of_cows):
      #Game Over
      if cowY[i]> 440:
        for j in range(num_of_cows):
          cowY[j] = 2000
          blockY[b] = 2000
        game_over_text()
        
      #Life Removed
      if cowY[i] > 440:
        lives_value = 0

      #Border Collision when the cow hits this it will move the cow the other direction
      cowX[i] += cowX_change[i]
      if cowX[i] <= 0:
        cowX_change[i] = +3
        cowY[i] += cowY_change[i]
      elif cowX[i] >= 736:
        cowX_change[i] = -3
        cowY[i] += cowY_change[i]
            #collision
      collision = isCollision(cowX[i],cowY[i],rockX,rockY)
      if collision:
      #Collision sounds
        explosion_sound = mixer.Sound('sounds/Cow_death.oga')
        explosion_sound.play()
        explosion_sound.set_volume(0.2)
        rockY = 480
        rock_state = "ready"
        score_value += 1
        cowX[i] = random.randint(0,750)
        cowY[i] = random.randint(50, 150)
  
      cow(cowX[i], cowY[i], i)
    
    for b in range(num_of_blocks): 
      #Blocker collision
      blocker = isBlocker(blockX[b], blockY[b], rockX, rockY)
      if blocker:
        wood_sound = mixer.Sound('sounds/wood_broke.mp3')
        wood_sound.play()
        wood_sound.set_volume(0.2)
        rockY = 480
        rock_state = "ready"
        blockX[b] = random.randint(40,760)
        blockY[b] = random.randint(250, 350)

      blocked(blockX[b], blockY[b], b)

   # Rock Movement
    if rockY <= 0:
        rockY = 480
        rock_state = "ready"
  
    if rock_state is "fire":
        fire_rock(rockX, rockY)
        rockY -= rockY_change
    #displaying position stated at the top
    player(playerX, playerY)
    show_score(textX, textY)
    life(textX, textY)
    pygame.display.update()