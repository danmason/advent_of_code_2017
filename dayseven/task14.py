file = open("input.txt","r")
tower = file.read().split("\n")
tower_names = []
tower_weights = []
pointed_to = []

for x in tower:
    tower_level = x.split()
    tower_names.append(tower_level[0])
    for c in ["(",")"]: tower_level[1] = tower_level[1].replace(c, "")
    tower_weights.append(tower_level[1])
    
    if("->") in x:
        y = x.split("-> ")[1]
        for z in y.split(", "):
            pointed_to.append(z)
            
print("Bottom of list",set(tower_names) - set(pointed_to))        
                

