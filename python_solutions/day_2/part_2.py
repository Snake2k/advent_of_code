input_file = open("./part_2_input.txt", "r")
strings_list = [i.strip() for i in input_file.readlines()]
input_file.close()
found = False
for x in range(len(strings_list)):
    for y in range(x, len(strings_list)):
        difference = 0
        for z in range(len(strings_list[x])):
            if strings_list[x][z] != strings_list[y][z]:
                difference += 1
        if difference == 1:
            s1 = set(strings_list[x])
            s2 = set(strings_list[y])
            sf = s1.intersection(s2)
            a1 = ''.join(sf)
            a2 = ''.join([i for i in strings_list[x] if i in sf])
            found = True
            break
    if found:
        break
print(a1)
print(a2)
