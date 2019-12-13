def from_string_to_list(string, container):
    to_add = string.split()
    for item in to_add:
        container.append(item)


a = [77, 'abc']
from_string_to_list('1 3 99 52', a)
print(*a)