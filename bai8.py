def uoc(n):
    dem = 0
    for i in range(2,n):
        if(n%i==0):
            dem = dem +1
    return dem
def find(n):
    l = []
    for i in range(1,n):
        if(uoc(i)==1):
            l.append(i)
    return l
n = int(input("nhap n: "))
print(find(n))
