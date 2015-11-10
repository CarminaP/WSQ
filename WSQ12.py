def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def GCD(x,y):
    while y != 0:
        z = y
        y = x % y
        x = z
    return x
def GcD(q,w):
    while q != w:
        if q > w:
            q = q - w
        else:
            w = w - q
    return q
num1 = int(input("Write an integer number:"))
num2 = int(input("Write another integer number:"))
print (("The greatest common denominator of ")+str(num1)+(" and ")+str(num2)+(" is: ")+str(gcd(num1,num2)))
print (("The greatest common denominator of ")+str(num1)+(" and ")+str(num2)+(" is: ")+str(GCD(num1,num2)))
print (("The greatest common denominator of ")+str(num1)+(" and ")+str(num2)+(" is: ")+str(GcD(num1,num2)))
