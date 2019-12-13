list = [int(input()) for i in range(int(input()))]
list.sort()
list.reverse()
print(*list, sep='\n')