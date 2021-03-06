input_file = open("./part_2_input.txt", "r")
strings_list = [i.strip() for i in input_file.readlines()]
input_file.close()
# So, this is what's happening.
# You loop through the list.
# On each loop you loop through the rest of it
# Match each character position and the character
# If it matches, add it to a list
# If it doesn't, add one to differences in the two strings
# We want to find that one difference
# Once we have that one difference
# Join the list
# Gobhwam, you're done.
found = False
for x in range(len(strings_list)):
    for y in range(x, len(strings_list)):
        difference = 0
        answer = ""
        for z in range(len(strings_list[x])):
            if strings_list[x][z] != strings_list[y][z]:
                difference += 1
            else:
                answer += strings_list[x][z]
        if difference == 1:
            found = True
            break
    if found:
        break
print(''.join(answer))
