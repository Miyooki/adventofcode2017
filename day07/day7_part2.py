
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