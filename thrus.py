#class and object


class Person:
    #init ko kam initialize garne ho ...

    def __init__(self,name,age):
        self.name=name
        self.age=age


    #introduce vanne function create gareko
    def introduce(self):
        print(f"Hi my name is {self.name}.I am {self.age} years old.")


#object create gareko....
p=Person("bibek",16)
q=Person("naryan",90)


p.introduce()
q.introduce()


# what is front end development and backend development do research in youtube and google...

#how to become a full stack backend develeper in python....