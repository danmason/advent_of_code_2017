file = open("input.txt","r")
instructions = file.read().split("\n")
instructions = list(map(int, instructions))
next_instruction = 0
steps = 0

while(next_instruction < len(instructions)):
    steps+=1
    current_instruction = next_instruction
    next_instruction+=instructions[current_instruction]
    instructions[current_instruction]+=1
    
print("Number of steps: ",steps)
