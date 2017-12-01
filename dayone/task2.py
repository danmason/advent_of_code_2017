file = open("input.txt", "r")
captcha = list(file.read())
length = len(captcha) 
total = 0

for i in range(length):
    element_to_check = int((i + (length/2)) % length)
    if captcha[i] == captcha[element_to_check]:
        total+=int(captcha[i])
    
print(total)
