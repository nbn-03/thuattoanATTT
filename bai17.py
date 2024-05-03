import math
def check_snt(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while i<=math.sqrt(n):
        if n%i==0 or n%(i+2)==0:
            return False
        i = i+6
    return True
def find(a,b,c):
    x = 1
    sum = a+b+c
    while(check_snt(sum)!=True):
        x = x+1
        sum = a*(x**2)+b*x+c
    print(x)
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
c = int(input("nhap so c: "))
find(a,b,c)
