from time import sleep
from pynput.keyboard import Controller, Key
keyboard = Controller()

print('[1] Spam text from txt file\n[2] Spam text')
while True:
    try:
        option = int(input('please select an option: '))
        break
    except ValueError:
        print('Invalid input')
        sleep(0.2)


if option == 1:
    while True:
        try:
            wait = float(
                input('Enter how much time you want the program to wait before typing: '))
            file = input('Enter file name')
            txt_exists = file[-4:]
            if txt_exists == '.txt':
                pass

            else:
                file = str(file + str('.txt'))

            f = open(file, 'r')
            break
        except ValueError and FileNotFoundError:
            print('Invalid input')
            sleep(0.21)
    print('Program will start typing in 6 seconds')
    sleep(6)
    for word in f:
        keyboard.type(word)
        keyboard.press(Key.enter)
        sleep(wait)


elif option == 2:
    while True:
        try:
            message = input('Enter message: ')
            wait_time = float(input(
                'Enter how much time you want the program to wait between messages(note: must be above 0): '))
            if wait_time <= 0:
                raise ValueError
            repeat = int(
                input('Enter how many times you want to spam the message: '))
            break
        except ValueError:
            print('Invalid input')
    print('Program will start typing in 6 seconds')
    sleep(7)
    times_typed = 0
    while times_typed != repeat:
        times_typed += 1
        keyboard.type(message)
        keyboard.press(Key.enter)
        sleep(wait_time)
