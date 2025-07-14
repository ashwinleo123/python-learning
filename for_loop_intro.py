"""
#list
a=[10,22,40,45,6]
for f in a:
    print(f,end=" ")
"""
"""
#tuple
a=(19,39,45,66)
for f in a:
    print(f)
"""
"""
#string
name=("ashwin","jesin","shahid","leodas")
for f in name:
    print(f)
""" 
"""   
#set
a={12,34,56,78}
for f in a:
    print(f)
"""
"""
#dict
my_dict={"ashwin":23,45:23,"poli":34}
#for f,val in my_dict.items():
for f in my_dict:
    print(f,[my_dict])
"""
"""
a=(23,45,67,77,87)
print(tuple(enumerate (a)))
for c,k in enumerate(a):
    print(c,k)
"""

#print(list(range(4,27,3)))
num=int(input("enter your number:"))
for k in range(1,11):
    print(f"{k} * {num} = {k*num}")
 


#for num in range (1,17)
#   ifnum%2==0
#    print(num)
  

#num=int(input("enter your number"))
#for num in range(2,18):
#    if num%2==0:
#        print(num)
"""
fruits=("apple","banana","watermelon","pear","assam")
#for k in fruits:
#    if k.startswith("a"):
#       print(k)
for k in fruits:
    if k.lower()[0]=='a':
        print(k)
"""
"""
list=["aswhin","jesin","ebin","iran","shahid"]
vowels="a,e,i,o,u"
for k in list:
    if k.lower()[0] in "a,e,i,o,u":
        print(k)
"""
"""
for num in range(1,11):
    if num==4:
        continue
    print(num)
"""
"""
for num in range(1,11):
    if num==4:
        break
    print(num)     
"""
"""
for r in range(1,4):
    for j in range(1,r+1):
        print(j,end=" ")
    print(" ")          
"""

