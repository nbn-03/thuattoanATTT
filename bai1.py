import math
def uoc(n):
    dem = 0
    for i in range(2,n):
        if(n%i==0):
            dem = dem + 1
    return dem

def Q_prime(n):
    l = []
    for i in range(1,n+1):
        if(uoc(i)==2):
            l.append(i)
    return l

n = int(input("nhap n: "))
print(Q_prime(n))

 
