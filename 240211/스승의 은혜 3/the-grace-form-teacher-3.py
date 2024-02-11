import sys
input = sys.stdin.readline

N, B = map(int, input().split())

gifts = [list(map(int, input().split())) for _ in range(N)]

# print(gifts)

# 인덱스 별로 가격//2 를 하고 나서 가격을 구한 뒤 costs에 넣고 max를 구한다.

# i이덱스를 제외하고는 그냥 a+b i인덱스라면 (a//2) + b)
max_val = 0
def max_gifts(N, B, gifts):
    global max_val
    for i in range(N):
        costs = []
        for j in range(N):
            if i == j:
                costs.append( (gifts[j][0] // 2) + gifts[j][1] )
            else:
                costs.append(gifts[j][0] + gifts[j][1])
        costs.sort()
        total = B
        count = 0
        for i in range(N):
            if B - costs[i] >=0:
                count += 1
                B -= costs[i]
            else:
                break

        max_val = max(max_val, count)

    return max_val

print(max_gifts(N, B, gifts))