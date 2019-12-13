d = int(input())
m = int(input()) - 2 % 12
year = int(input())
y = year % 100
c = year // 100
day_of_week = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
print(day_of_week % 7)