#*args

"""def total(*n):
    print((n))
total(1,2,3)   """ 


"""def total(*n):
    print(sum(n))
total(1,2,3)    
"""


"""def greetings(name,age):
    print(f"hello {name}  youre {age} years old")
greetings("ashwin",20) """

"""def greetings(**student):
    print(f"hello {student ["name"]} youre {student ["age"]} years old")
greetings(age=20,name="ashwin")"""



"""def sample(a,b):
    return a,b
c,b=sample(3,6)
print(c,b)"""

"""c=5
def sample():
    global c
    c=c+1
sample()    
print(c)
"""

"""def fun():
    print("hello")
    fun()    
fun()"""

def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print(fact(20))
