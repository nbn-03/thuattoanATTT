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
        if(n%i== 0 or n%(i+2)==0):
            return False
        i= i+6
    return True

def find(n):
    l = []
    for i in range(1,n+1):
        if(check_snt(i)==True):
            l.append(i)
    for i in range(0,len(l)):
        for j in range(i, len(l)):
            if(check_snt(l[i]+l[j])==True and check_snt(l[j]-l[i])==True):
                print(f"{l[i]}-{l[j]}")
n = int(input("nhap n: "))
find(n)
