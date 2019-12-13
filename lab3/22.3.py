import random

scoring = {'Яблочко': 50, 'Зеленое кольцо': 25,
           'Внешнее кольцо': {x: y for x, y in zip(range(1, 21), [random.randint(0, 60) for i in range(20)])},
           'Внутреннее кольцо': {x: y for x, y in zip(range(1, 21), [random.randint(0, 60) for j in range(20)])}}


def score(ring, sector=None):
    global scoring
    return scoring[ring][sector] if sector is not None else scoring[ring]


print(score('Зеленое кольцо'))