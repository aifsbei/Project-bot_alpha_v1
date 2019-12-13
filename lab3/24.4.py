words = [input() for i in range(int(input()))]


def anagram(words):
    temp = []
    for ix, word in enumerate(words):
        temp.append([])
        for item in words:
            if set(item.lower()) == set(word.lower()):
                temp[ix].append(item.lower())
    temp_set = set(frozenset(i) for i in temp)
    for item in temp_set:
        print(*item)


anagram(words)