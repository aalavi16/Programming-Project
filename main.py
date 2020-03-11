from time import sleep
import random
import csv
import os 
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
def viewLeaderboard():
  see = open("highscores.csv","r")
  highscores = csv.reader(see,delimiter=',')
  count = 0
  i = 0
  highscores1 = []
  usernames2 = []
  highscores3 = []
  for row in highscores:
    highscores1.append([row[0],row[1]])
    i = i + 1
    usernames2.append(row[0])
    highscores3.append(row[1])
  highScores2 = sorted(highscores1, key=lambda data:data[1])
  print(highScores2)
  zipScores = zip(usernames2, highscores3)
  highscoresdict = dict(zipScores)
  print(highscoresdict)
  menu1pb()
  #could create a dictionary instead with key value pairs for username / score respectively


def login():
  global round
  global username
  global password
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
        break
        


    if loggedin1 == False and loginA<4:
      print('Failed to sign in. Please try again') 
      #loginA = loginA + 1
      login()
    elif loggedin1 == True:
      print("Welcome " + username + "!")
      sleep(1)
      round = 1
      
      if multiplayer == True:
        login2P()
      else:
        menu1pb()
      #game()
    #elif loggedin1 == False and loginA == 3:
    #  print("You have had too many attempts")
     # sleep(1)
      #print("Please try again later")
      #sleep(1)
     # print("Goodbye")
     # exit()

def login2P():
  global username2
  global loginA
  check = open('UsernamePassword.csv','r')
  database = csv.reader(check,delimiter=',')
  loggedin2 = False
  while loggedin2==False:
    username2 = input("Please enter your username, player 2: ")
    password2 = input("Please enter your password, player 2: ")
    for row in database:
      usernameF = row[0]
      passwordF = row[1]
      if (usernameF == username2 and passwordF == password2):
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
  global round
  while True:
    try:
      choice1 = int(input("1) Play Against CPU\n2) View Leaderboard\n3) Exit to Main Menu\n4) Exit Game\nChoice: "))
    except ValueError:
      print("Try again!")
      continue
    else:
      break
  while choice1 < 1 or choice1 > 4:
    choice1 = input("Invalid input! ")
  if choice1 == 1:
    round = 1
    sleep(0.5)
    #print("\033[2J")
    os.system("clear")
    game()
  elif choice1 == 2:
    #Leaderboard
    viewLeaderboard()
  elif choice1 == 3:
    mainmenu()
  elif choice1 == 4:
    exit()
  
def menu1pa():
  """2nd menu asking whether to login or register."""
  while True:
    try:
      choicep1 = int(input("Do you want to:\n1) Login\n2) Register\nChoice: "))
    except ValueError:
      print("Try again!")
      continue
    else:
      break
  
  if choicep1 == 1:
    login()
  elif choicep1 == 2:
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
    #menu2pa()
    print("\033[1;31;1mWIP")
    multiplayer = True
    #mainmenu()



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
  print("\033[0;31;1mPRESS ENTER TO VIEW FINAL RESULTS!")
  if draws >= 3 or cpuWins == playerWins:
    print("\033[0;31;1mNO-ONE WINS!")
  elif cpuWins >= 3 or (draws < 3 and cpuWins > playerWins):
    print("\033[0;33;1mBETTER LUCK NEXT TIME. THE CHAMPION IS THE CPU!")
  elif playerWins >= 3 or (draws < 3 and playerWins > cpuWins):
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
  choice = input("Do you want to save your score? ")
  if choice == "Yes":
    row = [username, p1FinalTotal] #creates a row to store the details
    save = open("highscores.csv", "a", newline = '')#opens the files to save the details
    csvwriter = csv.writer(save) #tells the program how to write (save) to the file
    csvwriter.writerow(row) #tells the program how to write to the file
    save.close()


  choice12 = input("Do you want to play again? ")
  if choice12 == "Yes":
    round = 1
    playerWins = 0
    cpuWins = 0
    draws = 0
    p1FinalTotal = 0
    cpuFinalTotal = 0
    #print("\033[2J")
    os.system("clear") #clear screen
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
  sleep(1)
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
    print("YOU GOT TWO OF THE SAME IN A ROW!")
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
    print("THE CPU GOT TWO OF THE SAME NUMBERS IN A ROW!")
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
  input("\033[0;31;1mPRESS ENTER TO VIEW ROUND RESULTS!")
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
  

mainmenu()






  

#testing purposes
#viewLeaderboard()


