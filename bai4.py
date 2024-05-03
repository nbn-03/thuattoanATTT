import math
def check_snt(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2 ==0 or n%3==0:
        return False
    i = 5
    while i<=math.sqrt(n):
        if (n%i==0 or n%(i+2)==0):
            return False
        i = i +6
    return True

def find (a,b):
    dem = 0
    for i in range(a,b+1):
        if check_snt(i)==True:
            dem = dem +1
    return dem

a = int(input("nhap a: "))
b = int(input("nhap b: "))
print(find(a,b))
