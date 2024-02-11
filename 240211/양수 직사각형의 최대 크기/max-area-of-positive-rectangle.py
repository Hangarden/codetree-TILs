n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
def max_positive_rectangle(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_area = -1

    # Step 1: Calculate the height of positive numbers up to each row
    height = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                height[i][j] = height[i-1][j] + 1 if i > 0 else 1

    # Step 2: Find the maximum rectangle in each row's histogram
    for row in height:
        stack = []
        for i in range(m + 1):
            h = row[i] if i < m else 0
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

    return max_area if max_area != -1 else -1

print(max_positive_rectangle(matrix))