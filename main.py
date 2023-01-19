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

#Frame Rate
clock = pygame.time.Clock()
clock.tick(30)

#Intialize the pygame
pygame.init()

#Main Menu Music and volume played
mixer.music.load('sounds/Main_Menu.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.2)

#Screen display and load
SCREEN = pygame.display.set_mode((800, 600))
BG = pygame.image.load("assets/Menu.png")

#Caption and Icons
pygame.display.set_caption("Main Menu")
icon = pygame.image.load('assets/chick.png')
pygame.display.set_icon(icon)

#Font size
def get_font(size):
    # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#Option Button
def options():
    #Frame Rate
    clock = pygame.time.Clock()
    clock.tick(60)
    
    #Create Screen
    screen = pygame.display.set_mode((800, 600))
    #Title and Icon
    pygame.display.set_caption("Main Menu")
    icon = pygame.image.load('assets/chick.png')
    pygame.display.set_icon(icon)
    
    #Background
    background = pygame.image.load('assets/Option.png')
    #Screen blit background, image and text.  
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
      
        #Back button in options
        OPTIONS_BACK = Button(image=pygame.image.load("assets/Back.png"), pos=(750, 50), 
                            text_input="", font=get_font(32), base_color="White", hovering_color="Black")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        #Mouse Input on button
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
#Main Menu Screen
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        #Display all the buttons, font, position, and colour
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300, 380), 
                            text_input="", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(750, 50), 
                            text_input="", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(460, 380), 
                            text_input="", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        #Using the button file to make 3 different buttons
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        #Mouse Input on button as well when clicked it will load thhe def or file
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    import Invaders
                    Invaders.main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()