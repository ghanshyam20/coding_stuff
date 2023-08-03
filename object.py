#oop concepts in python 
# c programming is  procedural programming language ho 


#python is  object oriented programming language...

# what is class in programming ??
# what is object in programming ???

#oop languages are  python,java, c#,ruby, c++,php,javascript,scala,kotlin,swift.



#class=blueprint ho !!


# euta class bata dherai wota object banauna sakinxa
#euta map bata dherai wota houses banauna sakinxa.....

#naksa=bluprint or class and houses=object
#euta class bata multiple object banauna sakinxa...


class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year


    def start_engine(self):
        return f"{self.make} {self.model} {self.year} engine started"
    


car1=Car("toyota","corolla",2020)
car2=Car("honda",'Civic',2021)


print(car1.make)
print(car2.model)

print(car1.start_engine())
print(car2.start_engine())










