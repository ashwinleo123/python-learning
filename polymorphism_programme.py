#method overriding

class parent():
    def fun(self):
        print("hi")
class child(parent):        
    def fun(self):
        print("name:Ashwin")
a=child()
a.fun()  