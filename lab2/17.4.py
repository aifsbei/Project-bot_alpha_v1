history_length = int(input())
history = {}
names = []
for i in range(history_length):
    string = input()
    if 'опубликовал' in string:
        words = string.split()
        history[words[0]] = [int(words[5]), []]
        names.append(words[0])
    elif 'отрепостил' in string:
        words = string.split()
        history[words[0]] = [int(words[7]), []]
        #print(history[words[4][:-1]])
        history[words[4][:-1]][1].append(words[0])
        names.append(words[0])
for name in reversed(names):
    while history[name][1] != []:
        history[name][0] += history[history[name][1][0]][0]
        del history[name][1][0]
for person in history:
    print(history[person][0])
