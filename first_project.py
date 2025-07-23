tasks=[]
while True:
 print("==========TO DO LIST========= \n 1.add task \n 2.show task \n 3.mark task as done \n 4.exit")
 num=int(input("enter your choice:"))
 if num==1:
  num=int(input("how many task you want to add:"))
  print(num)
  tasks.append(num)
  for x in range(num+1):
    a=input("enter the task:")
    print(a)
    print("Task added")
 if num==2:
  print()

     
  
  

