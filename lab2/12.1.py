whitelist = [input() for i in range(int(input()))]
requests = [input() for i in range(int(input()))]
print(*(request for request in requests if request in whitelist), sep='\n')