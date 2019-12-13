n = int(input())
string = ''
list_of_strings = []
for i in range(n):
    string = input()
    if string[:2] == '%%':
        string = string[2:]
    if string[:4] == '####':
        string = None
    list_of_strings.append(string) if string is not None else None
print(*list_of_strings, sep='\n')