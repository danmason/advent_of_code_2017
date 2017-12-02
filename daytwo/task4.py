file = open("input.txt","r")
file_input = (file.read()).split("\n")
checksum = 0

for x in file_input:
    input_line = list(map(int,x.split("\t")))
    for i in range(len(input_line)):
        for j in range(i + 1, len(input_line)):
            if input_line[i] % input_line[j]==0:
                checksum += input_line[i]/input_line[j]
            elif input_line[j] % input_line[i]==0:
                checksum += input_line[j]/input_line[i]
            
print(checksum)
    
