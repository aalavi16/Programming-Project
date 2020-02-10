import time
import csv

print("Welcome to the registration screen!")
print("Please enter your chosen username and password")
time.sleep(1)
username = input("Please choose your username: ")
time.sleep(1)
password = input("Please choose your password: ")
time.sleep(1)
row = [username, password] #creates a row to store the details
reg = open("UsernamePassword.csv", "a", newline = '')#opens the files to save the details
csvwriter = csv.writer(reg) #tells the program how to write (save) to the file
csvwriter.writerow(row) #tells the program how to write to the file
csvwriter.writerow("\n")
print("Welcome " + username + ". You have successfully registered")
time.sleep(1)
print("Please login now")
time.sleep(1)
reg.close() #closes the file.
