share = int(input())
have_share = False
bought = 0
sold = 0
while True:
    prev_share = share
    share = int(input())
    if share == 0:
        break
    if have_share == False:
        if prev_share < share:
            bought = share
            have_share = True
    elif have_share:
        if prev_share > share:
            print('yeaaa')
            sold = share
            have_share = None
print(bought, sold, sold - bought)