# 간단하게 i가 음수라면 그전까지를 체크 포인트로 저장해도 된다.

# 음수가 나타났는데 현재까지 합에서 음수를 더했을 때 양수라면 더 이상 연속하여 숫자 더하기를 중단하고 0으로 설정한다


#             4 -1   2 -19    3 6 9
#             4  3   5 -14->0 3 9 18
# 체크포인트   4 max(4,5)    





n = int(input())

numbers = list(map(int, input().split()))

current = 0
max_val = 0

if max(numbers) < 0:
    print(max(numbers))
else:
    for number in numbers:
        max_val = max(current, max_val)
        if number >= 0:
            current += number
        else:
            if current <= -number:
                
                current = 0
                continue
            current += number

    else:
        max_val = max(current, max_val)
        print(max_val)
    # print(current)
# print(max_val)