def hasGrid(line):
    for ix, char in enumerate(line):
        if char == '#':
            return line
    return None


def findLine(line, container):
    for ix, item in enumerate(container):
        if line in item:
            return ix + 1
    return None


lines = []
#hasGrid('sd')
while True:
    item = input()
    if item == '':
        break
    lines.append(item)
filtered = list(filter(lambda x: hasGrid(x), lines))
filtered = list(map(lambda x: x.replace('# ', 'Line {}: '.format(findLine(x, lines))).lstrip(), filtered))
print(*filtered, sep='\n')