import math
def check_snt(n):
    if n<=1:
        return False
    elif n <=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5 
    while i <= math.sqrt(n):
        if n%i==0 or n%(i+2)==0:
            return False
        i = i +6
    return True
def uoc(n):
    l = []
    for i in range(1,n+1):
        if n%i ==0:
            l.append(i)
    k =0
    q = 0
    for i in l:
        if check_snt(i) ==True:
            k = k + 1
            q = q + i
    key = n + len(l) + sum(l) - k - q
    return key
n = int(input("nhap n: "))
print(uoc(n))
