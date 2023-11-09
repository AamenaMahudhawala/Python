class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I dont speak...")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name},I am {self.age} years old,I am {self.color}.")


class Dog(Pet):    
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim",19)
p.show()

c = Cat("Abbey",5,"Orange")
c.speak()
c.show()

d = Dog('Bruno',3)
d.show()

f = Fish("Goldy",1)
f.speak()




