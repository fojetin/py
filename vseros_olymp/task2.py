from fractions import gcd as nod
a = int(input())
b = int(input())
c = int(input())
d = int(input())

def sravn(a,b,c,d):
    if b == d:
        if a < c:
            return 1
        else:
            return 0
    elif a == c:
        if b > d:
            return 1
        else:
            return 0
    else:
        if d*a < b*c:
            return 1
        else:
            return 0

count = 0
while sravn(a,b,c,d):
    a+=1
    b+=1
    count+=1
    a, b = a/nod(a,b), b/nod(a,b)
    

if a == c and b == d:
    print (count)
else:
    print (0)
