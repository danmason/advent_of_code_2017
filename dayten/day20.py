from functools import reduce

lengths = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"
ascii_lengths = []
hashes = []
for x in lengths:
    ascii_lengths.append(ord(x))       
ascii_lengths = ascii_lengths + [17, 31, 73, 47, 23]
list_to_edit = [i for i in range(256)]
position = 0
skip_size = 0

for i in range(64):
    for x in ascii_lengths:
        rev_list = []
        for y in range(x):
            rev_list = [(list_to_edit[(position + y) % len(list_to_edit)])] + rev_list
        for z in range(x):
            list_to_edit[(position + z) % len(list_to_edit)] = rev_list[z]
        position += skip_size + x
        skip_size+=1

dense = []
for x in range(0,16):
    result = 0
    for y in range(0,16):
        result^= list_to_edit[(x*16)+y]
    dense.append('{0:02x}'.format(result))

print(''.join(dense))


