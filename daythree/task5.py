puzzle_input = 368078
i=1
height = 1
distance = [0,0]

while i*i < puzzle_input:
    i+=2
    height+=2
    distance[0]+=1
    distance[1]+=1

iteration = i*i
print(distance)
