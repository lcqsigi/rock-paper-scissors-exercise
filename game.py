
import random

print("------------")

print("Welcome to rock, paper, and scissors")

print("------------")

#1 user input

user_input=input("Select 'rock', 'paper', or 'scissors': ")

valid_options = ["rock","paper","scissors"]


#2 validate user input

if user_input not in valid_options:
    print("Invalid option try again")
    exit() #quit()

print(f"You chose: '{user_input}' ")


#3 computer choice

computer_input=""

list1=['rock','paper','scissors']

computer_input=random.choice(list1)

print(f"Computer chose: '{computer_input}' ")


#4 determine the winner

if user_input == 'rock':
    num_user = 0
if user_input == 'paper':
    num_user = 1
if user_input == 'scissors':
    num_user = 2

if computer_input == 'rock':
    num_computer = 0
if computer_input == 'paper':
    num_computer = 1
if computer_input == 'scissors':
    num_computer = 2

#rock -- rock      0 0      --> draw
#rock -- paper     0 1      --> paper wins
#rock -- scissors  0 2      --> rock wins

#paper -- rock     1 0      --> paper wins
#paper -- paper    1 1      --> draw
#paper -- scissors 1 2      --> scissors win

#scissors -- rock     2 0   --> rock wins
#scissors -- paper    2 1   --> scissors win
#scissors -- scissors 2 2   --> draw


#5 display results

print("------------")

if num_user == num_computer:
    print("Result: Draw")

if (num_user == 0 and num_computer == 1) or (num_user == 1 and num_computer == 0):
    if num_user > num_computer:
        print("Result: You won")
    else:
        print("Result: Computer won")

if (num_user == 1 and num_computer == 2) or (num_user == 2 and num_computer == 1):
    if num_user > num_computer:
        print("Result: You won")
    else:
        print("Result: Computer won")

if (num_user == 0 and num_computer == 2) or (num_user == 2 and num_computer == 0):
    if num_user < num_computer:
        print("Result: You won")
    else:
        print("Result: Computer won")

print("------------")

#rock -- paper        0 1      --> paper wins
#paper -- rock        1 0      --> paper wins

#paper -- scissors    1 2      --> scissors win
#scissors -- paper    2 1      --> scissors win

#scissors -- rock     2 0      --> rock wins
#rock -- scissors     0 2      --> rock wins

#select rock, paper, or scissors: scissors
#you chose: 'scissors' 
#computer chose: 'rock' 
#you won
#computer won


#----
#Welcome player one...
#----
#Please choose either rock, paper, or scissors: rock
#You chose rock
#The computer chose paper
#----
#The computer won...
