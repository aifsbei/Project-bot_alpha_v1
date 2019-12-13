number_of_permissions = int(input())
permissions = [input() for i in range(number_of_permissions)]
number_of_requests = int(input())
for i in range(number_of_requests):
    request = input()
#    for permission in permissions:
#        print("YES") if permission in request else print("NO")
    if any(request.startswith(permission) for permission in permissions):
        print('YES')
        continue
    print('NO')