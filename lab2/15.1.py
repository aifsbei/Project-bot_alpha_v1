symbol = input()
words = input().split()
for word in words:
    print(word) if symbol.lower() in word or symbol.upper() in word else None