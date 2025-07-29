"""class Laptops:
    def spec(self):
        self.RAM="16GB"
        self.model="HP INTEL CORE I5"
lap1=Laptops()        
lap1.spec()
print(lap1.model)"""


"""class Laptops:
    def spec(self,a,b):
        self.RAM=a
        self.model=b
lap1=Laptops()  
lap2=Laptops()      
lap1.spec("4GB","DELL")
lap2.spec("16GB","HP")
print(lap2.RAM)"""



"""class Laptops:
    owner="Ashwin"
    def __init__(self,a,b):
        self.RAM=a
        self.model=b
lap1=Laptops("4GB","DELL")  
lap2=Laptops("16GB","HP")      
print(lap1.model)
print(lap2.model)
print(Laptops.owner)"""



"""class Vehicle:
    def detail(self,m,model):
        self.make=m
        self.model=model
class Car(Vehicle):
    def __init__(self,c,p):
        self.color=c
        self.power=p
c1=Car(c="RED",p="151BHP")
c1.detail(m="2000",model="BMW")
print(c1.make)
print(c1.model)"""


"""class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=Person("zaman","zid")
x.printname()"""



#multiple inheritence
"""class Father:
    def skills(self):
        print("Father:reading,walking")
class Mother:
    def skills(self):
        print("Mother:cooking")            
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("child:football")
c=Child()
c.skills()"""


#multilevel inheritence
"""class Grandfather:
    def Grandfather(self):
        print("I AM THE GRAND FATHER")
class Father(Grandfather):
    def Father(self):
        print("I AM THE FATHER")
class Child(Father):
    def Child(self):
        print("I AM THE CHILD")
c=Child()
c.Grandfather()
c.Father()
c.Child()"""



#hierarchial inheritance using init
"""class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"name:{self.name}")
class Student(Person):
    def study(self):
        print(f"{self.name} is a student")
class Teacher(Person):
    def teach(self):
        print(f"{self.name} is a teacher")
s=Student("Ashwin")
s.display()
s.study()                                 
t=Teacher("jesin")
t.display()
t.teach()"""


#