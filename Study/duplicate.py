# given list
l = [1,1,2,4,55,6,7,7,7,8,8,8,8,8,5,5,5,6]
# using set to get unique items and then convert to list
# drawback.. we are not keeping the order
new_list = list(set(l))
newlist = []
repeatedlist = []

for _ in l:
    if _ not in newlist:
        newlist.append(_)
    else:
        if _ not in repeatedlist:
            repeatedlist.append(_)

print(newlist)
print(repeatedlist)

