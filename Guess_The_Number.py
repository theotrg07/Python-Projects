# Guess the number game in Python 3.8.6 (in vs code)

import time
import random


random_number = random.randint(1, 10)
health = 10

print(
    "Welcome to the game called 'Guess the number'. In this game you have to guess the right number between 1 and 10. You have 5 chances to guess the right number. The number you have to guess is not decimal"
)

name = input("What is your name? ")
age = input("How old are you?  ")
if int(age) < 10:
    print("Sorry. You are not old enough to play this game.")
    time.sleep(3)
    exit()

print("Hello " + name + "!")
print("You are old enough to play.")

is_ready = input("Are you ready to play? Yes or No? ")
if is_ready.lower() != "yes":
    print("OK. Cyaaa....")
    time.sleep(3)
    exit()

print("Lets play!")
while True:
    guess = input("Enter your guess: ")
    if int(guess) < int(random_number):
        print("The right number is even higher.Try again")
        health -= 2

    elif int(guess) > int(random_number):
        print("The right number is even lower. Try again ")
        health -= 2

    elif int(guess) == int(random_number):
        print("You won! The right number is " + guess)
        break

    if health <= 0:
        print("Game over...You are out of attempts! ")
        break

time.sleep(3)
