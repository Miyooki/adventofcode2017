
file = open("day6_input.txt")

starting = [int(i) for i in file.read().split("\t")]
position_dictionary = []
previous_memory = starting.copy()
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
                    previous_memory = new_memory.copy()
                    done = True
                elif new_memory in position_dictionary:
                    position_dictionary.append(new_memory)
                    repeated_mem = new_memory.copy()
                    done = True
                    repeat = True
                    
        except IndexError:
            highest_pos = -1

print("The repeating memory is:", new_memory)
print("Number of redistribution cycles before repeat is:", len(position_dictionary) - 1)
