#sửa code trong thuật toán
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
def chuyen(n):
    if check_snt(n)==True:
        return n
    elif check_snt(n)==False:
        return 0
def find(l,r):
    sum = 0
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            sum = sum + chuyen(i)*chuyen(j)
    return sum
print('Nhap vao khoang [L, R]: ')
l = int(input("Nhap vao gia tri L: "))
r = int(input('Nhap vao gia tri R: '))
print(find(l,r))
            
