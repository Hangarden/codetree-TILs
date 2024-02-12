import copy
n, m = map(int, input().split())

count = 0
for i in range(n,m+1):
    a = list(str(i))
    x = copy.deepcopy(a)
    x.reverse()
    if x == a:
        count += 1

print(count)