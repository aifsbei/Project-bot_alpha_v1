def roots_of_quadratic_equation(a, b, c):
    if a == 0 and b == 0:
        return ['all']
    try:
        x1 = (-b - (((b ** 2) - 4 * a * c) ** (1 / 2))) / (2 * a)
        x2 = (-b + (((b ** 2) - 4 * a * c) ** (1 / 2))) / (2 * a)
    except:
        return []
    if x1 == x2:
        return [x1]
    else:
        return [x1, x2]


result = roots_of_quadratic_equation(1, -3, 2)
print(*sorted(result))