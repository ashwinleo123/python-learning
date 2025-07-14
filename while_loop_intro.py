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

   

