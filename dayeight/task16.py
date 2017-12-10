file = open("input.txt","r")
registers = file.read().split("\n")
register_dictionary = {}
lifetime_max = 0

def changeValue(inc_or_dec, number, value_to_change):
    if inc_or_dec == "inc":
        register_dictionary[value_to_change] += number
    else:
        register_dictionary[value_to_change] -= number

for x in registers:
    register=x.split()
    if register[0] not in register_dictionary:
        register_dictionary.update({register[0]:0}) 
    if register[4] not in register_dictionary:
        register_dictionary.update({register[4]:0})
    # Using eval to handle the operations in the string
    if eval(str(register_dictionary[register[4]]) + register[5] + register[6]):
        changeValue(register[1], int(register[2]), register[0])
        if register_dictionary[register[0]] > lifetime_max:
            lifetime_max = register_dictionary[register[0]]

print(lifetime_max)
            
