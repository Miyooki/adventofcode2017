
file = open("day1_input.txt")
numlist = file.read()
numlist = list(numlist)

total = 0
for index in range(len(numlist) - 1):
    if numlist[index] == numlist[index + 1]:
        print("Adding {0} to the total, total: {1}".format(index, total))
        total += int(numlist[index])

if numlist[-1] == numlist[0]:
    total += int(numlist[-1])

print(total)
