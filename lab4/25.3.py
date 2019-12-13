from random import randint
radius = 1
field = 4
iters = 1000000
accuracy = 100
belongs = 0
not_belongs = 0


def is_in_circle(x, y):
    global radius
    return True if x ** 2 + y ** 2 < radius ** 2 else False
    #return True if -1 <= x <= 0 and 0 <= y <= 1 else False


for i in range(iters):
    x = randint(-field * accuracy, field * accuracy) / accuracy
    y = randint(-field * accuracy, field * accuracy) / accuracy
    if is_in_circle(x, y):
        belongs += 1
    else:
        not_belongs += 1
try:
    square = belongs / (not_belongs + belongs)
    square *= (2 * field) ** 2
    print(square)
except ZeroDivisionError:
    print('miss')