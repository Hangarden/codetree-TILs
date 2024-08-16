def check(i,j):
    if j==0 and 0< i < n-1: # 왼쪽 -> 오른쪽
        return [0]
    if i==0 and 0< j < n-1:
        return [3]
    if i==n-1 and 0< j < n-1:
        return [1]
    if j==n-1 and 0 < i < n-1:
        return [2]

    if i == 0 and j == 0:
        return [0,3]
    if i == (n-1) and j == 0:
        return [0,1]
    if i ==0 and j == (n-1):
        return [2,3]
    if i ==(n-1) and j == (n-1):
        return [1,2]

def throw(i,j, direction):
    count = 0
    while (0 <= i <= n-1 and 0 <= j <= n-1):
        i += dx[direction]
        j += dy[direction]
        count += 1
        if not (0 <= i <= n-1 and 0 <= j <= n-1):
            return count

        if maps[i][j] == 1:
            direction = abs(direction-5) % 4
        
        if maps[i][j] == 2:
            direction = abs(direction-3)

        
    return count

n = int(input())


maps = [list(map(int, input().split())) for _ in range(n)]

nums1 = [0, n-1]
# print(nums1)


dx = [0,-1,0,1]
dy = [1,0,-1,0]
max_val = -888


for i in nums1: # 0 4
    for j in nums1: # 0 4
        # print(i,j)
        direction = check(i,j)
        if len(direction) >= 2:
            
            # print(throw(i,j, direction[0]), [i,j])
            # print(throw(i,j, direction[1]), [i,j])
            max_val = max(max_val, throw(i,j, direction[0]))
            max_val = max(max_val, throw(i,j, direction[1]))
    
for i in nums1: # 0 4 
    for j in range(1,n-1):# 1 2 3
        direction = check(i,j)

        if len(direction) <= 1:
            # print(throw(i,j, direction[0]), [i,j])
            max_val = max(max_val, throw(i,j, direction[0]))

for i in range(1, n-1):
    for j in nums1:
        direction = check(i,j)

        if len(direction) <= 1:
            # print(throw(i,j, direction[0]), [i,j])
            max_val = max(max_val, throw(i,j, direction[0]))


print(max_val+1)