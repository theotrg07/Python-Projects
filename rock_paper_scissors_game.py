#Rock paper scissor's game in python (vs code)

import time
import random

moves = ["rock", "paper", "scissors"]


attempts = 3
wins = 0




print("Welcome to the game called 'Rock Paper Scissors'. In this game" 
" you have to win three rounds to win the game. But be careful! You have only 3 attempts!")


is_ready = input("Are you ready to play?  yes/no  ")
if is_ready.lower() != 'yes':
    print("OK. Have a good timee....")
    time.sleep(3)
    exit()
   

print("Lets play!")

name = input("What is your name? ")
age = input("How old are you? ")

if int(age) < 10:
    print("Sorry. You are not old enough to play this game... Try after a few years...")
    time.sleep(3)
    exit()
    

print("Hello",name,"!")
print("It seems like you are old enough to play!")



def win():
    print("THE GAME: You win")


def lost():
    print("THE GAME: You lost")


def draw():
    print("THE GAME: Its a draw")


while True:
    ans = input(str("Choose your move. Rock, paper or scissors?   (rock/paper/scissors)  ")).lower()
    computer_move = random.choice(moves)
    print("You: " + ans)
    print(" Computer: " + computer_move)

    if ans == computer_move:
        draw()
        print("Score: ", wins)
        print("Attempts left: ", attempts)
    
    
    elif ans == 'rock' and computer_move == 'scissors':
        win()
        wins += 1
        print("Score: ", wins)
        print("Attempts left: ", attempts)
    
    elif ans == 'rock' and computer_move == 'paper':
        lost()
        attempts -=1
        print("Score: ", wins)
        print("Attempts left: ", attempts)

    

    elif ans == 'paper' and computer_move == 'rock':
        win()
        wins += 1
        print("Score: ", wins)
        print("Attempts left: ", attempts)

    elif ans == 'paper' and computer_move == 'scissor':
        lost()
        attempts -=1
        print("Score: ", wins)
        print("Attempts left: ", attempts)

    

    elif ans == 'scissors' and computer_move == 'paper':
        win()
        wins += 1
        print("Score: ", wins)
        print("Attempts left: ", attempts)
    
    elif ans == 'scissors' and computer_move == 'rock':
        lost()
        attempts -=1
        print("Score: ", wins)
        print("Attempts left: ", attempts)

    

    else:
        attempts -=1
        print("False answer! You have", attempts,"attempts left !")
        print("Score: ", wins)
        print("Attempts left: ", attempts)



    if  int(wins) == 3:
        print("Well done! You won the game!")
        time.sleep(4)
        exit()
        


    elif int(attempts) <= 0:
        print("Game Over! Out of attempts....")
        time.sleep(4)
        exit()
        
    






