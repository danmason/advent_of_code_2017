file = open("input.txt","r")
file_input = (file.read()).split("\n")
checksum = 0

for x in file_input:
    #used map to map strings in the split list to integers then saves result
    input_line = list(map(int,x.split("\t")))
    checksum += max(input_line)-min(input_line)

print(checksum)
    
