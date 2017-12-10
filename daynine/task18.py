file = open("input.txt","r")
stream = file.read()
read_values = True
ignore_value = False
score = 0
bracket_score = 0
garbage_value = 0

for x in stream:
    if read_values:
        if x == "<":
            read_values = False
        elif x == "{":
            bracket_score+=1
        elif x == "}":
            score += bracket_score
            bracket_score -= 1
    else:
        if ignore_value:
            ignore_value = False
        else:
            if x == ">":
                read_values = True
            elif x == "!":
                ignore_value = True
            else:
                garbage_value+=1
                
print(garbage_value)
