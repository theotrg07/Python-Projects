class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def walk(self):
        print(self.name,"is walking....")



    def speak(self):
        print("Hello, my name is ",self.name,"and I am ",self.age,"years old")



John = Person("John", 56)
Maria = Person("Maria", 53)



John.walk()
John.speak()

Maria.walk()
Maria.speak()
