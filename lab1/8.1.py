rows = int(input())
cols = int(input())
current = 0
matrix = [(j + 1) / (i + 1) for i in range(cols) for j in range(rows)]
for i in range(cols):
    for j in range(rows):
        print("%.2f" % matrix[current], ' ', end='')
        current += 1
    print('\n')