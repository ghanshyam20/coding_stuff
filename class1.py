# class Superclass:
#     #some code will be here



# class Childclass(Superclass):
    #some code of child class will be here 

#this is the parent class
class Animal:
    def __init__(self,species):
        self.species=species



    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self,name):
        super().__init__("Dog")
        self.name=name


    def make_sound(self):
        return "woof"
    


class Cat(Animal):
    def __init__(self,name):
        super().__init__("Cat")
        self.name=name


    def make_soud(self):
        return "Meow"
    


d=Dog("Budddy")
c=Cat("cutie")

print(d.species)
print(d.name)
print(d.make_sound())

print(c.species)
print(c.name)
print(c.make_sound())













