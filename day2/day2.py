# Part 1
file = open("day2_input.txt")
numlist = []
for line in file:
    numlist.append(line.strip().split("\t"))

checksum = 0

for rows in numlist:
    rows = [int(i) for i in rows]
    found = False
    while not found:
        for num in range(len(rows) - 1):
            for num2 in range(len(rows) - 1):
                if num != num2:
                    if rows[num] % rows[num2] == 0:
                        checksum += rows[num] / rows[num2]
                        found = True

print(checksum)