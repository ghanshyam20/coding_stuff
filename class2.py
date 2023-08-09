#oop concept
#class is a blurprint=euta class ko help le dherai wota object banauna sakinxa.
#oop in python =task


class GFG:
    def __init__(self,name,company):
        self.name=name
        self.company=company


    def show(self):
        print(f"My name is {self.name} and  i am working at {self.company}")




q=GFG("nature","apple")
p=GFG("bibek","Google")
r=GFG("naryan","tesla")
q.show()
p.show()
r.show()

