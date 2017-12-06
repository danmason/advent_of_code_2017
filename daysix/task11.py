file = open("input.txt","r")
memory_banks = file.read().split("\t")
memory_banks = list(map(int, memory_banks))
seen = []
iterations = 0

while memory_banks not in seen:
    seen.append(memory_banks[:])
    to_distribute = max(memory_banks)
    to_distribute_index = memory_banks.index(to_distribute)
    current_index = (to_distribute_index + 1) % len(memory_banks)
    while to_distribute > 0:
        if current_index == to_distribute_index:
            if to_distribute == 1:
                memory_banks[to_distribute_index] = 1
                break
            else:
                current_index=(current_index+1) % len(memory_banks)
        else:
            memory_banks[current_index]+=1
            to_distribute-=1
            current_index=(current_index+1) % len(memory_banks)
            memory_banks[to_distribute_index] = to_distribute
    iterations+=1
    
print("Number of iterations:",iterations)
            
            
