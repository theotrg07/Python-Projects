class Robot:
    def __init__(self, name, color, weight):
        self.name = name 
        self.color = color 
        self.weight = weight
        
    def introduce_self(self):
        print("My name is ", self.name)
        print("I am ",self.color)
        print("I am ",self.weight,"kilos")

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()