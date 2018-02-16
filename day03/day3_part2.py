
TARGET = int(open("day3_input.txt").read())

coordinates = [0, 0]
coordinates_dict = {(0, 0): 1}

def up(coordinates):
    coordinates[1] += 1

def right(coordinates):
    coordinates[0] += 1

def down(coordinates):
    coordinates[1] -= 1

def left(coordinates):
    coordinates[0] -= 1

def surround(number, coordinates):
    total = 0
    
    if coordinates_dict.get(tuple((coordinates[0], coordinates[1] + 1))) is not None:
        total += coordinates_dict[tuple((coordinates[0], coordinates[1] + 1))]
    
    if coordinates_dict.get(tuple((coordinates[0] + 1, coordinates[1] + 1))) is not None:
        total += coordinates_dict[tuple((coordinates[0] + 1, coordinates[1] + 1))]

    if coordinates_dict.get(tuple((coordinates[0] + 1, coordinates[1]))) is not None:
        total += coordinates_dict[tuple((coordinates[0] + 1, coordinates[1]))]
        
    if coordinates_dict.get(tuple((coordinates[0] + 1, coordinates[1] - 1))) is not None:
        total += coordinates_dict[tuple((coordinates[0] + 1, coordinates[1] - 1))]
    
    if coordinates_dict.get(tuple((coordinates[0], coordinates[1] - 1))) is not None:
        total += coordinates_dict[tuple((coordinates[0], coordinates[1] - 1))]

    if coordinates_dict.get(tuple((coordinates[0] - 1, coordinates[1] - 1))) is not None:
        total += coordinates_dict[tuple((coordinates[0] - 1, coordinates[1] - 1))]

    if coordinates_dict.get(tuple((coordinates[0] - 1, coordinates[1]))) is not None:
        total += coordinates_dict[tuple((coordinates[0] - 1, coordinates[1]))]

    if coordinates_dict.get(tuple((coordinates[0] - 1, coordinates[1] + 1))) is not None:
        total += coordinates_dict[tuple((coordinates[0] - 1, coordinates[1] + 1))]
    
    return total

number = 1
square_size = 0

while number < TARGET:
    square_size += 1

    right(coordinates)
    coordinates_dict[tuple(coordinates)] = surround(number, coordinates)
    number = surround(number, coordinates)

    for _ in range(square_size * 2 - 1):
        if number < TARGET:
            up(coordinates)
            coordinates_dict[tuple(coordinates)] = surround(number, coordinates)
            number = surround(number, coordinates)
        else:
            break
    
    for _ in range(square_size * 2):
        if number < TARGET:
            left(coordinates)
            coordinates_dict[tuple(coordinates)] = surround(number, coordinates)
            number = surround(number, coordinates)
        else:
            break

    for _ in range(square_size * 2):
        if number < TARGET:
            down(coordinates)
            coordinates_dict[tuple(coordinates)] = surround(number, coordinates)
            number = surround(number, coordinates)
        else:
            break

    for _ in range(square_size * 2):
        if number < TARGET:
            right(coordinates)
            coordinates_dict[tuple(coordinates)] = surround(number, coordinates)
            number = surround(number, coordinates)
        else:
            break

print("First value larger than input is:", coordinates_dict[list(coordinates_dict.keys())[-1]])
