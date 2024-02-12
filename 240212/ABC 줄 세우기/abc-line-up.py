def bubble_sort(arr):
    n = len(arr)
    swap = 0

    for i in range(n):
       for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                continue
            else:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1

    return swap

n = int(input())
arr = list(input().split())

print(bubble_sort(arr))