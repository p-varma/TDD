s = "aabbbbbcccdddddd"
# get unique char elements
unique_char = set(s)
print(unique_char)
unique_char_list = list(unique_char)
unique_char_list.sort()
output = ""
for item in unique_char_list:
    item_count = 0
    # check the str item in entire string to find the number of repeat
    for element in s:
        if item == element:
            item_count += 1

    output += "{}{}".format(item,item_count)

print(output)



