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




score = 0
highscore = 0
username = ''
life = 3
loginA = 0
def login():
  global round

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

        if multiplayer == True:
          login2P()
    if loggedin1 == False and loginA<4:
      print('Failed to sign in. Please try again') 
      loginA = loginA + 1
      login()
    elif loggedin1 == True:
      sleep(1)
      round = 1
      
      
      
      game()
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
    login()
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
  login()

def finalResults():
  print("FINAL RESULTS!")
  if draws == 5:
    print("NO-ONE WINS!")
  if cpuTotal > player1Total:
    print("BETTER LUCK NEXT TIME. THE WORLD CHAMPION IS THE CPU!")
  elif player1Total:
    print("YAY! YOU WIN!")


def resultsRoll():
  if point == 1:
    print("Unlucky. (1)")
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
  print("Your current total is: " + str(player1Total))




def game():
  global round
  global point
  global player1Total
  global cpuTotal
  global point1
  global point2
  global username
  global loginA
  global cpuWins
  global playerWins
  global draws
  """Player One Game"""
  global roll
  point = 0
  player1Total = 0
  cpuTotal = 0
 # pointlist = []
  roll = 1
  print("ROUND" , round)
  print("PLAYER TURN")
  #rollChoice = ("Do you want to:\nplay it safe (spin)\nor take a risk (roll)? ")
  input("Press enter to roll the die ")
  sleep(1)
  point1 = random.randint(1,6)
  player1Total += point1
  point = point1
  resultsRoll()
  cpuroll = 1
  print("CPU TURN")
  sleep(1)
  cpupoint1 = random.randint(1,6)
  cpuTotal += cpupoint1
  print("The CPU got" , cpupoint1)
  print("Their total is" , cpuTotal)
  print("PLAYER TURN 2")
  input("Press enter to roll the die (Roll 2)")
  sleep(1)
  roll = 2
  
  point2 = random.randint(1,6)
  player1Total += point2
  point = point2
  resultsRoll()
  if point1 == point2:
    print("You got two of the same in a row!")
    print("PLAYER TURN 3!")
    roll = 3
    point = random.randint(1,6)
    player1Total += point
    resultsRoll()
  print("CPU TURN 2")
  cpuroll = 2
  sleep(1)
  cpupoint2 = random.randint(1,6)
  cpuTotal += cpupoint2
  print("The CPU got" , cpupoint2)
  print("Their total is" , cpuTotal)
  if cpupoint1 == cpupoint2:
    print("The CPU got two of the same numbers in a row!")
    print("CPU TURN 3!")
    cpuroll = 3
    point = random.randint(1,6)
    cpuTotal += point
    print("The CPU got" , point)
    print("Their total is" , cpuTotal)
  print("ROUND RESULTS!")
  print("PLAYER RESULTS:")
  if player1Total % 2 == 0:
    print("Your total is even!")
    player1Total += 10
    print("10 points have been added! Your round total is:" , player1Total)
  else:
    print("UNLUCKY! Your total is odd!")
    player1Total -= 5
    if player1Total < 0:
      player1Total = 0
    print("5 points have been subtracted! Your round total is:" , player1Total)
  print("CPU RESULTS:")
  if cpuTotal % 2 == 0:
    print("The CPU's total is even!")
    cpuTotal += 10
    print("10 points have been added! Their round total is:" , cpuTotal)
  else:
    print("The CPU's total is odd!")
    player1Total -= 5
    if player1Total < 0:
      player1Total = 0
    print("5 points have been subtracted! Their round total is:" , cpuTotal)
  if cpuTotal == player1Total:
    print("THIS ROUND WAS A DRAW!")
    draws = 1
    round += 1
    game()
    # if round = 5 do final results
  elif player1Total > cpuTotal:
    print("YOU WIN THIS ROUND!")
    playerWins = 1
    round += 1
    game()
  elif cpuTotal > player1Total:
    print("YOU LOST THIS ROUND!")
    cpuWins = 1
    round += 1
    game()
  

          






  

#testing purposes
mainmenu()


