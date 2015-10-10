x= int(input("Write the number you want the factorial of: "))
a= 1
y=x
if x == 0:
    print (("The factorial of ")+str(x)+(" is: 1"))
else:
    while x > 0:
        a=a*x
        x-=1
    print (("The factorial of ")+str(y)+(" is: ")+str(a))
