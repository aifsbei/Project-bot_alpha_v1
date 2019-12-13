def possible_turns(cell):
    cells = []
    digits = to_digits(cell)
    if in_range((digits[0] + 2, digits[1] + 1)):
        cells.append(to_letters((digits[0] + 2, digits[1] + 1)))
    if in_range((digits[0] - 2, digits[1] + 1)):
        cells.append(to_letters((digits[0] - 2, digits[1] + 1)))
    if in_range((digits[0] + 2, digits[1] - 1)):
        cells.append(to_letters((digits[0] + 2, digits[1] - 1)))
    if in_range((digits[0] - 2, digits[1] - 1)):
        cells.append(to_letters((digits[0] - 2, digits[1] - 1)))
    if in_range((digits[0] + 1, digits[1] + 2)):
        cells.append(to_letters((digits[0] + 1, digits[1] + 2)))
    if in_range((digits[0] - 1, digits[1] + 2)):
        cells.append(to_letters((digits[0] - 1, digits[1] + 2)))
    if in_range((digits[0] + 1, digits[1] - 2)):
        cells.append(to_letters((digits[0] + 1, digits[1] - 2)))
    if in_range((digits[0] - 1, digits[1] - 2)):
        cells.append(to_letters((digits[0] - 1, digits[1] - 2)))
    return cells

def to_digits(string):
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    return letters.index(string[0]) + 1, int(string[1])


def to_letters(digits):
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    return letters[digits[0] - 1] + str(digits[1])


def in_range(digits):
    return all(0 < digit < 9 for digit in digits)


print(sorted(possible_turns('B1')))