def catalan(n):
    c = [1]
    for i in range(n):
        c.append(c[i] * c[n - i - 1])
    return c[n]


print(catalan(0))