
file = open("day2_input.txt")
numlist = []
for line in file:
    numlist.append(line.strip().split("\t"))

checksum = 0

for rows in numlist:
    rows = [int(i) for i in rows]
    checksum += max(rows) - min(rows)

print(checksum)
