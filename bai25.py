import math

def check_snt(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def list_snt(n):
    l = []
    for i in range(2, n):  # Bắt đầu từ 2 thay vì 1
        if check_snt(i):
            l.append(i)
    return l

def find(l, m, target, path, res):
    if target == 0 and len(path) == m:
        res.append(path)
        return
    if target < 0 or len(path) > m:
        return
    for i in range(len(l)):
        find(l[i:], m, target - l[i], path + [l[i]], res)

def solve(n, m):
    listRes = []
    listPr = list_snt(n)
    find(listPr, m, n, [], listRes)
    return listRes

def main():
    n = int(input("Nhập N: "))
    m = int(input("Nhập M: "))
    listRes = solve(n, m)
    if len(listRes) != 0:
        print(f"Các bộ {m} số nguyên tố thoả yêu cầu là:")
        for res in listRes:
            print(res)
    else:
        print(f"Không tìm thấy bộ {m} số nguyên tố thoả yêu cầu!!!")

if __name__ == "__main__":
    main()
