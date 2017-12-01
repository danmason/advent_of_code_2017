file = open("input.txt", "r")
captcha = list(file.read())
total = 0

for i in range(len(captcha)-1):
    if captcha[i] == captcha[i+1]:
        total+=int(captcha[i])

if(captcha[len(captcha)-1] == captcha[0]):
    total+= int(captcha[len(captcha)-1])
    
print(total)
