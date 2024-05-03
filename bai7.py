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

def dao(n):
    l =[]
    while(n!=0):
        l.append(n%10)
        n = n//10
    a = 0
    for i in range(0,len(l)):
        a = a + l[i] * pow(10,len(l)-1-i)
    return a

def find(n):
    l = []
    for i in range(1,n):
        if(check_snt(i)==True and check_snt(dao(i))==True):
            l.append(i)
    return l
n = int(input("nhap n: "))
print(find(n))
