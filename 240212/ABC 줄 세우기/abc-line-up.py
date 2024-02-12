n = int(input())

lst = list(input().split())

# print(lst)

array = []
order = 0
count = 0
for i in range(65, 65 + n):
    for j in lst:
        if order == n-1:
            break
        if ord(j) == i:
            if lst.index(j) == order:
                # print("right")
                order +=1
                break
            else:
                # print("modify")
                count += 1
                order +=1
                break


print(count)
# array.sort()
# new_array = []
# for x in array:
#     new_array.append(chr(x))
# print(new_array)