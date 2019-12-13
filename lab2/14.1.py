number_of_points = int(input())
recipe = []
for i in range(number_of_points):
    point = input()
    recipe.append(point) if 'лук' not in point else None
print(*recipe, sep=', ')