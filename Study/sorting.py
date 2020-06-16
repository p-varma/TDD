# selection sort
l = [64, 25, 12, 22, 11]

# Traverse through all list elements
for i in range(len(l)):

    # Find the minimum element in remaining
    # unsorted list
    min_index = i
    for j in range(i + 1, len(l)):
        if l[min_index] > l[j]:
            min_index = j

            # Swap the found minimum element with
    # the first element
    l[i], l[min_index] = l[min_index], l[i]

# Driver code to test above
print("Sorted array")
for i in range(len(l)):
    print("%d" % l[i]),

########################################################################
# Bubble sort

l = [64, 25, 12, 22, 11]

for i in range(len(l)):
    for j in range(len(l) - i - 1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]


print('Bubblesort')
print(l)