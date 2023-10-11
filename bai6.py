import math
import time
a = time.time()
def uoc(n):
    a = 0
    for i in range (1,n):
        if(n%i==0):
           a = a + i
    return a
def kt(n):
    list = []
    for i in range (2,n):
        a = uoc(i)
        if(a>i):
            b = uoc(a)
            if(b==i):
               list.append(i)
               list.append(a) 
    print(list)
n = int(input('Nhap vao so n: '))
kt(n)
print(time.time()-a)