money = int(input())
count = int(input())
for bull in range(1, count):
    for cow in range(count):
        for calf in range(count):
            if bull + cow + calf == count:
                if bull * 20 + cow * 10 + calf * 5 <= money:
                    print(bull, cow, calf, 'with price =', bull * 20 + cow * 10 + calf * 5)