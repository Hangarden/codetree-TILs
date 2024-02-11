from collections import deque
# N개 밭의 높낲이 고르게 
# 높이를 낮추거나 높일 떄 비용은 1로 같다. 
# T번 이상 H높이로 나오도록 

# 3높이로 3번 이상 
# 6개 입력 연속해서니까 연속해서 몇개나 고를 수 있는지 
N, H, T = map(int, input().split())

lst = list(map(int, input().split()))
# T개씩 훑으면서 3가지 수와 H의 차이의 절댓값을 저장 한 뒤 최솟값을 갱신하도록 한다.
# q = deque(lst)
# T개씩 고르는 방법
temp = []
max_val = float('inf')
while lst: 

    temp.append(lst.pop(0))
    # print(temp)
    if len(temp) >= T:
        sums = 0 
        for i in temp:
            sums += abs(H - i)
        max_val = min(max_val, sums)
        temp.pop(0)

print(max_val)
    


# N, H 는 100까지
# T는 10까지


# 1 2 3

# 1
# 1
# 2
# 3
# 2
# 1 2 
# 2 3  
# 3  
# 1 2 3

# 4번쨰
# 1
# 2
# 3
# 4

# 1 2 
# 2 3
# 3 4

# 1 2 3
# 2 3 4

# 1 2 3 4
# 5번째
# 1 2
# 2 3
# 3 4
# 4 5