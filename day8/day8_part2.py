
file = open("day8_input.txt")

commands = []
for line in file:
    commands.append(line.strip().split(" "))

register = {}
largest = 0

def reg_change(command):
    global largest
    if command[1] == "inc":
        register[command[0]] += int(command[2])
        compare = register[command[0]]
        if compare > largest:
            largest = compare

    elif command[1] == "dec":
        register[command[0]] -= int(command[2])
        compare = register[command[0]]
        if compare > largest:
            largest = compare

def reg_help(command):
    if register.get(command[0]) == None:
        register[command[0]] = 0
    if register.get(command[4]) == None:
        register[command[4]] = 0

    if command[5] == "==":
        if register[command[4]] == int(command[6]):
            reg_change(command)

    elif command[5] == "!=":
        if register[command[4]] != int(command[6]):
            reg_change(command)
        
    elif command[5] == "<":
        if register[command[4]] < int(command[6]):
            reg_change(command)

    elif command[5] == "<=":
        if register[command[4]] <= int(command[6]):
            reg_change(command)

    elif command[5] == ">":
        if register[command[4]] > int(command[6]):
            reg_change(command)

    elif command[5] == ">=":
        if register[command[4]] >= int(command[6]):
            reg_change(command)

for command in commands:
    reg_help(command)

print(largest)
