"""
age=int(input("enter your age :"))

if  age>=18:
    print("eligible for voting")
    print("please get your voters id")
else:
    print("not eligible for voting")
    print("apply when youre 18")
"""
"""
name="ashwin"
a=list(name)
print(a)
a=set(name)
print(a)
a=tuple(name)
print(a)
"""
"""
my_dict={"name:ashwin"}
my_dict.clear()
print(my_dict)
"""
"""
my={"name":"ashwin","age":20}
my.update(age=30)
print(my)
"""
"""
a={"a":12,"b":13,"c":14}
a.setdefault("e",15)
print(a)
"""
#a=[12,13,45]
#print(a[-2])

"""
number=int(input("enter a number:"))
if  number %2==0:
    print("number is a even")    
else:
    print("number is a odd")    
"""
"""
year=int(input("enter a leap year :"))
if  (year%4==0 and year%100!=0 or year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
"""
"""
mark=int(input("enter your mark:"))
payment_status=True
if payment_status:
   if mark>50:   
      print("eligible for written exam")
   else:
       print("increase your module mark")
else:
    print("please pay your payment")
"""
"""
a=2
if a==1:
   print("a is one")
elif a==2:
     print("a is two")
elif a==3:
     print("not found")
"""
"""
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("1:addition \n 2:substraction \n 3:division \n 4:multiplication")
num3=int(input("please enter your choice:1,2,3,4:"))
if num3==1:
   print(num1+num2)
elif num3==2:
     print(num1-num2)
elif num3==3:
     print(num1*num2)
elif num3==4:
     print(num1/num2)
else:
     print("not found") 
"""   
"""                   
age=int(input("enter your age:"))
if age>=18:
    if age==18:
       print("This is your first voting have a nice voting")
    else:
        print("your eligible for voting")
else:
    print("your not eligilble for voting")            
 """
"""
distance=int(input("how many distance you want to travel(km) :"))
if distance==1:
   print("only 1kms just walk dear")
elif distance==2:
     print("travel by bike or take a bus")
elif distance>10 and distance<20:
     print("take a bus")
elif distance>4 and distance<50:
     print("travel by train or plain")
elif distance>=10000:
     print("ask nadhil")
else:
     print("please sit at your home")
     
"""


#python is a case sensitive language
name=("ashwin")
print(name.capitalize())


#aswhin is a good boy