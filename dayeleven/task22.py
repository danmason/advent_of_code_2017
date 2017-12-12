file = open("input.txt","r")
directions = file.read().split(",")
steps = {"n":0, "e":0, "s":0, "w":0}
max_distance = 0

for x in directions:
    for y in x:
        steps[y] +=1
    new_list = [steps["n"]-steps["s"], steps["s"]-steps["n"], steps["e"]-steps["w"], steps["w"]-steps["e"]]
    if max_distance < max(new_list):
        max_distance = max(new_list)

print(max_distance)
