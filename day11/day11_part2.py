
file = open("day11_input.txt")

direction = file.read().split(",")

coordinates = [0, 0]
# first value represents 60 degrees horizontal movement (represents x)
# second value represent vertical movement (represents y)

def north_west(coordinates):
    coordinates[0] -= 1
    coordinates[1] += 1

def north(coordinates):
    coordinates[1] += 1

def north_east(coordinates):
    coordinates[0] += 1

def south_east(coordinates):
    coordinates[0] += 1
    coordinates[1] -= 1

def south(coordinates):
    coordinates[1] -= 1

def south_west(coordinates):
    coordinates[0] -= 1

def furthest(coordinates):
    if coordinates[0] <= 0 and coordinates[1] <= 0:
        return abs(coordinates[0] + coordinates[1])

    elif coordinates[0] >= 0 and coordinates[1] >= 0:
        return abs(coordinates[0] + coordinates[1])

    else:
        return max(abs(coordinates[0]), abs(coordinates[1]))

furthest_step = 0

for step in direction:
    if step == "nw":
        north_west(coordinates)
        
    elif step == "n":
        north(coordinates)

    elif step == "ne":
        north_east(coordinates)

    elif step == "se":
        south_east(coordinates)

    elif step == "s":
        south(coordinates)

    elif step == "sw":
        south_west(coordinates)
    
    if furthest(coordinates) > furthest_step:
        furthest_step = furthest(coordinates)

print("The end coordinates are:", coordinates)
print("The furthest steps away the child process travelled:", furthest_step)
