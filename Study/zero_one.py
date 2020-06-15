l =[0,1,1,0,1,1,0,0,1]

newlist = []

for _ in l:
    if _ == 0:
        newlist.insert(_,0)
    else:
        newlist.append(_)

print(newlist)
