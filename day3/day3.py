
TARGET = 265149

def move_up(x, y):
    return x, y + 1

def move_right(x, y):
    return x + 1, y

def move_down(x, y):
    return x, y - 1

def move_left(x, y):
    return x - 1, y

coordinates = (0, 0)
count = 0

for steps in range(TARGET):
    count += 1
    move_right(coordinates)
    print("At step {0}, coordinate: {1}".format(count, coordinates))

print(coordinates)
    