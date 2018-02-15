
TARGET = int(open("day3_input.txt").read())

coordinates = [0, 0]

def up(coordinates):
    coordinates[1] += 1

def right(coordinates):
    coordinates[0] += 1

def down(coordinates):
    coordinates[1] -= 1

def left(coordinates):
    coordinates[0] -= 1

number = 1
square_size = 0

while number < TARGET:
    square_size += 1

    right(coordinates)
    number += 1

    for _ in range(square_size * 2 - 1):
        if number != TARGET:
            up(coordinates)
            number += 1
        else:
            break
    
    for _ in range(square_size * 2):
        if number != TARGET:
            left(coordinates)
            number += 1
        else:
            break

    for _ in range(square_size * 2):
        if number != TARGET:
            down(coordinates)
            number += 1
        else:
            break

    for _ in range(square_size * 2):
        if number != TARGET:
            right(coordinates)
            number += 1
        else:
            break
    
print("Final coordinates are:", coordinates)
print("Manhattan distance from access port: {0}".format(abs(coordinates[0]) + abs(coordinates[1])))
