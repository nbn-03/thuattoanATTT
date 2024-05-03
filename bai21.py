#sửa code trong thuật toán
import math
def check_snt(n):
    if n <=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while i<math.sqrt(n):
        if n%i==0 or n%(i+2)==0:
            return False
        i = i+6
    return True
def dem(n):
    dem = 0
    for i in range(1,n):
        if (check_snt(i)==True):
            dem = dem+1
    return dem

def find(a,b):
    d = 0
    for i in range(a,b+1):
        if check_snt(dem(i))==True:
            d = d +1
    print(d)
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
find(a,b)
