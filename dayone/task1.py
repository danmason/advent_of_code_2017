file = open("input.txt", "r")
captcha = list(file.read())
total = 0

for i in range(len(captcha)):
    element_to_check = int((i+1) % len(captcha))
    if captcha[i] == captcha[element_to_check]:
        total+=int(captcha[i])
    
print(total)
