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

playerWins = 0
cpuWins = 0
draws = 0
p1FinalTotal = 0
cpuFinalTotal = 0

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
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
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
      #loginA = loginA + 1
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
    username = input("Please enter your username, player 2: ")
    password = input("Please enter your password, player 2: ")
    for row in database:
      usernameF = row[0]
      passwordF = row[1]
      if (usernameF == username and passwordF == password):
        loggedin2 = True
        print("Welcome " + username + "!")
        sleep(1)
    if loggedin2 == False and loginA<4:
      print('Failed to sign in. Please try again...') 
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
  while True:
    try:
      choice = int(input("Do you want to:\n1) Login\n2) Register\nChoice: "))
    except ValueError:
      print("Try again!")
      continue
    else:
      break
  
  if choice == 1:
    login()
  elif choice == 2:
    register()
  else:
    print("Invalid input!")
    menu1pa()
  

def mainmenu():
  global multiplayer
  while True:
    try:
      choice = int(input("1) 1 Player\n2) 2 Players\nChoice:  "))
    except ValueError:
      print("Try again!")
      continue
    else:
      break


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
  global draws
  global cpuWins
  global playerWins
  global p1FinalTotal
  global cpuFinalTotal
  global round
  print("\n")
  print("\033[0;31;1mFINAL RESULTS!")
  if draws >= 3:
    print("\033[0;31;1mNO-ONE WINS!")
  elif cpuWins >= 3:
    print("\033[0;33;1mBETTER LUCK NEXT TIME. THE CHAMPION IS THE CPU!")
  elif playerWins >= 3:
    print("\033[0;34;1mYAY! YOU WIN!")
  print("\n")
  print("\033[0;34;1mYour final total is" , p1FinalTotal)
  print("\n")
  print("\033[0;33;1mThe CPU's final total is" , cpuFinalTotal)
  print("\n")
  print("\033[0;34;1mYou won " + str(playerWins) + " time(s).")
  print("\n")
  print("\033[0;33;1mThe CPU won " + str(cpuWins) + " time(s).")
  print("\n")
  print("\033[0;31;1mYou drew " + str(draws) + " time(s).")
  print("\n")
  choice12 = input("Do you want to play again? ")
  if choice12 == "Yes":
    round = 1
    playerWins = 0
    cpuWins = 0
    draws = 0
    p1FinalTotal = 0
    cpuFinalTotal = 0
    print("\033[2J")
    game()
  else:
    exit()



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
  global p1FinalTotal
  global cpuFinalTotal
  
  point = 0
  player1Total = 0
  cpuTotal = 0
 # pointlist = []
  roll = 1
  print("\n")
  print("\033[0;31;1mROUND" , round)
  print("\n")
  print("\033[0;34;1mPLAYER TURN")
  #rollChoice = ("Do you want to:\nplay it safe (spin)\nor take a risk (roll)? ")
  input("Press enter to roll the die ")
  sleep(0.5)
  point1 = random.randint(1,6)
  player1Total += point1
  point = point1
  resultsRoll()
  cpuroll = 1
  print("\n")
  sleep(0.5)
  print("\033[0;33;1mCPU TURN")
  sleep(0.5)
  cpupoint1 = random.randint(1,6)
  cpuTotal += cpupoint1
  print("The CPU got" , cpupoint1)
  print("Their total is" , cpuTotal)
  print("\n")
  print("\033[0;34;1mPLAYER TURN 2")
  input("Press enter to roll the die (Roll 2)")
  sleep(0.5)
  roll = 2
  
  point2 = random.randint(1,6)
  player1Total += point2
  point = point2
  resultsRoll()
  if point1 == point2:
    print("\n")
    print("You got two of the same in a row!")
    print("\033[0;34;1mPLAYER TURN 3!")
    input("Press enter to roll the die (Bonus Roll)")
    roll = 3
    point = random.randint(1,6)
    player1Total += point
    resultsRoll()
  print("\n")
  sleep(0.5)
  print("\033[0;33;1mCPU TURN 2")
  cpuroll = 2
  sleep(0.5)
  cpupoint2 = random.randint(1,6)
  cpuTotal += cpupoint2
  print("The CPU got" , cpupoint2)
  print("Their total is" , cpuTotal)
  if cpupoint1 == cpupoint2:
    print("\n")
    print("The CPU got two of the same numbers in a row!")
    sleep(0.5)
    print("\033[0;33;1mCPU TURN 3!")
    cpuroll = 3
    point = random.randint(1,6)
    cpuTotal += point
    sleep(0.5)
    print("The CPU got" , point)
    print("Their total is" , cpuTotal)
  print("\n")
  sleep(0.5)
  print("\033[0;31;1mROUND RESULTS!")
  sleep(0.5)
  print("\n")
  print("\033[0;34;1mPLAYER RESULTS:")
  sleep(0.5)
  p1FinalTotal += player1Total
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
  print("\n")
  sleep(0.5)
  print("\033[0;33;1mCPU RESULTS:")
  sleep(0.5)
  cpuFinalTotal += cpuTotal
  if cpuTotal % 2 == 0:
    print("The CPU's total is even!")
    cpuTotal += 10
    print("10 points have been added! Their round total is:" , cpuTotal)
  else:
    print("The CPU's total is odd!")
    cpuTotal -= 5
    if cpuTotal < 0:
      cpuTotal = 0
    print("5 points have been subtracted! Their round total is:" , cpuTotal)
  sleep(0.5)
  if cpuTotal == player1Total:
    print("\n")
    print("\033[0;31;1mTHIS ROUND WAS A DRAW!")
    draws += 1
    round += 1
    if round > 5:
      finalResults()
    else:
      game()
    # if round = 5 do final results
  elif player1Total > cpuTotal:
    print("\n")
    print("\033[0;34;1mYOU WIN THIS ROUND!")
    playerWins += 1
    round += 1
    if round > 5:
      finalResults()
    else:
      game()
  elif player1Total < cpuTotal:
    print("\n")
    print("\033[0;33;1mYOU LOST THIS ROUND!")
    cpuWins += 1
    round += 1
    if round > 5:
      finalResults()
    else:
      game()
  

          






  

#testing purposes
mainmenu()


