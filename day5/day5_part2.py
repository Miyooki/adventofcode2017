
file = open("day5_input.txt")

move = []

for line in file:
    move.append(line.strip())

move = [int(i) for i in move]

def move_help(move, index):
    go_to = move[index]
    try:
        check = move[index + go_to]
        if go_to >= 3:
            move[index] -= 1
        else:
            move[index] += 1
        return index + go_to
    except IndexError:
        return None

steps = 0
current_index = 0

while True:
    current_index = move_help(move, current_index)
    steps += 1
    if current_index == None:
        break
    
print(steps)
