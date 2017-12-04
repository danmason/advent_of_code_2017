file = open("input.txt","r")
passphrases = file.read().split("\n")
num_phrases = len(passphrases)
invalid = 0

def check_anagram(word1,word2):
    if len(word1) == len(word2):
        if sorted(list(word1)) == sorted(list(word2)):
            return True
    return False
    
for x in passphrases:
    is_anagram = False
    passphrase = x.split(" ")
    seen = []
    for y in passphrase:
        for z in seen:
            is_anagram = check_anagram(y,z)
            if(is_anagram):
                invalid+=1
                break
        if(is_anagram):
            break
        seen.append(y)
        
print("Number valid:",num_phrases - invalid,"/",num_phrases)
