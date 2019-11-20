
"""
>	increment the data pointer (to point to the next cell to the right).

< 	decrement the data pointer (to point to the next cell to the left).
+ 	increment (increase by one) the byte at the data pointer.
- 	decrement (decrease by one) the byte at the data pointer.
. 	output the byte at the data pointer.
, 	accept one byte of input, storing its value in the byte at the data pointer.
[ 	if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
] 	if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
"""


program_string = '+[,.]'

program_list = split(program_string)

data_array = [0]
data_pointer = 0

instruction_pointer = 0

def increment_bit(data_pointer):
    if (data_array[data_pointer] == 255):
        data_array[data_pointer] = 0
        instruction_pointer += 1
    else:
        data_array[data_pointer] += 1
        instruction_pointer += 1

def decrement_bit(data_pointer):
    if (data_array[data_pointer] == 0):
        data_array[data_pointer] = 255
    else:
        data_array[data_pointer] -= 1

def find_close_brakcet(instruction_pointer):
    search_pointer = instruction_pointer
    while (program_list[search_pointer] != ']'):
        search_pointer += 1

    return search_pointer + 1

# #### Build jump table
# for instruction in program_list:

jump_list = []
for instruction in program_list:
    if (instruction == '['):



while (instruction_pointer < len(program_list)):
    if (program_list[instruction_pointer] == "+"):
        increment_bit(data_pointer)
    
    elif (program_list[instruction_pointer] == "-"):
        decrement_bit(data_pointer)
    
    elif (program_list[instruction_pointer] == ">"):
        data_array.append(0)
        data_pointer += 1

    elif (program_list[instruction_pointer] == "<"):
        if (instruction_pointer == 0):
            continue
        instruction_pointer -= 1
    
    elif (program_list[instruction_pointer] == "."):
        print(data_array[data_pointer])

    elif (program_list[instruction_pointer] == ","):
        data_array[data_pointer] = input(">> ")

    # elif (program_list[instruction_pointer] == "["):
    #     if data_array[data_pointer] == 0:


cmd_input = input(">> ")

