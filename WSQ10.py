x= 10
s=0
numbers = []
while x > 0:
    n = float(input("Write a number: "))
    numbers.append(n)
    x-=1
for i in numbers:
    s=s+i
print (("The total of the numbers is: ")+str(s))
l = len(numbers)
a = s/l
print (("The average is: ")+str(a))
