input_file = open("./part_1_input.txt", "r")
change_list = [int(i) for i in input_file.readlines()]
input_file.close()
# Keep adding the numbers into a variable
frequency = 0
for change in change_list:
    frequency += change
print(frequency)
