
file = open("day7_input.txt")

circus = []
towers = []
BASE = ["bpvhwhh", 60, "lzfgxlb", "fzclaow", "kfdxxb", "xnmjpa",
        "rilgrr", "fvrrpo", "zcmlgn"] #Obtained from Part 1.

for line in file:
    circus.append(line.strip().split())

for level in circus:
    if "->" in level:
        string_format = level
        string_format.remove("->")
        string_format[1] = int(string_format[1][1:-1])
        for index in range(2, len(string_format) - 1):
            string_format[index] = string_format[index][:-1]
        towers.append(string_format)
    else:
        string_format = level
        string_format[1] = int(string_format[1][1:-1])
        towers.append(string_format)

def get_id_list(id: str):
    for tower in towers:
        if tower[0] == id:
            return tower

def get_weight(id: list, towers: list):
    global weight
    
    if len(id) == 2:
        weight += id[1]
        return weight

    elif len(id) > 2:
        weight += id[1]
        for tower_id in id[2:]:
            id_list = get_id_list(tower_id)
            get_weight(id_list, towers)
            
        return weight

# Unfinished auto-generated answer
weight_check = {}
for tower in BASE[2:]:
    weight = 0
    tower_id = get_id_list(tower)
    weight_check[tower_id[0]] = get_weight(tower_id, towers)

print(weight_check)
