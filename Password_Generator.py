import random

s = "qwertyuiopasdfghjklzxcvbnm.,()-_"

passlen = 8


p = "".join(random.sample(s, passlen))

print("Your password is:",p)