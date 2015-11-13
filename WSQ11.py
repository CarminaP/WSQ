def reverse(n):
    return int(str(n)[::-1])
def Lychrel(a,b):
    candidate = list(range(a,b))
    palindr = 0
    nonlych = 0
    lych = 0
    count = 0
    for i in candidate:
        if i == reverse(i):
            palindr += 1
        elif i[-1] == 0:
            palindr += 1
        else:
            q=i
            while q != reverse(q) and count != 30:
                q = q+reverse(q)
                if q == reverse(q):
                    nonlych += 1
                count +=1
            if q!=reverse(q) and count >= 30:
                lych+=1
    print(("Natural Palindromes: ")+str(palindr))
    print(("Non-Lychrels (become palindrome): ")+str(nonlych))
    print(("Lychrel candidates: ")+str(lych))

x = int(input("Write the lower bound of numbers to consider: "))
y = int(input("Write the upper bound of numbers to consider: "))

print("Calculating whether each value is one of: palindrome, non-lychrel or lychrel candidate")
print(("The results are from the range ")+str(x)+(" to ")+str(y))
Lychrel(x,y)
