lengths = [192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12]
list_to_edit = [i for i in range(256)]
position = 0
skip_size = 0

for x in lengths:
    rev_list = []
    for y in range(x):
        rev_list = [(list_to_edit[(position + y) % len(list_to_edit)])] + rev_list
    for z in range(x):
        list_to_edit[(position + z) % len(list_to_edit)] = rev_list[z]
    position = (position + x + skip_size) % len(list_to_edit)
    skip_size+=1

print(list_to_edit[0] * list_to_edit[1])
