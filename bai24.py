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
def tao_mang(n):
    return [i**2 for i in range(0,n)]
def find(a,b):
    s1 = tao_mang(b)
    s2 = tao_mang(b)
    for i in range(a,b+1):
        if(check_snt(i)==True):
            for k in range(0,len(s1)):
                for l in range(k,len(s2)):
                    if(s1[k]+s2[l]==i):
                        print(i) 

a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
find(a,b)
