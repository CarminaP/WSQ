import math

def calculate_e (precision):
    suma = 0
    for i in range(0, precision+1):
        num = float(math.factorial(i))
        suma += float(1/num)
    return round(suma, precision)

a = int(input("Write the number of decimal points of accuracy: "))
print(("The value of e is: ")+str(calculate_e(a)))
