class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade


    def display_intro(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.grade}")

if __name__=="__main__":
    student1=Student("bibek",16,"A") #object create gareko with the help of class Student.
    student2=Student("nature",20,"A")
    
#student1 and student2 object ho. we made these objects with the help of class name Student.
    print("Student 1:")
    student1.display_intro()

    #function call garda always (object.function_name) garinxa

    print("\nStudent 2:")
    student2.display_intro()



#features of classes in object oriented programming language.
#task to do 2mro  do some research on what is oop in python and what are its features.

#abstraction:data hiding
#encapsulation:classes allow you to bundle data together into single unit.
#inheritance:parent class ko feature child class ma acquire garne.
#polymorphism: one object have many features.
#attributes:classes allow to to define attributes(variables) that stores related data.
#methods:class vitra ko function lai method vaninxa.








