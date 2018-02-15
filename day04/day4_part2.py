
file = open("day4_input.txt")
passphraselist = []

for line in file:
    passphraselist.append(line.strip().split(" "))

count = 0

for phrases in passphraselist:
    anagram = False
    for word in range(len(phrases)):
        anagramdict = {}
        for letter in phrases[word]:
                try:
                    anagramdict[letter] += 1
                except KeyError:
                    anagramdict[letter] = 1

        for word2 in range(len(phrases)):
            comparedict = {}
            if word2 != word:
                for letter in phrases[word2]:
                    try:
                        comparedict[letter] += 1
                    except KeyError:
                        comparedict[letter] = 1

            if anagramdict == comparedict:
                anagram = True
        
    if not anagram:
        count += 1

print("Number of valid anagram passphrases:", count)
