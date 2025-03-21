class Animal:
    def sound(self):
        pass

class Bird(Animal):
    def sound(self):
        return "Chirp"    

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
Animals = [Bird(), Dog(), Cat()]

for a in Animals:
    # print(a.sound())
    # print("Animal says: ", a.sound())
    print(f"{a.__class__.__name__} says: {a.sound()}")