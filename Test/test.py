t = int(input())
lst = []

def findmax(n):
    k = 0
    while (1 << (k + 1)) <= n:
        k += 1
    return k

for i in range(t):
    lst.append(int(input()))

for i in lst:
    print(findmax(i))