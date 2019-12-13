def solve(*coefficients):
    if len(coefficients) > 3:
        return None
    a = None
    b = None
    c = None
    try:
        a, b, c = coefficients
    except ValueError:
        try:
            a, b = coefficients
        except ValueError:
            a = coefficients
    if a is not None and b is not None and c is not None:
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
    elif a is not None and b is not None:
        return [-b / a]
    elif a is not None:
        return ['all']
    else:
        return None


print(sorted(solve(1, 2)))