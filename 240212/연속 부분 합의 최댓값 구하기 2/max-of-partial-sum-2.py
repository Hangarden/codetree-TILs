n = int(input())

numbers = list(map(int, input().split()))

current = 0
max_val = 0
for number in numbers:
    # print(current)
    if current + number < 0:
        current = 0
        continue
    else:
        if current >= current + number:
            max_val = max(max_val, current)
        current += number

if current == max_val:
    print(max_val)
elif current < 0:
    print(min(numbers))
else:
    print(current)
# print(max_val)