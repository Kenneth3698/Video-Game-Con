#Name:Kenneth Ly
#Date:Dec 6, 2022
#Program Name: Dungeon Memory Game
#Purpose: To get a good mark in Computer Science and to build our RPG game 
import random
import time
import colorama as cr
cr.init(autoreset=True)
from art import *
from replit import audio
import sys
from tqdm import tqdm
from random import randint
from collections import deque
import pygame
from pygame.locals import *
import Tutorial
import flappy
#Title of the code
tprint("Speed Wizard's")
print(
  "--------------------------------------------------------------------------------------")
def leaderboard():
    print ("\n")
    print ("⬇ LeaderBoard ⬇") #LEADERBOARD SECTION
    f = open('H_Highscore.txt', 'r')
    leaderboard = [line.strip().split(',') for line in f.readlines() if line.strip()]
    leaderboard = [(i[0], int(i[1][:-3])) for i in leaderboard]
    leaderboard.sort(key=lambda tup: tup[1], reverse=True)
    for i in leaderboard[:5]:
        print(i[0], i[1],'pts')
    f.close()
    time.sleep(10)
#Slowprints text and changes colour of the text 
def slowprint(s, colour):
  for c in s + '\n':
    sys.stdout.write(colour + c + cr.Fore.WHITE)
    sys.stdout.flush()
    time.sleep(0.03)
slowprint("Welcome to Speed Wizard's! Where you can play 3 different games!",cr.Fore.WHITE)

#checks the name of the person to see if its only letters and if its under 10 characters
def CheckIfNameValid(name):
  if len(str(name)) < 11:
    if name.isalpha():
      return True, ""
    else:
      return False, f"{cr.Fore.RED}Please only use proper characters (letters only)"
  else:
    return False, f"{cr.Fore.RED}Name should not be over 10 characters"
  
  #Error Checks name to make it not more than 10 characters
while True:
  user = str(input("Please enter your name:"))
  valid, error = CheckIfNameValid(user)
  if valid == True:
    break
  else:
    print(error)
while True:
  print(f"{cr.Fore.GREEN}[1] Yes")
  print(f"{cr.Fore.RED}[2] No")
  question = input("Before We start would you like a tutorial? ")
  if question == "1":
    Tutorial.tutorial()
  if question == "2":
    break

while True:
  print(f"{cr.Fore.LIGHTCYAN_EX}[1] Reaction Time")
  print(f"{cr.Fore.YELLOW}[2] ")
  print(f"{cr.Fore.BLUE}[3] ")
  print(f"{cr.Fore.LIGHTBLUE_EX}[4] LeaderBoard")
  print(f"{cr.Fore.RED}[5] Exit")
  question2 = input("Please enter any option given. ")
  if question2 == "1":
    bar = tqdm(range(100), desc="Loading Reaction Time Game")
    time.sleep(1.00)
    for i in bar:
      time.sleep(0.05)
    flappy.main()
  elif question2 == "2":
    a
  elif question2 == "3":
    a
  elif question2 == "4":
    break

  elif question2 == "5":
    exit()
    
file = open ("H_Highscore.txt", "a")
score = str(input("enter you score: "))
file.write(f"{user},{score}pts\n")
file.close()
time.sleep(0.5)
leaderboard() 



