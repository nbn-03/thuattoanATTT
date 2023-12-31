def failure(p): #Hàm tìm kích thước dài nhất của tiền tố p[0:j-1] sao cho bằng với hậu tố p[1:j-1] 
    f = [-1]
    for i in range(1,len(p)):# Duyệt độ dài chuỗi con của b
        count = 0
        for j in range(1,i): #duyệt các tiền tố và hậu tố trong chuỗi con
        	# Để hai chuỗi bằng nhau thì trước hết độ dài phải bằng nhau, nên ta chỉ xét những tiền tố và hậu tố cố độ dài bằng nhau trong chuỗi con
            if p[0:j] == p[i-j:i]: #Nếu tiền tố p[0:j] bằng hậu tố [i-j:i] (i-j vì để cho hai chuỗi nàu có độ dài bằng nhau và bằng j) 
                count = j
        f.append(count)
    return f
 
 
 
def Knuth_Morris_Pratt(p,T):
    f = failure(p)
    i=0
    j=0
    while(i<=(len(T)-len(p))):
        while (j<len(p)) and (p[j]==T[i+j]):
            j+=1
        if j == len(p):
            return i
        else:
            i = i+j-f[j]
            if f[j]==-1: j=0
            else: j = f[j]
    return -1
p = input("nhap p: ")
T = input("nhap T: ")
print(Knuth_Morris_Pratt(p,T))