input_file = open("./part_1_input.txt", "r")
string_list = input_file.readlines()
input_file.close()
# A dict to count characters that appeared twice or thrice.
occurence_counter = {
        "two": 0,
        "three": 0
}
# For each string in the list. Check each of their chars to see which one
# shows up twice or thrice, and add one in the dict above.
# Note: The flags are there to prevent the loop from runnning too much.
# If three chars show up twice in a string it still counts as one.
# Thus the flags to break the loop for staying fast boiiii.
for string in string_list:
    two_flag = False
    three_flag = False
    chars = set(string)
    for char in chars:
        if string.count(char) == 2 and not two_flag:
            two_flag = True
            occurence_counter["two"] += 1
        elif string.count(char) == 3 and not three_flag:
            three_flag = True
            occurence_counter["three"] += 1
        if two_flag and three_flag:
            break
# The product of the two counters.
answer = occurence_counter["two"] * occurence_counter["three"]
print(answer)
