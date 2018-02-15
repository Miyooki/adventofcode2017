
file = open("day9_input.txt")

stream = list(file.read())
groups = 0

def clean_up(stream):
    pass

for index in range(len(stream)):
    if stream[index] == "<":
        garbage_start = index

print(stream)

for char in stream:
    if char == "{":
        pass

    elif char  == "}":
        pass

    elif char == "!":
        pass

    elif char == "<":
        pass
    
    elif char == ">":
        pass

""" 
TODO: Count the starting brackets
"""