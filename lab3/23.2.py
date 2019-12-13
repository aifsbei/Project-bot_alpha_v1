import math

def find_farthest_orbit(list_of_orbits):
    return max(item for item in list_of_orbits if
               item[0] * item[1] * math.pi == max(math.pi * i[0] * i[1]
                                                  for i in list_of_orbits))


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))