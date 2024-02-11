def max_gifts(N, B, gifts):
    max_students = 0
    
    for i in range(N):
        # Calculate total cost when using coupon for the ith gift
        costs = [(p // 2 + s if i == j else p + s) for j, (p, s) in enumerate(gifts)]
        # print(costs)
        costs.sort()
        # print()
        # print(costs)

        total_cost = 0
        students = 0
        
        # Count how many students can receive gifts within the budget
        for cost in costs:
            if total_cost + cost <= B:
                total_cost += cost
                students += 1
            else:
                break
                
        max_students = max(max_students, students)
        
    return max_students 

N, B = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

# max_gifts(N,B,students)
print(max_gifts(N,B,students))