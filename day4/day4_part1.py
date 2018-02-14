
file = open("day4_input.txt")
passphraselist = []

for line in file:
    passphraselist.append(line.strip().split(" "))

count = 0

for phrases in passphraselist:
    repeat = False
    for word in range(len(phrases)):
        place = phrases.index(phrases[word])
        try:
            phrases.index(phrases[word], place + 1)
            repeat = True
        except ValueError:
            pass     
    if not repeat:
        count += 1

print(count)
