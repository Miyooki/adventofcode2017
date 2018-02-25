
file = open("day7_input.txt")

circus = []
towers = []

for line in file:
    circus.append(line.strip().split())

for level in circus:
    if "->" in level:
        string_format = level
        string_format.remove("->")
        for index in range(2, len(string_format) - 1):
            string_format[index] = string_format[index][:-1]

        towers.append(string_format)

def sub_tower(tower: list, towers: list):
    search = tower[0]
    for index in range(len(towers)):
        for sub in range(2, len(towers[index])):
            if search == towers[index][sub]:
                return towers[index]

    return None

bottom = False
current = towers[0]

while not bottom:

    if sub_tower(current, towers) != None:
        if sub_tower(sub_tower(current, towers), towers) == None:
            print(sub_tower(current, towers))
            bottom = True
        else:
            current = sub_tower(current, towers)
            