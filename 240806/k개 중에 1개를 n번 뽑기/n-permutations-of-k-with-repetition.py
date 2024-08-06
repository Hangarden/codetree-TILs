K, N = map(int, input().split())

def recursion(lst, x):
    if x > N:
        print(*lst)
        return
    for i in range(1, K+1):
        recursion(lst + [i], x+1)

recursion([],1)