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


# global keyward
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


# recurssion
"""def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print(fact(5))"""


# reverse recurssion
"""def Rev(s):
    if len(s)==0:
        return s
    else:
        return Rev(s[1:])+s[0]
print(Rev("ashwin"))"""


"""odds=[k for k in range(1,18) if k%2==1]
print(odds)
evens=[k for k in range(1,17) if k%2==0]
print(evens)"""

#lambda
"""v=lambda a,b=0:a+b
print(v(5))"""

"""is_even=lambda num:True if num%2==0 else False
print(is_even(7))
"""
"""is_even=lambda num:f"{num} is even" if num%2==0 else f"{num} is odd"
print(is_even(3))"""


"""is_even=lambda num:f"{num} is even" if num%2==0 else f"{num} is odd"
a=int(input("enter your number :"))
print(is_even(a))"""

"""def squares(num):
    return num**2
number=[1,3,4,7]
print(set(map(squares,number)))"""

"""numbers=[1,3,4,5]
print(list(map(lambda x:x**2, numbers)))"""