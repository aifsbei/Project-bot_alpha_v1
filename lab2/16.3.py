def kill(matrix, x, y, dmg = 4):
    if matrix[x][y] > dmg:
        matrix[x][y] -= dmg
    else:
        matrix[x][y] = 0
    return matrix[x][y]

size = int(input())
matrix = [[int(input()) for i in range(size)] for j in range(size)]
dose = int(input())
destination = [[int(input()) for ii in range(2)] for jj in range(dose)]
for poison in destination:
    y = poison[0]
    x = poison[1]
    kill(matrix, x, y, 8)
    if x - 1 >= 0:
        kill(matrix, x - 1, y)
        if y - 1 >= 0:
            kill(matrix, x - 1, y - 1)
        if y + 1 < size:
            kill(matrix, x - 1, y + 1)
    if x + 1 < size:
        kill(matrix, x + 1, y)
        if y - 1 >= 0:
            kill(matrix, x + 1, y - 1)
        if y + 1 < size:
            kill(matrix, x + 1, y + 1)
    if y - 1 >= 0:
        kill(matrix, x, y - 1)
    if y + 1 < size:
        kill(matrix, x, y + 1)
for line in matrix:
    print(*line, sep=' ')