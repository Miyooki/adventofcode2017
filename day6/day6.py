
starting = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
test = [0, 2, 7, 0]
position_dictionary = []
previous_memory = starting.copy()
new_memory = []
highest = 0
repeat = False

position_dictionary.append(starting)
while not repeat:
    done = False
    new_memory = previous_memory.copy()
    highest = max(new_memory)
    highest_pos = new_memory.index(highest)
    new_memory[highest_pos] = 0
    while not done:
        highest_pos += 1
        try:
            if highest != 0:
                new_memory[highest_pos] += 1
                highest -= 1
            elif highest == 0:
                if new_memory not in position_dictionary:
                    position_dictionary.append(new_memory)
                    print(new_memory)
                    previous_memory = new_memory.copy()
                    done = True
                elif new_memory in position_dictionary:
                    print("The repeating memory is:", new_memory)
                    position_dictionary.append(new_memory)
                    repeated_mem = new_memory.copy()
                    repeat = True
                    done = True
        except IndexError:
            highest_pos = -1

print(position_dictionary)
print(len(position_dictionary))
repeat_pos = position_dictionary.index(repeated_mem)
print(position_dictionary.index(repeated_mem))
print(position_dictionary.index(repeated_mem, repeat_pos + 1))