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
def slowprint(s, colour):
  for c in s + '\n':
    sys.stdout.write(colour + c + cr.Fore.WHITE)
    sys.stdout.flush()
    time.sleep(0.03)
def tutorial():
  #Loading Bar
  bar = tqdm(range(100), desc="Loading Tutorial")
  time.sleep(1.00)
  for i in bar:
    time.sleep(0.05)
  tprint("Tutorial")
  print(
    "-----------------------------------------------------------------------------------------------")
  slowprint("Welcome to Tutorial Where you can how to play these 3 games! ",cr.Fore.WHITE)
  while True:
    print(f"{cr.Fore.LIGHTCYAN_EX}[1] Reaction Time")
    print(f"{cr.Fore.GREEN}[2] Game2")
    print(f"{cr.Fore.GREEN}[3] Game3")
    print(f"{cr.Fore.RED}[4] Main Menu")
    Tutorial = input("Please select a game to learn about? ")
    if Tutorial == "1":
      React.react()
    if Tutorial == "2":
      3
    if Tutorial == "3":
      5
    if Tutorial == "4":
      import main