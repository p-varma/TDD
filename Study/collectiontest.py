from collections import UserList,UserDict


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deleltion
    # from List
    def remove(self, a=None):
        raise RuntimeError("Deletion not allowed")

        # Function to stop pop from

    # List
    def pop(self, a=None):
        raise RuntimeError("Deletion not allowed")

    # Driver's code

    def append(self, a=None):
        raise RuntimeError("append not allowed")



L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
#L.append(5)
print("After Insertion")
print(L)
print(type(L))


class MyDict(UserDict):

    # Function to stop deleltion
    # from dictionary
    #def __del__(self):
       # raise RuntimeError("Deletion not allowed")

        # Function to stop pop from

    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

        # Function to stop popitem

    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")

    def __setitem__(self, k=None, v = None) :
        raise RuntimeError("Addition not allowed")



d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

print("Original Dictionary")
print(d)
d['d'] = 4
d.up
print(d)
d.pop()

