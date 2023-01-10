import pygame

#Intialize the pygame
pygame.init ()

#Create Screen
screen = pygame.display.set_mode((800,800))
#Title and Icon
pygame.display.set_caption("Party Game")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Background

#Player
playerImg = pygame.image.load('hen.jpg')#Will be a weapon
playerX= 200
playerY= 400
playerX_change = 0
pygame.key.set_repeat(15,15)
def player(x,y):
  screen.blit(playerImg, (playerX, playerY))

#Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
#Key Press Checker
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          playerX_change = -3
        if event.key == pygame.K_d:
          playerX_change = 3
        if event.key == pygame.K_ESCAPE:
          exit()
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_a or event.key == pygame.K_d:
            playerX_change = 0

    playerX += playerX_change
    if playerX <=0:
        playerX= 0
    elif playerX >=736:
        playerX = 736
    screen.fill((255,255,255))
    player(playerX,playerY)
    pygame.display.update()
