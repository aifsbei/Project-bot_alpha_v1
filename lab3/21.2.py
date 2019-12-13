def transpose(matrix):
    cols = []
    for i in range(len(matrix[0])):
        cols.append([line[i] for line in matrix])
    matrix.clear()
    for item in cols:
        matrix.append(item)


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)