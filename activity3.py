class Parrot:
    def __init__(self,name,age):
     self.age=age
     self.name=name
    def display(self):
       print("Name is",self.name)
       print("Age is",self.age)
Parrot1=Parrot('Kookaburra',7)
Parrot1.display()