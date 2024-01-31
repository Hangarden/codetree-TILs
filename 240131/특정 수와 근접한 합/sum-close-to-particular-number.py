import copy

n, target = map(int, input().split())

lst = list(map(int, input().split()))
max_val = float('inf')
visited = [False] * n
def back(lst, n):
    global max_val
    if n == 2:
        max_val = min(max_val, abs(sum(lst) - target) )
        return
    
    for i in range(len(lst)):
        if not visited[i]:
            visited[i] = True
            x = copy.deepcopy(lst[i])
            lst[i] = 0
            back(lst, n+1)
            lst[i] = x
            visited[i] = False

back(lst, 0)

print(max_val)
# N, S = map(int, input().split())

# lst = list(map(int, input().split()))



# lst.sort()

# def binary_search(target, lst):
#     start = 0
#     end = len(lst) -1


#     while start <= end:
#         mid = (start + end) // 2
#         if lst[mid] == target:
#             return mid

#         else:
#             if lst[mid] >= target:
#                 end = mid -1
#             else:
#                 start = mid + 1
#     else:
#         return start

# # print(binary_search(0, len(lst), find_value))

# for i in range(2):
#     sums = sum(lst)
#     find_value = (sums - S)//(2-i)
#     x = binary_search(find_value, lst)
#     if x >= len(lst):
#         x -=1
#     lst.pop(x)

# print(sum(lst) - S)










# lst.sort()

# def binary_search(target, lst):
#     start = 0
#     end = len(lst) -1


#     while start <= end:
#         mid = (start + end) // 2
#         if lst[mid] == target:
#             return mid

#         else:
#             if lst[mid] >= target:
#                 end = mid -1
#             else:
#                 start = mid + 1
#     else:
#         return start

# # print(binary_search(0, len(lst), find_value))

# for i in range(2):
#     sums = sum(lst)
#     find_value = (sums - S)//(2-i)
#     x = binary_search(find_value, lst)
#     if x >= len(lst):
#         x -=1
#     lst.pop(x)

# print(sum(lst) - S)