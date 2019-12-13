from collections import Counter
string = input().lower()
c = Counter(string)
print(list(c.most_common(1))[0][1])