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
    for i in range(0,n):
        for j in range(0,i):
            if check_snt(j) ==True:
                if(i%j==0 and i%pow(j,2)==0):
                    print(i)

n = int(input("nhap so n: "))
find(n)
