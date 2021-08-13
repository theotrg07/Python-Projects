import time

print("Welcome to my adventure game! In this game you will be trying to reach a castle to save your best friend.")

is_ready = input("Are you ready to play? yes/no ")
if is_ready.lower() == "yes":
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    
    if int(age) >= 18:
        print("Hello " + name + "!" )
        print("You are old enough to play!")

        ans = input("Alright.First choice.You see a road and you wanna go across but there are a lot of cars. Do you go across risking your life or wait for the cars to stop? across/wait ")
        if ans == 'wait':
            print("OK. Finally the cars stopped and you went across.")
            ans1 = input('You now see a dog and it seems very angry. You run or you try to calm it down? run/calm down ')
            if ans1 == 'run':
                print("Oof.. you are so lucky. The dog was so close to catch you. But you are still alive!")

                ans2 = input("You now see a thief robbing an ATM. You try to stop him or you call the police? stop him/call the police ")
                if ans2 == 'call the police':
                    print("The robber was caught because of you. Well done!")
                    ans3 = input("After walking for a while you see a big lake in front of you. You go around or across? around/across ")
                    if ans3 == 'around':
                        print("Well done! You reached the castle! You won!")
                        time.sleep(3)
                    
                    else:
                        print("Oh man... You are really unlucky. A shark just ate you...")
                        time.sleep(3)
                else:
                    print("The robber killed you and he left without leaving a single trace!")    
                    time.sleep(3)
            else:
                print("The dog bitted you and you lost...")
                time.sleep(3)

        else:
            print("Oops. A car hit you hard and you lost...")
            time.sleep(3)
    else:
        print("Sorry. You aren't old enough to play. ")
        time.sleep(3)

else:
    print("OK.Cyaa...")
    time.sleep(3)