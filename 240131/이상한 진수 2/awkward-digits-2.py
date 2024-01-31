a = list(input())

def bit_sum(a):
    global max_val
    sums = 0
    for i in range(len(a)):

        if a[i] == '1':
            sums += 2**(len(a)-1-i)
    max_val = max(sums, max_val)

max_val = 0
for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        bit_sum(a)
        a[i] = '0'
    else:
        a[i] = '0'
        bit_sum(a)
        a[i] = '1'

print(max_val)