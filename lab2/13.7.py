quantity = int(input())
soldiers = [input() for i in range(quantity)]
dec = int(input()) - 1
while len(soldiers) > 0:
    for ix, soldier in enumerate(soldiers):
        if ix % dec == 0:
            print(soldier)
            soldiers.remove(soldier)