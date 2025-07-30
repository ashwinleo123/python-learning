"""def decorator(fun):

    def wrapper():
        print("before printing")
        fun()
        print("after printing")
    return wrapper
@decorator
def greet():
    print("Hello,Developers")
greet()
"""

"""def subtract(a,b):
    a,b=b,a
    print(a-b)
subtract(10,20)    """



from datetime import date
today_date=date.today()
print("today's date:",today_date)

