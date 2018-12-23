input_file = open("./part_2_input.txt", "r")
change_list = [int(i) for i in input_file.readlines()]
input_file.close()
# Make a set to keep unique values and a flag to stop the while loop
frequency_set = set()
frequency = 0
found_frequency = False
# Keep looping through the list, add the numbers, till you find one that
# already exists in the set.
while not found_frequency:
    for change in change_list:
        frequency += change
        if frequency in frequency_set:
            found_frequency = True
            break
        else:
            frequency_set.add(frequency)
print(frequency)
