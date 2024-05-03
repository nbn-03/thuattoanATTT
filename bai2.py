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

def find(n):
    for i in range(pow(10,n-1),pow(10,n)):
        if check_snt(i) == True: 
            print(i)
n = int(input("nhap n: "))
find(n)
