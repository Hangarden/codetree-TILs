import heapq
n = int(input())

lst = list(map(int, input().split()))
lst.sort()
# print(lst)

option1 = lst[-1] * lst[-2] * lst[-3]
option2 = lst[0] * lst[1] * lst[-1]

print(max(option1, option2))
# minus = []
# plus = []

# for x in lst:
#     if x >= 0:
#         heapq.heappush(plus, x)
#     else:
#         heapq.heappush(minus, x)
# plus.sort(reverse = True)
# print(plus)
# print(minus)
# array = []
# for x in lst:
#     abs_x = abs(x)
#     array.append((abs_x,x))
# array.sort(reverse= True)
# print(array)