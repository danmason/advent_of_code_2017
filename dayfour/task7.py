file = open("input.txt","r")
passphrases = file.read().split("\n")
num_phrases = len(passphrases)
invalid = 0

for x in passphrases:
    passphrase = x.split(" ")
    seen = []
    for y in passphrase:
        if y in seen:
            invalid +=1
            break
        seen.append(y)

print("Number valid:",num_phrases - invalid,"/",num_phrases)
