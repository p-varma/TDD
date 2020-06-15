# min will always start from 0 for any array
# max will be length -1
# since we dont know the length of array before calling function,
# we are setting max to None and changing it to len -1 for the first iteration
# this is done to avoid asking user to input min and max value
# the function just need sorted list and element to search
# the function will return the index of element if found else -1
def search(items,item,min=0,max=None):
    # change the value to max to length -1 for the first iteration
    if max == None:
        max = len(items) - 1
    # find the mid of the given min and max values denoting sublist
    mid = (min + max) // 2

    if max >= min:

        if items[mid] == item:
            return mid
        # if the mid element value is less than number then move the min to mid +1
        elif items[mid] < item:
            return search(items, item, mid + 1, max)
        # if the mid element value is greater than number then move the max to mid -1
        else:
            return search(items, item, min, mid - 1)
    else:
        return -1





if __name__ == '__main__':

    l1 = [1,2,3,5,6,7,2,3,466,7,44,3,12,34,56,67,68,33,44,86]
    found = search(sorted(l1),12)
    print(found)