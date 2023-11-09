class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I dont speak...")

class Cat(Pet):    
    def speak(self):
        print("Meow")


class Dog(Pet):    
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim",19)
p.show()

c = Cat("Abbey",5)
c.speak()

f = Fish("Goldy",1)
f.speak()




