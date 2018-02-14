
file = open("day5/day5_input.txt")

move = []

for line in file:
    move.append(line.strip())

move = [int(i) for i in move]

print(move)