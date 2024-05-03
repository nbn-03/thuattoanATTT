import math
import random
def check_snt(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while i<=math.sqrt(n):
        if n%i ==0 or n%(i+2)==0:
            return False
        i = i+6
    return True

def tao_mang(n):
    l = []
    for i in range(0,n):
        l.append(random.randint(1,100))
    return l

def find(n):
    l = tao_mang(n)
    k = []
    for i in range(0,len(l)):
        if check_snt(i)==True:
            k.append(i)
    return k
n = int(input("nhap n: "))
print(find(n))
