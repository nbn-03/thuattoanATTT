#sủa code trong thuật toán
w=8
t=4
def find_array(n):
    l = []
    for i in range(t-1,-1,-1):
        l.append(n//pow(2,i*w))
        n = n % pow(2,i*w)
    return l
def find(a,b):
    l1 = find_array(a)
    l2 = find_array(b)
    l3 = []
    e = 0 
    for i in range(t-1,-1,-1):
        sum = l1[i]+l2[i]+e
        if(sum <pow(2,w)):
            l3.append(sum)
            e = 0
        else:
            l3.append(sum%pow(2,w))
            e = 1
    l3.reverse()
    return (e,l3)
def array_to_num(a,b):
    (e,l3) = find(a,b)
    sum = 0
    for i in range(0, len(l3)):
        sum = sum + l3[i]*pow(2,(len(l3)-1-i)*w)
    if e ==1 :
        return sum +pow(2,32)
    elif e==0:
        return sum
a = int(input("nhap a: "))
b = int(input("nhap b: "))
print(array_to_num(a,b))
