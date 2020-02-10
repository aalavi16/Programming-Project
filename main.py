import time
import random
import re
import os
import csv

def login1P():
  """Authenticates the player before they play against the CPU."""
  print("Please enter your login details. ")
  username1 = input("Please enter your username: ")
  password1 = input("Please enter your password (don't use a password you use for another application): ") #passwords arent hashed

  file = open("login.txt","r")

  for row in file:
    field = row.split(",")
  username = field[0]
  password = field[1]
  lastchar = len(password)-1
  password = password[0:lastchar]

  if username1 == username and password1 == password:
    print("Hello",username)
    file.close()
    #game()


  else:
    print("incorrect") 
    file.close()
    login1P()

def login2P():
  """Authenticates the two players before they play against each other."""
  print("Player one, please enter your login details.")
  username1 = str(input("Username: "))
  password1 = str(input("Password: "))
  file = open("login.txt","r")
  for row in file:
    field = row.split(",")
  username = field[0]
  password = field[1]
  lastchar = len(password)-1
  password = password[0:lastchar]
  
  if username1 == username and password1 == password:
    print("Hello",username)
    print("Player two, please enter your login details.")
    username2 = str(input("Username: "))
    password2 = str(input("Password: "))
    for row in file:
      field = row.split(",")
    username = field[0]
    password = field[1]
    lastchar = len(password)-1
    password = password[0:lastchar]
    if username2 == username and password2 == password:
      print("Hello",username)
      file.close()
      #game
  else:
    print("incorrect") 
    file.close()
    login1P()

def mainmenu2():
  choice = int(input("1) 1 Player\n2) 2 Players\nChoice:  "))
  if choice == 1:
    menu1p()
  elif choice == 2:
    #menu2p()
    print("\033[1;31;1mWIP")


def menu1p():
  choice1 = int(input("1) Play Against CPU\n2) View Leaderboard\n3) Exit to Main Menu\n4) Exit Game\nChoice: "))
  while choice1 < 1 or choice1 > 4:
    choice1 = input("Invalid input! ")
  if choice1 == 1:
    #game1p()
    print("WIP")
  elif choice1 == 2:
    #Leaderboard
    print("WIP")
  elif choice1 == 3:
    mainmenu2()
  elif choice1 == 4:
    exit()
  

def mainmenu():
  choice = int(input("1) 1 Player\n2) 2 Players\nChoice:  "))
  if choice == 1:
    menu1p()
  elif choice == 2:
    #menu2p()
    print("\033[1;31;1mWIP")


import login
mainmenu()




