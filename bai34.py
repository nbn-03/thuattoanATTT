import random 

def binary(n):
    list = []
    while(n>0):
        a = int(float(n%2))
        list.append(a)
        n = (n-a)/2
    return list
def nhanbpcl(a,k,n):
    list = binary(k)
    b = 1
    if k==0:
        return b
    else:
        A = a
        if(list[0]==1):
            b = a
        for i in range(1,len(list)):
            A = pow(A,2)%n
            if(list[i]==1):
                b = (A*b)%n
            else:
                b = b
        return b
def Fermat(n,t):
    for i in range(1, t+1):
        a = random.randint(2, n-2)
        r = nhanbpcl(a, n-1, n)
        if r != 1:
            return 'Hop so'
    return 'Nguyen to'

def main():
    n = int(input('Nhap vao so tu nhien n: '))
    t = int(input('Nhap va so lan lap t: '))
    print(n, "->", Fermat(n,t))
main()
