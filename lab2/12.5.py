from collections import Counter
n = int(input())
string = str(1/n)
string = string[2:]
samples = []
c = Counter()
for i in range(len(string)):
    for j in range(i):
        samples.append(string[j-i:i])
samples = list(set(samples))
samples.sort()
if len(samples) < 8:
    print(0)
    exit(0)
try:
    del samples[0]
    c = Counter(string)
    c = dict(c)
    most_common_digit = 0
    for item in c:
        if c[str(item[0])] > int(most_common_digit):
            most_common_digit = c[str(item[0])]
    for item in c:
        if c[str(item[0])] == int(most_common_digit):
            print(item[0], end='')
except IndexError:
    print(0)