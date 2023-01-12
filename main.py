    
import pygame
from pygame import mixer
import random
import math

#Intialize the pygame
pygame.init()

#Create Screen
screen = pygame.display.set_mode((800, 600))

#Background
#background = pygame.image.load(#Background png)

#Background Sound
mixer.music.load('background.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.2)

#Title and Icon
pygame.display.set_caption("Cow Invaders")
icon = pygame.image.load('chick.png')
pygame.display.set_icon(icon)

#Background

#Player
playerImg = pygame.image.load('slingshot.png')  #Will be a weapon
playerX = 370
playerY = 480
playerX_change = 0

#Cow
cowImg = []
cowX = []
cowY = []
cowX_change = []
cowY_change = []
num_of_cows = 5



for i in range(num_of_cows):
  cowImg.append(pygame.image.load('cow.png'))
  cowX.append(random.randint(0,736))
  cowY.append(random.randint(50, 150))
  cowX_change.append (0.3)
  cowY_change.append (40)

#Rock
rockImg = pygame.image.load('rock.png')
rockX = 0
rockY = 480
rockX_change = 0
rockY_change = 1.5
rock_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Lives
lives_value = 3
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Game Over text
over_font = pygame.font.Font('freesansbold.ttf',64)     

def show_score(x,y):
  score = font.render("Score : " + str(score_value), True, (0, 255, 0))
  screen.blit(score, (x, y))
  
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text, (200, 250))

def life(x,y):
    lives = font.render("Lives: " + str(lives_value), True, (0, 255, 0))
    screen.blit(lives, (650, 10))
  
def player(x, y):
  screen.blit(playerImg, (playerX, playerY))


def cow(x, y, i):
  screen.blit(cowImg[i], (x, y))


def fire_rock(x, y):
  global rock_state
  rock_state = "fire"
  screen.blit(rockImg, (x + 16, y + 10))

def isCollision(cowX, cowY, rockX, rockY):
    distance = math.sqrt(math.pow(cowX - rockX, 2) + (math.pow(cowY - rockY, 2)))
    if distance < 27:
        return True
    else:
        return False
#Game Loop
running = True
while running:
    screen.fill((255, 255, 255))

  #Background added
  #screen.blit(background, (0, 0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
  #Key Press Checker
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
              playerX_change = -0.5
          if event.key == pygame.K_d:
              playerX_change = 0.5
          if event.key == pygame.K_SPACE:
              if rock_state is "ready":
                rock_sound = mixer.Sound('rock_throw.mp3')
                rock_sound.play()
                rock_sound.set_volume(0.2)
              #Gets Cordinate of the Slingshot
                rockX = playerX
                fire_rock(playerX, rockY)
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d:
          playerX_change = 0
  #player movement
    playerX += playerX_change
    if playerX <= 0:
      playerX = 0
    elif playerX >= 736:
      playerX = 736
      
  #Cow movement
    for i in range(num_of_cows):

      #Game Over and Life Removed
      if cowY[i] > 435 and cowY[i] < 450:
        lives_value -= 1
        life(650,10)
        
        
      if lives_value == 0:
        for j in range(num_of_cows):
          cowY[j] = 2000
          game_over_text()
          break
        
      cowX[i] += cowX_change[i]
      if cowX[i] <= 0:
        cowX_change[i] = 0.5
        cowY[i] += cowY_change[i]
      elif cowX[i] >= 736:
        cowX_change[i] = -0.7
        cowY[i] += cowY_change[i]
  #collision
      collision = isCollision(cowX[i],cowY[i],rockX,rockY)
      if collision:
        explosion_sound = mixer.Sound('Chicken_death.mp3')
        explosion_sound.play()
        rockY = 480
        rock_state = "ready"
        score_value += 1
        cowX[i] = 0
        cowY[i] = random.randint(50, 150)
  
      cow(cowX[i], cowY[i], i)
   # Rock Movement
    if rockY <= 0:
        rockY = 480
        rock_state = "ready"
  
    if rock_state is "fire":
        fire_rock(rockX, rockY)
        rockY -= rockY_change
    

  
    player(playerX, playerY)
    show_score(textX, textY)
    life(textX, textY)
    pygame.display.update()
