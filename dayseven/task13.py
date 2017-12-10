file = open("input.txt","r")
tower = file.read().split("\n")
tower_names = []
pointed_to = []

for x in tower:
    tower_names.append(x.split(' ', 1)[0])
    if("->") in x:
        y = x.split("-> ")[1]
        for z in y.split(", "):
            pointed_to.append(z)
print("Bottom of list",set(tower_names) - set(pointed_to))        
                

