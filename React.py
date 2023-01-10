import random
import time
import colorama as cr
cr.init(autoreset=True)
from art import *
from replit import audio
import sys
from tqdm import tqdm

def react():
  tprint("Reaction Game")
  print(
    "-----------------------------------------------------------------------------------------------")
  while True:
    print(f"{cr.Fore.LIGHTCYAN_EX}[1] Rules")
    print(f"{cr.Fore.GREEN}[2] Play Game")
    print(f"{cr.Fore.GREEN}[3] Tutorial Menu")
    ReactPick = input("Please select a game to learn about? ")
    if ReactPick == "1":
      a
    if ReactPick  == "2":
      Tflappy.main()
    if ReactPick == "3":
      main.menu()
