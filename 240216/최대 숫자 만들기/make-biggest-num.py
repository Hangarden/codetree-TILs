from functools import cmp_to_key

# # custom comparator를 직접 정의
# # x가 앞에 있는 숫자, y가 뒤에 있는 숫자 가정했을 때
# # 이 순서가 우리가 원하는 순서라면 0보다 작은 값을, 
# # 반대라면 0보다 큰 값을
# # 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
# # 보통 반환값에 1, -1, 0을 사용합니다.
def compare(x, y):
    # x가 y보다 크다면
    # 우리가 원하는 방향입니다.
    x = str(x)
    y = str(y)
    x = x * 11
    y = y * 11
    # print(x, y)
    for i in range(11):
        if int(x[i]) > int(y[i]):
            return -1
        if int(x[i]) < int(y[i]):
            return 1
        
        continue
    
# arr = [41, 22, 85, 53, 9]
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
# # 내림차순 정렬
arr.sort(key=cmp_to_key(compare))
# print(arr)
output = ""
for i in arr:
    output += str(i)
print(output)
# print(*arr, end = "")
# for elem in arr: # 정렬 이후의 결과 출력
#     print(elem, end=" ")

# # >> 9 8 5 4 2
# x, y = 433, 4333
# x = str(x)
# y = str(y)
# x = x * 9
# y = y * 9
# print(x, y)