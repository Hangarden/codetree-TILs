n = int(input())

nums = list(map(int, input().split()))



# print(nums)

# 0 1 
# 2 3 
# 4 5
# 6 7 
# 8 9
count = 0
# print(nums, len(nums))
if len(nums) % 2 == 0:
    while len(nums) != 1:
        nums.sort()
        n = len(nums)
        new_nums = []
        for i in range(n//2): 
            new_nums.append((nums[2*i] + nums[2*i+1]))
            count += (nums[2*i] + nums[2*i+1])
        nums = new_nums
        # print(new_nums)
else:
    while len(nums) != 1:
        nums.sort()
        n = len(nums)
        new_nums = []
        for i in range(n//2):
            new_nums.append((nums[2*i] + nums[2*i+1]))
            count += (nums[2*i] + nums[2*i+1])
        if len(nums) % 2 == 1:
            new_nums.append(nums[-1])
        nums = new_nums

print(count)
# else:
#     while len(nums) == 1:
    
#         for i in range()



# n log n -> 100000 log 100000 -> 1000 = 2의 10  128 = 2^7  2의 17 제곱이 100000보다 크다 따라서 16 ~17사이 -> 1600000만정도
# 50000 log 5 * 10^4 -> 50000 * 13 14 700000
# 25000 log 25000 300000
# 12500 log 125000 170000
# 6250 log 6250 7,80000
# 31             30
#