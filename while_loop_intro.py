"""
count=1
while count<=10:
    print(count)
    count=count+1
"""
"""
num=int(input("enter your number:"))
count=1
while count<=9:
    print(f"{num} * {count} = {num*count}")
    count=count+1
"""
"""
num=int(input("enter your number:"))
f=count=1
while count<=num:
    f=f*count
    count+=1
print(f) 
"""
"""
while True:
 num=int(input("enter your number:"))
 numb=int(input("enter your second number:"))
 print("1:addition \n 2:multiplication \n 3:division \n 4:modules \n 5:substraction")
 num2=int(input("enetr your chioce 1,2,3,4,5:"))
 if num2==1:
    print(num+numb)
 elif num2==2:
    print(num*numb)
 elif num2==3:
    print(num/numb)
 elif num2==4:
    print(num%numb) 
 elif num2==5:
    print(num-numb)
 else:
    print("please enter a valid input from choice given")
 str=input("do you want to continue(yes/no):")
 if str.lower()!="yes":
    break
"""
"""
for x in range(1,26,2):
   print(x,end=" ")   
print(" ")   
"""
"""
for x in range(1,5):
   print("* "*x)
"""   
"""
for r in range(1,6):
    for sp in range(5-r):
        print(" ",end="")
    for st in range(r):
        print("*",end="")
    print("")   
"""

"""
for x in range(1,6):
    print(" "*int(5-x),"*"*x)
"""   

"""
for x in range(5,0,-1):
     for r in range(1,x+1):
         print("*",end=" ")
     print() 
"""     



"""
for x in range(1,5):
    for r in range(1,x+1):
        print(x*r,end=" ")
    print()
"""


 