number_of_stations = int(input())
stations = [input().split() for i in range(1, number_of_stations)]
trip = input().split()
trip = list(map(lambda x: int(x), trip))
trip.sort()
temp = []
for ix, line in enumerate(stations):
    stations[ix] = list(map(lambda x: int(x), line))
if stations[trip[1] - 1][trip[0]] > sum(stations[trip[1]]):
    print(trip[1] + 1)
else:
    print(trip[0])