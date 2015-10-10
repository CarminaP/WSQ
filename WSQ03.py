#The first two inputs ask the user for a number
x=int(input("Give me a number "))
y=int(input("Give me another number "))
#The first operation is assigned to a new variable
z=x+y
#The result is printed
print (str(x)+("+")+str(y)+("=")+str(z))
#Second operation and print
z=x-y
print (str(x)+("-")+str(y)+("=")+str(z))
#Third operation and print
z=x*y
print (str(x)+("x")+str(y)+("=")+str(z))
#Forth operation and print
z=x//y
print (str(x)+("/")+str(y)+("=")+str(z))
#Fifth and last operation and print
z=x%y
print (str(x)+("/")+str(y)+(" the reminder is ")+str(z))
