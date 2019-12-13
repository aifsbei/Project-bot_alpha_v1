quantity = int(input())
items = [input() for i in range(quantity)]
number_of_rotations = int(input())
new_order = ()
for i in range(number_of_rotations):
    items_left = int(input())
    quantity -= 3 - items_left
    new_order = list(int(input()) for i in range(quantity))
new_order.reverse()
for ix in range(len(new_order)):
    print(items[new_order[ix]])