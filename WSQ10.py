from statistics import *
x= 10
s=0
numbers = []
while x > 0:
    n = float(input("Write a number: "))
    numbers.append(n)
    x-=1
for i in numbers:
    suma += i
print (("The total of the numbers is: ")+str(s))

avrg = suma/len(numbers)
print (("The average is: ")+str(avrg))

stdev = pstdev(numbers)
print (("The standard deviation is: ")+str(stdev))
