from fractions import Fraction
quantity = int(input())
final_damage = Fraction(0, 1)
list = []
for i in range(0, quantity):
    numerator = int(input())
    denominator = int(input())
    damage = Fraction(numerator, denominator)
    list.append(damage)
for item in list:
    final_damage += item
print(final_damage)

