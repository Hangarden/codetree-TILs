n = int(input())

nums = list(map(int, input().split()))

min_val = nums[0]
max_val = 0
for num in nums:
    if num < min_val:
        min_val = num
    else:
        max_val = max(max_val, num - min_val)

print(max_val)