
file = open("day16_input.txt")

dance_moves = file.read().split(",")

programs = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p"]

for move in dance_moves:
    if move[0] == "s":
        position = 16 - int(move[1:])
        programs = programs[position:] + programs[:position]

    elif move[0] == "x":
        source = int(move[1])
        if move[2] != "/":
            source = int(move[1:3])
            target = int(move[4:])
        else:
            target = int(move[3:])
        
        temp = programs[source]
        programs[source] = programs[target]
        programs[target] = temp

    elif move[0] == "p":
        source_index = programs.index(move[1])
        target_index = programs.index(move[3])
        temp = programs[source_index]
        programs[source_index] = programs[target_index]
        programs[target_index] = temp

print("Order of programs after dance:", "".join(programs))
