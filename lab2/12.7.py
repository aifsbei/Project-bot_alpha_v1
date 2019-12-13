height = int(input())
width = int(input())
img = []
for i in range(height):
    string = input()
    temp = [item for item in string]
    img.append(temp)
for cols, cells in enumerate(img):
    if cols > 0:
        img.remove(cells)

for cells in img:
    for ix, rows in enumerate(cells):
        del cells[ix]

for item in img:
    print(*item)