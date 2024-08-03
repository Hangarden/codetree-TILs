n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_sum = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def find_max_sum(x, y, sum):
    global max_sum
    
    # 도착 지점에 도착하면 최대 합을 갱신해줍니다.
    if x == n - 1 and y == n - 1:
        max_sum = max(max_sum, sum)
        return
    
    dxs, dys = [1, 0], [0, 1]
    
    # 가능한 모든 방향에 대해 탐색해줍니다.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if in_range(new_x, new_y):
            find_max_sum(new_x, new_y, sum + grid[new_x][new_y])
                         
                    
find_max_sum(0, 0, grid[0][0])
print(max_sum)