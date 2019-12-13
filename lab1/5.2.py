current_stones = 1
goal_stones = int(input())
steps = 0
while current_stones * 2 < goal_stones:
    steps += 1
    current_stones *= 2
while current_stones != goal_stones:
    steps += 1
    current_stones += 1
print(steps)