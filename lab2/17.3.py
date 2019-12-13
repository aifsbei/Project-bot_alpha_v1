number_of_mates = int(input())
mates = [input().split() for i in range(number_of_mates)]
mates.sort(key=lambda x: x[1])
questions = int(input())
for i in range(questions):
    string = input()
    for item in mates:
        if string in item:
            print(item[0], item[1], end=' ')
    print()