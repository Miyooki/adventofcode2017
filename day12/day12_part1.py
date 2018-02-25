
file = open("day12_input.txt")

pipes = []

for line in file:
    string_format = line.strip().split(" ")
    for index in range(2, len(string_format)):
        string_format[index] = string_format[index][:-1]
    pipes.append(string_format)

pipe_dict = {"0": 1}

def one_pass(pipe_dict: dict, pipes: list):
    for pipe_id in pipe_dict:

        for pipe in pipes:
            if pipe[0] == pipe_id:
                for output in range(2, len(pipe)):
                    if pipe_dict.get(pipe[output]) == None:
                        pipe_dict[pipe[output]] = 1
                        return pipe_dict

            for output in range(2, len(pipe)):
                if pipe[output] == pipe_id:
                    if pipe_dict.get(pipe[0]) == None:
                        pipe_dict[pipe[0]] = 1
                        return pipe_dict

    return -1

while True:
    if one_pass(pipe_dict, pipes) != -1:
        print(one_pass(pipe_dict, pipes))
    else:
        break
