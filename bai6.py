def uoc(n):
    p = 0
    for i in range(1,n):
        if n%i==0:
            p = p+i
    return p
def find(n):
    for i in range(1,n+1):
        p = uoc(i)
        if(p>i):
            a = uoc(p)
            if(a==i):
                print(f"{i}-{p}")
n = int(input("nhap n: "))
find(n)
