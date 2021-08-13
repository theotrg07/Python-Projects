import time
import pyautogui

message = input("Enter you message to spam: ")
repeat = int(input("How many times do you want to spam the message? "))

if repeat <= 0:
    print("You have to write how many times you want to spam the message man!")
    raise ValueError

wait_time = float(input(
    "How many seconds you want the program to wait between messages?(must be > 0) "))


if wait_time <= 0:
    print("Wait time must be above 0!")
    raise ValueError

print("Program will start typing in 5 seconds")

time.sleep(5)
pyautogui.typewrite(message)
times_typed = 0


while times_typed != repeat:
    times_typed += 1
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(wait_time)
