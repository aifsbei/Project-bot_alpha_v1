m = int(input())
students = []
for i in range(m):
    n = int(input())
    row = []
    for j in range(n):
        row.append(input())
    students.append(row)
answer = set(students[0])
for item in students:
    answer = answer & set(item)
print(*answer, sep='\n')