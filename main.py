from time import sleep
import random
import re
import os
import csv
global multiplayer
multiplayer = False
global player1Total
global cpuTotal
global point1
global point2
global point
global round
global roll


def game():
  print("hi")
def login1P():
  """Authenticates the player before they play against the CPU. - ACTUALLY WORKS!"""
  username = str(input("Please enter your username! "))
  password = str(input("Please enter your password! "))
  with open('UsernamePassword.csv', newline='') as csvfile:
    loginReader = csv.reader(csvfile, delimiter=',', quotechar='|')
    loggedinplayer1 = False
    
    for row2 in loginReader:
      if row2[0] == username:
        if row2[1]  == password:
          print("Works")
          loggedinplayer1 = True
          break
        else:
          continue
      else:
        continue
    if loggedinplayer1 == True:
      if multiplayer == True:
        login2P()
      else:
        print("Let's play")
    else:
      print("Invalid username or password!")
      login1P()
      #usernames = []
      #database = (', '.join(row2))
    # longlist = []

      #print(database)

      #database2 = database.split(",")
      #print(database2)


score = 0
highscore = 0
username = ''
life = 3
loginA = 0
def login():
  global username
  global loginA
  check = open('UsernamePassword.csv','r')
  database = csv.reader(check,delimiter=',')
  loggedin1 = False
  while loggedin1==False:
    username = input("Please enter your username ")
    password = input("Please enter your password ")
    for row in database:
      usernameF = row[0]
      passwordF = row[1]
      if (usernameF == username and passwordF == password):
        loggedin1 = True
        print("Welcome " + username + "!")
        sleep(1)
        if multiplayer == True:
          login2P()
    if loggedin1 == False and loginA<4:
      print('Failed to sign in. Please try again') 
      loginA = loginA + 1
      login()
    #elif loggedin1 == False and loginA == 3:
    #  print("You have had too many attempts")
     # sleep(1)
      #print("Please try again later")
      #sleep(1)
     # print("Goodbye")
     # exit()

def login2P():
  global username
  global loginA
  check = open('UsernamePassword.csv','r')
  database = csv.reader(check,delimiter=',')
  loggedin2 = False
  while loggedin2==False:
    username = input("Please enter your username, player 2")
    password = input("Please enter your password, player 2")
    for row in database:
      usernameF = row[0]
      passwordF = row[1]
      if (usernameF == username and passwordF == password):
        loggedin2 = True
        print("Welcome " + username + "!")
        sleep(1)
    if loggedin2 == False and loginA<4:
      print('Failed to sign in. Please try again') 
      loginA = loginA + 1
      login()
    #elif loggedin2 == False and loginA == 3:
      #print("You have had too many attempts")
      #sleep(1)
      #print("Please try again later")
     # sleep(1)
    #  print("Goodbye")
   #   exit()

def menu1pb():
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
    mainmenu()
  elif choice1 == 4:
    exit()
  
def menu1pa():

  choice = int(input("Do you want to:\n1) Login\n2) Register "))
  if choice == 1:
    login1P()
  elif choice == 2:
    register()
  else:
    print("Invalid input!")
    menu1pa()
  

def mainmenu():
  global multiplayer
  choice = int(input("1) 1 Player\n2) 2 Players\nChoice:  "))
  if choice == 1:
    menu1pa()
  elif choice == 2:
    #menu2p()
    print("\033[1;31;1mWIP")
    multiplayer = True


def register():

  print("Welcome to the registration screen!")
  print("Please enter your chosen username and password")
  sleep(1)
  username = input("Please choose your username: ")
  sleep(1)
  password = input("Please choose your password: ")
  sleep(1)
  row = [username, password] #creates a row to store the details
  reg = open("UsernamePassword.csv", "a", newline = '')#opens the files to save the details
  csvwriter = csv.writer(reg) #tells the program how to write (save) to the file
  csvwriter.writerow(row) #tells the program how to write to the file
  #csvwriter.writerow("")
  print("Welcome " + username + ". You have successfully registered")
  sleep(1)
  print("Please login now")
  sleep(1)
  reg.close() #closes the file.
  login1P()





#def resultsRound():

 # if point == 1:
  #  print("Unlucky. (2)")
  #elif point == 2:
  #  print("Meh. (2)")
  #elif point == 3:
  #  print("OK. (3)")
  #elif point == 4:
  #  print("Decent! (4)")
  #elif point == 5:
  #  print("Pretty good! (5)")
  #elif point == 6:
  #  print("PERFECT SCORE! (6)")



def game():
  """Player One Game"""
  global player1Total
  global cpuTotal
  global point1
  global point2
  global point
  global round
  global roll
  player1Total = 0
  cpuTotal = 0
  round = 1
  roll = 1
  print("ROUND" , round)
  print("PLAYER TURN")
  #rollChoice = ("Do you want to:\nplay it safe (spin)\nor take a risk (roll)? ")
  input("Press enter to roll the die ")
  sleep(1)
  point1 = random.randint(1,6)
  resultsRound()
  player1Total += point1
  point = 1
  point1 = point
  print("CPU TURN")
  sleep(1)
  cpupoint1 = random.randint(1,6)
  print("The CPU got" , cpupoint1)
  cpuTotal += cpupoint1
  print("PLAYER TURN")
  roll = 2
  rollChoice = ("Do you want to:\n1) play it safe (spin)\nor\n2) take a risk (roll)? ")
  if rollChoice == 1:
    lowerBound = point1 - 2
    upperBound = point1 + 2
    point2 = random.randint(lowerBound,upperBound)
    if point2 == 6:
      point2 = random.randint(4,5)
    else:
      point2 = point
      if point == 1:
        print("Unlucky. (2)")
      elif point == 2:
        print("Meh. (2)")
      elif point == 3:
        print("OK. (3)")
      elif point == 4:
        print("Decent! (4)")
      elif point == 5:
        print("Pretty good! (5)")
      elif point == 6:
        print("PERFECT SCORE! (6)")







  

#testing purposes
game()


