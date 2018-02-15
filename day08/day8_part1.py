
file = open("day8_input.txt")

commands = []
for line in file:
    commands.append(line.strip().split(" "))

register = {}

def reg_change(command):
    if command[1] == "inc":
        register[command[0]] += int(command[2])

    elif command[1] == "dec":
        register[command[0]] -= int(command[2])


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

print("Highest value held in any register:", register[max(register, key=register.get)])
