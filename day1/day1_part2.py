
file = open("day1_input.txt")
numlist = file.read()
numlist = list(numlist)

halfway = int(len(numlist) / 2)
doublelist = numlist + numlist
total = 0
for index in range(len(numlist)):
    if numlist[index] == doublelist[index + halfway]:
        print("Adding {0} to the total, total: {1}".format(doublelist[index], total))
        total += int(doublelist[index])

print(total)
