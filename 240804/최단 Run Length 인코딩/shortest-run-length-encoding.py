from collections import deque
string = input()

# print(string)
lst = list(string)
lst = deque(lst)

while (lst[0] == lst[-1]):
    x = lst.pop()
    lst.appendleft(x)

# print(list(lst))

answer = ""

initial = ""
count = 0
for i in lst:
    # print(i)
    if initial == "":
        initial = i
        count += 1
        continue
    
    if i == initial:
        count +=1
    else:
        answer += initial+str(count)
        initial = i
        count = 1

answer += initial + str(count)

print(len(answer))